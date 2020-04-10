import sys
def main():
    state = 'US'
    if len(sys.argv) >= 2:
        state = sys.argv[1]
    for l in sys.stdin:
        l = l[:-1]
        f = l.split(',')
        if f[0] == state:
            print '%s %s %s %s' % (f[1],f[2],f[5],f[6])
    pass
if __name__ == '__main__':
    main()
