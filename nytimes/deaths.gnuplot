set xdata time
set timefmt '%Y-%m-%d'
set xrange ['2020-01-01':'2020-05-01']
set logscale y
set yrange [1:100000]
set terminal png
set output 'deaths.png'
plot 'deaths.csv' using 1:2
