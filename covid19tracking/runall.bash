python ~/github.com/prohaska7/covid-19-tools/covid19tracking/extract-data.py < us_daily.csv
gnuplot ~/github.com/prohaska7/covid-19-tools/covid19tracking/plotall.gnuplot 
for state in MA IL SC CT OH IA; do
    bash ~/github.com/prohaska7/covid-19-tools/covid19tracking/runone.bash $state
done
