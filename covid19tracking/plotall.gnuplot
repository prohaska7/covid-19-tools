set xdata time
set timefmt '%Y%m%d'
set xrange ['20200301':'20200501']
set logscale y
set yrange [100:10000000]
set terminal png
set output 'covid19.png'
set key right bottom
set title 'COVID-19 USA Trends'
plot 'tests.csv' using 1:2,'positives.csv' using 1:2,'hospitalizations.csv' using 1:2, 'deaths.csv' using 1:2
