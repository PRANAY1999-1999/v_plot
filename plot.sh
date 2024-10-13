#!/bin/bash

cat mapped.bed | awk '{print c=(1000/($4-$3))*((($9+$10)/2)-$3)-500"\t"$12}' | sort -k1,1n -k2,2n | uniq -c | awk '{print $2,$3,$1}' |  tr ' ' '\t' > v_plot.tsv | python3 vplot.py
