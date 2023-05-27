import os,sys

for i in range(len(sys.argv)):
    "sys.argv[%d] = %s" % (i, sys.argv[i])
if len(sys.argv) != 5:
    print('''python PyExport input activityscore coldata bedfile''')
    exit(0)

fin = open(sys.argv[1],"r")
fout1 = open(sys.argv[2], "w")
fout2 = open(sys.argv[3], "w")
fout3 = open(sys.argv[4], "w")

fout1.write("region"+"\t"+"score"+"\n")
fout2.write("seqnames"+"\t"+"start"+"\t"+"end"+"\t"+"genomic_note"+"\t"+"genome_build"+"\n")

for line in fin:
    line = line.rstrip()
    if(line.startswith("seqnames")):
        continue
    else:
        s = line.split("\t")
        chrom = s[0]
        start = s[1]
        end = s[2]
        score = s[3]
        fout1.write(">"+chrom+":"+start+"-"+end+"\t"+score+"\n")
        fout2.write(chrom[3:]+"\t"+start+"\t"+end+"\t"+"synthetic"+"\t"+"hg19"+"\n")
        fout3.write(chrom+"\t"+start+"\t"+end+"\n")

fin.close()
fout1.close()
fout2.close()
fout3.close()

