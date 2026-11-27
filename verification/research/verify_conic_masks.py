#!/usr/bin/env python3
"""Exhaustive exact conic mask tests, including non-split and prime-power components."""
from collections import Counter, defaultdict
from itertools import product
from math import gcd


def torus_counts(N, c):
    out = Counter()
    for x,y in product(range(N), repeat=2):
        n = (x*x-c*y*y)%N
        if gcd(n,N)!=1:
            continue
        z=pow(n,-1,N)
        C=(x*x+c*y*y)*z%N; D=2*x*y*z%N
        assert (C*C-c*D*D)%N==1
        out[C,D]+=1
    exact={(C,D) for C,D in product(range(N),repeat=2) if (C*C-c*D*D)%N==1}
    phi=sum(gcd(a,N)==1 for a in range(N))
    assert set(out)==exact and set(out.values())=={phi}
    return out


def main():
    cases=targets=transitions=fibres=0
    for N in (15,21,35,45,63,77,105):
        units=[u for u in range(N) if gcd(u,N)==1]
        tors={c:torus_counts(N,c) for c in units}
        cases+=len(tors)
        for k in (-1,1,2,5):
            k%=N
            if gcd(k,N)!=1:continue
            # A norm-one and, when available, a different unit-norm fibre.
            params={(0,1,1)}
            if gcd(4-k,N)==1:params.add((1,2,(4-k)%N))
            for h0,z0,q in sorted(params):
                full={(h,z) for h,z in product(range(N),repeat=2)
                      if (z*z-k*h*h)%N==q}
                points=Counter(((h0*C+z0*D)%N,(z0*C+k*h0*D)%N)
                               for C,D in tors[k])
                assert set(points)==full and set(points.values())=={1}
                valid={(h,z) for h,z in full if gcd(h,N)==1}
                pub=defaultdict(set)
                for h,z in valid:pub[h*h%N,z].add(h)
                for (s,z),hs in pub.items():
                    assert hs=={h for h in units if h*h%N==s}
                    fibres+=len(hs)
                    # Test the public mask against every private sign fibre.
                    c=k*s%N
                    for h in hs:
                        got=Counter()
                        for C,D in tors[c]:
                            a=(C+D*z)%N; zp=(C*z+c*D)%N; sp=s*a*a%N
                            hp=h*a%N
                            assert hp*hp%N==sp and (zp*zp-k*sp)%N==q
                            assert (gcd(a,N)==1)==(gcd(hp,N)==1)
                            got[hp,zp]+=1;transitions+=1
                        assert set(got)==full and set(got.values())=={1}
                        assert {u for u in got if gcd(u[0],N)==1}==valid
                        targets+=1
    print('exact norm-one group laws:',cases,'target/fibre refreshes:',targets,
          'point transitions:',transitions,'private fibre checks:',fibres)


if __name__=='__main__':main()
