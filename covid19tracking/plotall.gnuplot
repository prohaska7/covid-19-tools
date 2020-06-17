set xdata time
set timefmt '%Y%m%d'
set xrange ['20200301':'20200701']
set logscale y
set yrange [100:100000000]
set terminal png
set output 'covid-19-usa.png'
set key right bottom
set title 'COVID-19 USA (data from covidtracking.com)'
plot 'tests.csv' using 1:2 title 'tests','positives.csv' using 1:2 title 'positives','hospitalizations.csv' using 1:2 title 'hospitalizations', 'deaths.csv' using 1:2 title 'deaths', 'recovered.csv' using 1:2 title 'recovered','hcurrent.csv' using 1:2 title 'hcurrent','icu.csv' using 1:2 title 'icu'
