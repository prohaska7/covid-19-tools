dates=$(tail -n +2 covid_analytics_projections.csv | cut -d, -f4  | sort | uniq)
for x in $dates;do
    bash deaths.bash "North America,US" "$x" >estimate-$x.csv
done
