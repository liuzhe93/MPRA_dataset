import os,sys

for i in range(len(sys.argv)):
    "sys.argv[%d] = %s" % (i, sys.argv[i])
if len(sys.argv) != 3:
    print('''python PyExport input activityscore''')
    exit(0)

fin = open(sys.argv[1],"r")
fout = open(sys.argv[2], "w")

fout.write("loci"+"\t"+"seq"+"\n")

for line in fin:
    line = line.rstrip()
    s = line.split(" ")
    loci = s[0]
    seq = s[1]
    fout.write(loci+"\t"+seq+"\n")

fin.close()
fout.close()
