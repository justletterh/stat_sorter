import os,sys

div="-"*os.get_terminal_size().columns
fp=lambda *x:os.path.join(".",*x)
j=lambda *x:os.path.join(*x)
ishere=lambda x:os.path.exists(x)

def perr(s):
    res=sys.stderr.write(s+"\n")
    sys.stderr.flush()
    return res

def yn(s):
    res=False
    def ask(s):
        o=input(s).lower().replace(" ","")
        if len(o)>0:
            o=o[0]
        return o
    s+=" (y/n): "
    ans=ask(s)
    while not ans in ["y","n"]:
        perr("Try Again.")
        ans=ask(s)
    if ans=="y":
        res=True
    return res

def loop(l):
    run=True
    while run:
        ask=lambda:input("Enter A Stat Name Or 'q' To Quit: ").replace("  "," ").lower()
        i=ask()
        if i.replace(" ","")=="" or i in l:
            perr("Try Again.")
        else:
            while i[0].isspace():
                i=i[1:]
            while i[-1].isspace():
                i=i[:-1]
            if i=="q":
                run=False
            else:
                l.append(i)
                print(f"Added {repr(i)} Successfully!")
    return l

def main(*,infp=fp("in.txt")):
    l=[]
    orig=0
    if ishere(infp):
        res=yn("I Have Detected An Existing Input File,\nWould You Like To Append To It?")
        if res:
            f=open(infp,"r+")
            s=f.read()
            f.close()
            for i in s.split("\n"):
                while "  " in i:
                    i=i.replace("  ","")
                i=i.lower()
                if not i in l:
                    l.append(i)
            print(f"Successfully Imported {len(l)} Stats!")
            orig=len(l)
        print(div)
    l=loop(l)
    print(div)
    if ishere(infp):
        res=yn("Are You Sure You Want To Overwrite The Existing File?")
        if res:
            if len(l)!=orig:
                save(infp,l)
            else:
                perr("No Changes Detected.")
    else:
        save(infp,l)

def save(f,l):
    print(f"Saving {len(l)} Stats...")
    f=open(f,"w+")
    f.write("\n".join(l))
    f.close()

def init(quiet=False):
    print(div)
    main()
    if not quiet:
        print("Done!!!")

if __name__=="__main__":
    init()