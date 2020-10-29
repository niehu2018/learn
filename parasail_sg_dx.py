#!/usr/bin/env python
import re
import sys
import pysam
import parasail
from itertools import islice

def parseAlignment(result):
	# Traceback pair-wise alignment
	aligned_query  = result.traceback.query
	aligned_target = result.traceback.ref

	# Define gaps and alignment blocks
	regex = r"^(-*)([ATCG-]+?)(-*)$"
	matches = re.finditer(regex, aligned_query)
	(left_gap, mid, right_gap) = (0,0,0)
	for it in matches:
		left_gap = len(it.group(1))
		mid  = len(it.group(2))
		right_gap = len(it.group(3))
		break

	# alignment start and end in reference/target
	aligned_target_nogap = aligned_target.replace('-','') # reference/target length
	target_len = len(aligned_target_nogap) # target sequence length
	start = left_gap # alignment start position in target
	end = target_len - right_gap # alignment end position in target

	# block coordinates
	aligned_query_block = aligned_query[left_gap:(left_gap + mid)]
	aligned_ref_block   = aligned_target[left_gap:(left_gap + mid)]

	# count match, mismatch, insert, deletion
	(match, mismatch, insert, deletion) = (0,0,0,0)
	for index in range(len(aligned_ref_block)):
		query_base = aligned_query_block[index]
		ref_base = aligned_ref_block[index]
		if query_base == ref_base: # Match
			match = match + 1
		elif query_base == "-":    # Insertion in reference
			insert = insert + 1
		elif ref_base == "-":      # Deletion in reference
			deletion = deletion + 1
		else:                      # Mismatch
			mismatch = mismatch + 1
	return match, mismatch, insert, deletion, start, end

if len(sys.argv) != 2:
	msg = ['python', sys.argv[0], 'infile', '> out.txt']
	msg = ' '.join([str(x) for x in msg])
	print(msg)
	print("This program align two input sequences using semi-global algorithm")
	print('\tinfile: Input file in fasta format, allowing two sequence')
	print('\tThe first sequene is the query, the second is the target')
	print('Author: Hu Nie, niehu@genetics.ac.cn, 2020-10-29')
	quit()

# Arguments
infile = sys.argv[1] # input fasta file

# Align using parasail
# Read the first two sequences
# Set the first sequence as the query
# Set the second sequence as the target
# Ignore other sequence in input file
count = 0
query_name = ""
query_seq = ""
target_name = ""
target_seq = ""
with pysam.FastxFile(infile) as fa_in:
	for cnt, read in enumerate(islice(fa_in,None)):
		count += 1
		if count == 1: # query
			query_seq = read.sequence
			query_name = read.name
		elif count == 2: # target
			target_seq = read.sequence
			target_name = read.name
		else: # stop
			break

# set score
gap_open, gap_extend = 8, 4
score_matrix = parasail.matrix_create("ACGT", 5, -5)

# semi-global alignment
result = parasail.sg_dx_trace(query_seq, target_seq, gap_open, gap_extend, score_matrix)
aligned_query  = result.traceback.query
aligned_target = result.traceback.ref
match, mismatch, insert, deletion, start, end = parseAlignment(result)
summary = ['match:' + str(match), 'mismatch:' + str(mismatch), 'insertion:' + str(insert), 'deletion:' + str(deletion), \
		'match_start:' + str(start + 1), 'match_end:' + str(end)]
summary = ' '.join([str(x) for x in summary])
print("Input  | " + 'query:' + query_name + ' target:' + target_name)
print("Summary| " + summary)
print("Query  | " + aligned_query)
print("Target | " + aligned_target)
