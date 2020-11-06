bash ~/github.com/prohaska7/covid-19-tools/covid19tracking/runone.bash USA 100:2000000
for state in MA IL SC CT OH IA; do
    bash ~/github.com/prohaska7/covid-19-tools/covid19tracking/runone.bash $state 10:100000
done
