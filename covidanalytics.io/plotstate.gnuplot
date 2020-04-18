set xdata time
set timefmt '%Y-%m-%d'
set xrange ['2020-04-01':'2020-06-01']
set logscale y
set yrange [10:100000]
#set terminal png
#set output 'covid-19-MA.png'
set key right bottom
set title 'COVID-19 @STATE@ (data from covidanalytics.io)'
set datafile separator ','
plot 'ma.csv' using 4:6 title 'active','ma.csv' using 4:7 title 'hospital','ma.csv' using 4:10 title 'vent','ma.csv' using 4:9 title 'deaths'

