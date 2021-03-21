import os,json,sys

div="-"*os.get_terminal_size().columns
toj=lambda d:json.dumps(d)
fp=lambda *x:os.path.join(".",*x)
j=lambda *x:os.path.join(*x)

def main(*,outfp=fp("out.json"),infp=fp("in.txt")):
    l=getl(infp)
    d={"m":"mind","b":"body","s":"soul","i":"interactions"}
    if not os.path.exists(outfp):
        o={}
        for k in d:
            v=d[k]
            o[v]=[]
    else:
        f=open(outfp,"r+")
        o=json.load(f)
        f.close()
    o=loop(l,d,o)
    f=open(outfp,"w+")
    f.write(toj(o))
    f.close()

def getl(infp=fp("in.txt")):
    f=open(infp,"r+")
    s=f.read().split("\n")
    f.close()
    l=[]
    for i in s:
        if not i.isspace() and i!="":
            i=i.lower()
            while "  " in i:
                i=i.replace("  "," ")
            l.append(i)
    return l

def loop(l,d,o):
    change=False
    for i in l:
        if not i in tol(o):
            change=True
            break
    if change:
        def hlp(*,indent=2):
            print("Help:")
            for k in d:
                v=d[k]
                print(f"{' '*indent}{repr(k)} = {v.capitalize()}")
        ask=lambda i:input(f"What Group Is {repr(i)} In?: ").lower()[0]
        hlp()
        for i in l:
            if not i in tol(o):
                ans=ask(i)
                while ans not in list(d.keys()):
                    perr("Try Again!")
                    ans=ask(i)
                o[d[ans]].append(i)
    else:
        perr("No New Skills To Add.")
    for k in o:
        v=o[k]
        v.sort()
    return o

def tol(d):
    l=[]
    for k in d:
        v=d[k]
        for i in v:
            l.append(i)
    return l

def perr(s,*,nl=True):
    if not s.endswith("\n") and nl:
        s+="\n"
    res=sys.stderr.write(s)
    sys.stderr.flush()
    return res

def init(quiet=False):
    print(div)
    main()
    if not quiet:
        print(f"{div}\nDone!!!\n{div}")
    else:
        print(div)
    
if __name__=="__main__":
    init()