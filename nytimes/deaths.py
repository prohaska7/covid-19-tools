import sys
def main():
    bydate = {}
    for l in sys.stdin:
        f = l.split(',')
        if f[0] == 'date':
            continue
        d = int(f[4])
        try:
            bydate[f[0]] += d
        except:
            bydate[f[0]] = d
    for k in bydate.keys():
        print k, bydate[k]
    return
if __name__ == '__main__':
    main()
    
