set xdata time
set timefmt '%Y%m%d'
set xrange ['20200301':'20201201']
set logscale y
set yrange [10:@YLIMIT@]
set terminal png size 800,600
set output 'covid-19-@STATE@.png'
set key left top vertical Left reverse
set xtics format '%m'
set title 'COVID-19 @STATE@ (data from covid19tracking.com)'
plot 'tests.csv' using 1:2 title 'daily tests','positives.csv' using 1:2 title 'daily positives', 'hcurrent.csv' using 1:2 title 'current in hospital','icu.csv' using 1:2 title 'current in icu', 'deaths.csv' using 1:2 title 'daily deaths','hincrease.csv' using 1:2 title 'daily hospital'

