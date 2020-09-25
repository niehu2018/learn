# download page
cat samples.txt | while read a;do wget -c https://www.ncbi.nlm.nih.gov/sra/?term=${a} ;done

# extract sample name
cat samples.txt | while read a;do echo "cat index.html\?term\=${a}  | grep \"<title>GSM\" | sed 's/.*GSM/GSM/'| sed 's/;.*//'| sed 's/: /    /' ";done > extract.sh
sh extract.sh | paste samples.txt - >srr_gsm_sn.txt
