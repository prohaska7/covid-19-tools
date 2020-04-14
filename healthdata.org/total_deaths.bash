DATE="2020-04-01"
if [ $# = 1 ] ; then DATE=$1; fi
python total_deaths.py $DATE | sort -k 3,4 -n -r -t,
