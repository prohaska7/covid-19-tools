STATE=MA
if [ $# -ge 1 ] ; then STATE=$1; fi
YRANGE=10:100000
if [ $# -ge 2 ] ; then YRANGE=$2; fi
if [ $STATE = "USA" ] ; then
    cp us_daily.csv $STATE.csv
else
    egrep "date|$STATE" states_daily_4pm_et.csv >$STATE.csv
fi
python ~/github.com/prohaska7/covid-19-tools/covid19tracking/extract-data.py <$STATE.csv
temp=$(mktemp)
sed -e "s/@STATE@/$STATE/" -e "s/@YRANGE@/$YRANGE/" <~/github.com/prohaska7/covid-19-tools/covid19tracking/plot-data.gnuplot > $temp
gnuplot $temp
rm $temp

