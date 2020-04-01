last=$(tail -n +2 us-states.csv|cut -f1 -d,|sort|tail -1)
awk -F, "\$1 == \"$last\" { print }" us-states.csv | sort -t, -k4,4 -n -r
