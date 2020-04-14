import sys
def main():
    check_date = '2020-04-01'
    if len(sys.argv) == 2:
        check_date = sys.argv[1]

    # import state population
    states_pop = {}
    fd = open('us_states_population.csv','r')
    if fd:
        for l in fd:
            l = l[:-1]
            f = l.split(',')
            states_pop[f[0]] = int(f[2])
            states_pop[f[1]] = int(f[2])
        fd.close()
        t = 0
        for k in states_pop.keys():
            t += states_pop[k]
        states_pop['United States of America'] = t

    # import Hospitalizations
    schema = []
    rschema = {}
    data = []
    fd = open('Hospitalization_all_locs.csv','r')
    if fd:
        first = True
        for l in fd:
            if l.endswith('\n'):
                l = l[:-1]
            f = l.split(',')
            for i in range(len(f)):
                f[i] = f[i].replace('"','')
            if first:
                schema = f
                for i in range(len(schema)):
                    rschema[schema[i]] = i
                first = False
            else:
                data.append(f)
        fd.close()
        
    if False:
        print schema
        print rschema
        for i in range(len(data)):
            print data[i]
    for r in range(len(data)):
        dr = data[r]
        location = dr[rschema['location_name']]
        if states_pop.has_key(location) and dr[rschema['date']] == check_date:
              print '%s,%s,%.0f' % (dr[rschema['date']], dr[rschema['location_name']], float(dr[rschema['totdea_mean']]))

if __name__ == '__main__':
    main()
    
