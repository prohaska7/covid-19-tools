import sys
def main():
    bydate = {}
    for l in sys.stdin:
        f = l.split(',')
        if f[0] == 'date':
            continue
        c = int(f[3])
        try:
            bydate[f[0]] += c
        except:
            bydate[f[0]] = c
    for k in bydate.keys():
        print k, bydate[k]
    return
if __name__ == '__main__':
    main()
    
