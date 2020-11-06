def main():
    # import state population
    pop = {} # map state name -> population
    with open('states_population.csv','r') as fd:
        for l in fd:
            l = l[:-1]
            f = l.split(',')
            pop[f[0]] = int(f[2])
            pop[f[1]] = int(f[2])

    # import total tests per state
    tests = {} # map state name -> number of tests
    schema = {} # map column name -> column index
    with open('states_current.csv','r') as fd:
        for l in fd:
            l = l[:-1]
            f = l.split(',')
            if f[0] == 'date':
                for i in range(len(f)):
                    schema[f[i]] = i
                continue
            try:
                tests[f[schema['state']]] = int(f[schema[f[schema['totalTestResultsSource']]]])
            except:
                pass

    # compute per capita tests per state
    for s in tests.keys():
        if not tests.has_key(s):
            print s, 'skipped tests'
            continue
        if not pop.has_key(s):
            print s, 'skipped pop'
            continue
        print "%s\t%d\t%d\t%.2f%%" % (s, tests[s], pop[s], 100.0*float(tests[s])/pop[s])

if __name__ == '__main__':
    main()
