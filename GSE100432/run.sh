python PyExport.py GSE100432_differential_peaks_inhibitor_vs_no-inhibitor_supp.table2.tsv ActivityScore.txt colData.txt BedFile.bed
bedtools getfasta -fi /wynton/home/ahituv/liuzhe/data/human/hg19/GRCh37.p13.genome.fa -bed BedFile.bed > fasta.fa
xargs -l2 < fasta.fa > seq.txt
python PyFormat.py seq.txt rowRanges.txt
