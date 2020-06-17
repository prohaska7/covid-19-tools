import sys
def main():
    tests = open('tests.csv','w')
    positives = open('positives.csv','w')
    hospitalizations = open('hospitalizations.csv','w')
    hcurrent = open('hcurrent.csv','w')
    icu = open('icu.csv','w')
    deaths = open('deaths.csv','w')
    recovered = open('recovered.csv','w')
    for l in sys.stdin:
        f = l.split(',')
        if f[0] == 'date':
            continue
        d = f[0]
        try:
            pos = int(f[2])
        except:
            pos = 0
        try:
            neg = int(f[3])
        except:
            neg = 0
        try:
            pending = int(f[4])
        except:
            pending = 0
        n_tests = pos+neg+pending
        print >>tests, d, n_tests
        print >>positives, d, pos
        try:
            n_hcurrent = int(f[5])
        except:
            n_hcurrent = None
        try:
            h = int(f[6])
        except:
            h = None
        try:
            h17 = int(f[17])
        except:
            h17 = None
        if h is not None:
            n = h
        elif h17 is not None:
            n = h17
        else:
            n = n_hcurrent
        n_hospitalizations = n
        if n_hospitalizations is not None and n_hospitalizations != n_tests:
            print >>hospitalizations, d, n_hospitalizations
        try:
            n = int(f[5])
        except:
            n = None
        if n is not None:
            print >>hcurrent, d, n
        try:
            n = int(f[7])
        except:
            n = None
        if n is not None:
            print >>icu, d, n
        try:
            n = int(f[16])
            if n != n_tests:
                print >>deaths, d, n
        except:
            pass
        try:
            n = int(f[11])
            print >>recovered, d, n
        except:
            pass
    return
if __name__ == '__main__':
    main()
    
