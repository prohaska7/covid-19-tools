bash ~/github.com/prohaska7/covid-19-tools/covid19tracking/plotall.bash
for state in MA IL SC CT OH IA; do
    bash ~/github.com/prohaska7/covid-19-tools/covid19tracking/runone.bash $state
done
