def main():
    schema = []
    rschema = {}
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
            break
        fd.close()
    for i in range(len(schema)):
        print i, schema[i]

if __name__ == '__main__':
    main()
    
