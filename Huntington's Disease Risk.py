"""This codes counts the number of trinucleotide CAG repeats in a given
sequence of chromosome 4 at 4p16.3(HTT) to determine penetrance of
Huntington's disease

SamiranRoy 2010073"""

seq="GCTGCCGGGACGGGTCCAAGATGGACGGCCGCTCAGGTTCTGCTTTTACCTGCGGCCCAGAGCCCCATTCATTGCCCCGGTGCTGAGCGGCGCCGCGAGTCGGCCCGAGGCCTCCGGGGACTGCCGTGCCGGGCGGGAGACCGCCATGGCGACCCTGGAAAAGCTGATGAAGGCCTTCGAGTCCCTCAAGTCCTTCCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAACAGCCGCCACCGCCGCCGCCGCCGCCGCCGCCTCCTCAGCTTCCTCAGCCGCCGCCGCAGGCACAGCCGCTGCTGCCTCAGCCGCAGCCGCCCCCGCCGCCGCCCCCGCCGCCACCCGGCCCGGCTGTGGCTGAGGAGCCGCTGCACCGACC"
count=0
maxcount=0
buff=''

for i in seq:
    buff=buff+i
    if buff.upper()=='CAG':
        buff=''
        count=count+1
    elif buff.upper()=='C':
        pass
    elif buff.upper()=='CA':
        pass
    else:
        buff=''
        if maxcount<count:
            maxcount=count
            count=0
            
if maxcount<count:
    maxcount=count       
    
if maxcount<26:
    Class='Normal'
    Status='Not Affected'
    OffspringRisk='none'
elif maxcount<36 and count>25:
    Class='Intermediate'
    Status='Not Affected'
    OffspringRisk='Elevated'
elif maxcount<40 and count>35:
    Class='Reduced Penetrance'
    Status='May Be Affected'
    OffspringRisk='50%'
elif maxcount>39:
    Class='Full Penetrance'
    Status='Affected'
    OffspringRisk='50%'





print "Count:",maxcount
print "Classification::",Class
print "Status:",Status
print "Risk to Offspring:",OffspringRisk
