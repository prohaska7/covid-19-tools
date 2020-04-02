import sys
def main():
    tests = open('tests.csv','w')
    positives = open('positives.csv','w')
    hospitalizations = open('hospitalizations.csv','w')
    deaths = open('deaths.csv','w')
    for l in sys.stdin:
        f = l.split(',')
        if f[0] == 'date':
            continue
        d = f[0]
        try:
            n = int(f[4])
            print >>tests, d, n
        except:
            pass
        try:
            n = int(f[2])
            print >>positives, d, n
        except:
            pass
        try:
            n = int(f[6])
            print >>hospitalizations, d, n
        except:
            pass
        try:
            n = int(f[7])
            print >>deaths, d, n
        except:
            pass
    return
if __name__ == '__main__':
    main()
    
