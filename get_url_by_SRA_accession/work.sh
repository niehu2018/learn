# Step 1, download page
cat samples.txt | while read a;do wget -c https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=${a} ;done

# Step 2, extract url
cat samples.txt | while read a;do cat index.html\?run\=${a} | grep sra-pub-run | grep ncbi | sed 's/<td><a href="//' | sed 's/".*//' | head -1 ;done >url.txt
