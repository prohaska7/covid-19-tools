import sys
def main():
    t = []
    diffs = []
    for l in sys.stdin:
        t.append(float(l))
    for i in range(1,len(t)):
        print i, t[i], int(100*(t[i]-t[i-1])/t[i-1])
    return
if __name__ == '__main__':
    main()
    
