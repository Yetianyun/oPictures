#去重
def qch(zf):
    zf.replace(")","")
    zf.replace("(","")
    zf = zf.strip()
    l = len(zf)
    for i in range(2,l):
        if ( l % i == 0 ):
            m = 0
            jzf = zf[0:i]
            for j in range(0,l-1,i):
                xzf = zf[j:j+i]
                if ( xzf != jzf ):
                    m = 1
                    break
            if ( m == 0 ):
                return xzf

        print("\n")

if __name__ == '__main__':
    zf = 'WLWLWL'
    tl = qch(zf)
    print(tl)
