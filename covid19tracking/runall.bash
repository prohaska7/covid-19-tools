bash ~/github.com/prohaska7/covid-19-tools/covid19tracking/plotall.bash
for state in MA IL NY NJ NC WA ;do
    bash ~/github.com/prohaska7/covid-19-tools/covid19tracking/plotstate.bash $state 1000000
done
