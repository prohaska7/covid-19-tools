import sys
def main():
    check_date = '2020-04-01'
    if len(sys.argv) == 2:
        check_date = sys.argv[1]
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
            else:
                data.append(f)
            first = False
        fd.close()
    if False:
        print schema
        print rschema
        for i in range(len(data)):
            print data[i]
    for r in range(len(data)):
        dr = data[r]
        if dr[rschema['date']] == check_date:
              print '%s,%s,%.0f' % (dr[rschema['date']], dr[rschema['location_name']], float(dr[rschema['totdea_mean']]))

if __name__ == '__main__':
    main()
    
