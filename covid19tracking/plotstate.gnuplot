set xdata time
set timefmt '%Y%m%d'
set xrange ['20200301':'20201201']
set logscale y
set yrange [10:@YLIMIT@]
set terminal png
set output 'covid-19-@STATE@.png'
set key left top
set title 'COVID-19 @STATE@ (data from covid19tracking.com)'
plot 'tests.csv' using 1:2 title 'tests','positives.csv' using 1:2 title 'positives', 'hcurrent.csv' using 1:2 title 'hospital','icu.csv' using 1:2 title 'icu', 'deaths.csv' using 1:2 title 'deaths'

