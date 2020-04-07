def main():
    # import state population
    pop = {}
    fd = open('states_population.csv','r')
    if fd:
        for l in fd:
            l = l[:-1]
            f = l.split(',')
            pop[f[0]] = int(f[2])
            pop[f[1]] = int(f[2])
        fd.close()

    # import total tests per state
    tests = {}
    fd = open('states_current.csv','r')
    if fd:
        for l in fd:
            l = l[:-1]
            f = l.split(',')
            try:
                tests[f[0]] = int(f[22])
            except:
                pass
        fd.close()

    # compute per capita tests per state
    for s in tests.keys():
        if not tests.has_key(s):
            # print s, 'skipped tests'
            continue
        if not pop.has_key(s):
            # print s, 'skipped pop'
            continue
        print "%s\t%d\t%d\t%.2f%%" % (s, tests[s], pop[s], 100.0*float(tests[s])/pop[s])

if __name__ == '__main__':
    main()
