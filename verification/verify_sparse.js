// Reproduce with: node verify_sparse.js
// Exact finite consistency checks, not proofs of analytic estimates.
function checks() {
  "use strict";
  let state=0x71f21ab3, count=0;
  const rand=(m)=>{state^=state<<13;state^=state>>>17;state^=state<<5;return (state>>>0)%m;};
  const check=(b,msg)=>{count++;if(!b)throw Error(msg);};
  const mul=(a,b)=>{let z=0;while(b){if(b&1)z^=a;b>>>=1;a<<=1;if(a&256)a^=0x11b;}return z;};
  const pow=(a,n)=>{let z=1;while(n){if(n&1)z=mul(z,a);a=mul(a,a);n>>>=1;}return z;};
  const inv=a=>{if(!a)throw Error("division by zero");return pow(a,254);};
  const zero=n=>Array(n).fill(0), dot=(a,b)=>a.reduce((z,x,i)=>z^mul(x,b[i]),0), mv=(A,x)=>A.map(a=>dot(a,x));
  const tr=A=>A[0].map((_,j)=>A.map(a=>a[j])), xor=(a,b)=>a.map((x,i)=>x^b[i]), scale=(a,c)=>a.map(x=>mul(x,c));
  const equal=(a,b)=>a.every((x,i)=>x===b[i]);
  const rank=(A)=>{if(!A.length)return 0;let a=A.map(v=>v.slice()),r=0;for(let j=0;j<a[0].length&&r<a.length;j++){let i=r;while(i<a.length&&!a[i][j])i++;if(i===a.length)continue;[a[i],a[r]]=[a[r],a[i]];a[r]=scale(a[r],inv(a[r][j]));for(let k=r+1;k<a.length;k++)a[k]=xor(a[k],scale(a[r],a[k][j]));r++;}return r;};
  function bm(seq){
    let C=[1],D=[1],l=0,delay=1,last=1;
    for(let n=0;n<seq.length;n++){
      let v=seq[n];for(let i=1;i<=l;i++)v^=mul(C[i]||0,seq[n-i]);
      if(!v){delay++;continue;}
      let T=C.slice(),coef=mul(v,inv(last));while(C.length<D.length+delay)C.push(0);
      for(let j=0;j<D.length;j++)C[j+delay]^=mul(coef,D[j]);
      if(2*l<=n){l=n+1-l;D=T;last=v;delay=1;}else delay++;
    }
    while(C.length<l+1)C.push(0);
    return C.slice(0,l+1).reverse();
  }
  for(let x=1;x<256;x++)check(mul(x,inv(x))===1,"field inverse");
  let algebra={gram:0,projection:0,blind:0};
  // Compare explicit Euler entries against the rank-one decompositions.
  for(let rep=0;rep<500;rep++){
    const H=2+rand(9), npr=1+rand(4), B=Array.from({length:H},()=>Array(H).fill(1));let smooth=true;
    for(let k=0;k<npr;k++){
      const h=Array.from({length:H},()=>rand(2)?1:-1),e=1+rand(8),small=rand(3)===0,chi=small?1:(rand(2)?1:-1);
      const v=Array.from({length:H},()=>small?1:(rand(2)?1:-1));smooth&&=small;
      for(let a=0;a<H;a++)for(let b=0;b<H;b++){
        let same=h[a]===h[b], alpha=v[a]*v[b], explicit;
        if(same){explicit=0;for(let j=0;j<=e;j++)explicit+=alpha**j*(chi*alpha)**(e-j);}
        else explicit=e%2?0:chi**(e/2);
        let gram;
        if(chi===1&&e%2===1)gram=(e+1)*(same?alpha:0);
        else if(chi===1)gram=(e+2)/2+(e/2)*h[a]*h[b];
        else if(e%2)gram=0;
        else gram=(e/2)%2?h[a]*h[b]:1;
        check(gram===explicit,"Euler Gram identity");algebra.gram++;
        if(small)check(gram>=1 || (e%2===1&&!same&&gram===0),"smooth local decomposition");
        B[a][b]*=gram;
      }
      // The Gram decomposition for small primes dominates the all-ones matrix in PSD order, not entrywise.
    }
    let sum=B.reduce((z,row)=>z+row.reduce((a,b)=>a+b,0),0);
    check(sum>=0,"Schur Gram nonnegative sum");
    if(smooth)check(sum>=H*H,"smooth Gram sum");
  }
  let good=0,verified=0,full=0;
  for(let rep=0;rep<1000;rep++){
    const d=1+rand(8),m=d+3,rr=rand(d+1);
    let A=Array.from({length:d},()=>zero(m));
    let bases=Array.from({length:rr},()=>Array.from({length:m},()=>rand(2)));
    for(let i=0;i<d;i++)for(let j=0;j<rr;j++)if(rand(2))A[i]=xor(A[i],bases[j]);
    const At=tr(A),D=Array.from({length:m},()=>rand(256)),E=Array.from({length:d},()=>rand(256));
    const diag=(a,b)=>a.map((x,i)=>mul(x,b[i]));
    const bb=x=>mv(A,diag(D,mv(At,diag(E,x))));
    const cols=Array.from({length:d},(_,i)=>bb(Array.from({length:d},(_,j)=>+(i===j))));
    const B=tr(cols),B2=tr(cols.map(bb)),r=rank(A);
    let g=rank(B)===r&&rank(B2)===r;if(g)good++;
    const v=Array.from({length:m},()=>rand(256)),b=mv(A,v),w=Array.from({length:d},()=>rand(256));
    let x=zero(d),ok=true;
    if(b.some(Boolean)){
      let a=b.slice(),seq=[];for(let i=0;i<2*d;i++){seq.push(dot(w,a));a=bb(a);}
      let f=bm(seq);
      if(!f[0])ok=false;
      else {a=b.slice();for(let i=1;i<f.length;i++){x=xor(x,scale(a,f[i]));a=bb(a);}x=scale(x,inv(f[0]));ok=equal(bb(x),b);}
    }
    if(ok){
      verified++;
      let k=xor(v,diag(D,mv(At,diag(E,x))));
      check(mv(A,k).every(z=>z===0),"kernel certificate");algebra.projection++;
      let components=Array.from({length:8},(_,i)=>k.map(x=>(x>>>i)&1));
      for(let y of components){check(mv(A,y).every(z=>z===0),"binary component");algebra.projection++;}
      if(rank(components)>=3)full++;
    }
  }
  // Exhaustive CRT sign enumeration on two independent bits per hidden root.
  for(let m=2;m<=5;m++){
    for(let r=1;r<=Math.min(3,m);r++){
      for(let rep=0;rep<10;rep++){
        let E;do E=Array.from({length:r},()=>Array.from({length:m},()=>rand(2)));while(rank(E)!==r);
        const freq=Array(4**r).fill(0);
        for(let z=0;z<4**m;z++){
          let out=0;for(let i=0;i<r;i++){let a=0;for(let j=0;j<m;j++)if(E[i][j])a^=(z>>>(2*j))&3;out|=a<<(2*i);}freq[out]++;
        }
        for(let n of freq){check(n===4**(m-r),"blind uniformity");algebra.blind++;}
      }
    }
  }
  return {assertions:count,checked:algebra,fieldProjection:{attempts:1000,goodPreconditioner:good,verifiedSolutions:verified,threeIndependentBinaryVectors:full},seed:"0x71f21ab3",scope:"finite exact checks only"};
}
console.log(JSON.stringify(checks(), null, 2));

