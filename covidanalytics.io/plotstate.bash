state=$1
ylimit=100000
if [ $# = 2 ] ; then ylimit=$2; fi
egrep "North America,US,$state" covid_analytics_projections.csv >"$state.csv"

tmpplot=$(mktemp)
echo set xdata time >>$tmpplot
echo set timefmt \'%Y-%m-%d\' >>$tmpplot
echo set xrange [\'2020-04-01\':\'2020-06-01\'] >>$tmpplot
echo set logscale y >>$tmpplot
echo set yrange [100:$ylimit] >>$tmpplot
echo set terminal png >>$tmpplot
echo set output \'covid-19-$state.png\' >>$tmpplot
echo set key right bottom >>$tmpplot
echo set title \'COVID-19 $state \(data from covidanalytics.io\)\' >>$tmpplot
echo set datafile separator \',\' >>$tmpplot
echo plot \'$state.csv\' using 4:6 title \'active\',\'$state.csv\' using 4:7 title \'hospital\',\'$state.csv\' using 4:10 title \'vent\',\'$state.csv\' using 4:9 title \'deaths\' >>$tmpplot
gnuplot $tmpplot
rm $tmpplot
