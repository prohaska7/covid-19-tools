import sys
def main():
    tests = open('tests.csv','w')
    positives = open('positives.csv','w')
    hospitalizations = open('hospitalizations.csv','w')
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
        print >>tests, d, pos+neg+pending
        print >>positives, d, pos
        hcurrent = h = h15 = None
        try:
            hcurrent = int(f[5])
        except:
            pass
        try:
            h = int(f[6])
        except:
            pass
        try:
            h15 = int(f[15])
        except:
            pass
        n = h
        if n is None:
            n = h15
        if n is not None:
            print >>hospitalizations, d, n
        try:
            n = int(f[14])
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
    
