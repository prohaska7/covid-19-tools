STATE=$1
YLIMIT=100000
if [ $# = 2 ] ; then YLIMIT=$2;fi
egrep $STATE states_daily_4pm_et.csv | python ~/github.com/prohaska7/covid-19-tools/covid19tracking/plotall.py
temp=$(mktemp)
sed -e "s/@STATE@/$STATE/" -e "s/@YLIMIT@/$YLIMIT/" <~/github.com/prohaska7/covid-19-tools/covid19tracking/plotstate.gnuplot > $temp
gnuplot $temp
rm $temp
