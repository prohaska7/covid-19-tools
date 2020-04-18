where=$1
when=$2
egrep "$where" covid_analytics_projections.csv | egrep "$when" | sort -t, -k9,9 -n -r
