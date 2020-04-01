last=$(tail -n +2 us-counties.csv|cut -f1 -d,|sort|tail -1)
awk -F, "\$1 == \"$last\" && \$3 == \"$*\" { print }" us-counties.csv | sort -t, -k5,5 -n -r
