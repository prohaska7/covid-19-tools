import sys
schema = {}
def main():
    tests = open('tests.csv','w')
    positives = open('positives.csv','w')
    hospitalizations = open('hospitalizations.csv','w')
    hcurrent = open('hcurrent.csv','w')
    hincrease = open('hincrease.csv', 'w')
    icu = open('icu.csv','w')
    deaths = open('deaths.csv','w')
    recovered = open('recovered.csv','w')
    for l in sys.stdin:
        f = l.split(',')
        if f[0] == 'date':
            build_schema(f)
            continue
        d = f[0]

        try:
            pos = int(f[schema['positiveIncrease']])
        except:
            pos = 0
        try:
            neg = int(f[schema['negativeIncrease']])
        except:
            neg = 0
        print >>tests, d, pos+neg
        print >>positives, d, pos

        try:
            n = int(f[schema['hospitalizedCumulative']])
        except:
            try:
                n = int(f[schema['hospitalized']])
            except:
                try:
                    n = int(f[schema['hospitalizedIncrease']])
                except:
                    n = None
        if False and n is not None:
            print >>hospitalizations, d, n

        try:
            n = int(f[schema['hospitalizedCurrently']])
        except:
            n = None
        if n is not None:
            print >>hcurrent, d, n

        try:
            n = int(f[schema['inIcuCurrently']])
        except:
            n = None
        if n is not None:
            print >>icu, d, n

        try:
            n = int(f[schema['deathIncrease']])
        except:
            n = None
        if n is not None:
            print >>deaths, d, n

        try:
            n = int(f[schema['recovered']])
        except:
            n = None
        if False and n is not None:
            print >>recovered, d, n

        try:
            n = int(f[schema['hospitalizedIncrease']])
        except:
            n = None
        if n is not None and n > 0:
            print >>hincrease, d, n

    return 0
def build_schema(f):
    for i in range(len(f)):
        schema[f[i]] = i
if __name__ == '__main__':
    sys.exit(main())
    
