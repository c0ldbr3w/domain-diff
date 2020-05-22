# domain-diff
Simple tool to compare two lists of (sub)domains and show both the unique items in each list, plus overlap.

# Usage
git clone https://github.com/c0ldbr3w/domain-diff  
cd domain-diff  
python3 domain-diff.py infile_1.txt infile_2.txt  

# Output
Unique values in infile_1.txt:  
corp.aol.com  
yahoo.com  
  
  
Unique values in infile_2.txt:  
vpn.aol.com  
netscape.com  
www.netscape.com  
  
  
Duplicate values in both lists:  
www.aol.com  
www.yahoo.com  
