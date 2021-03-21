import os

div="-"*os.get_terminal_size().columns

def main():
    quiet=True
    from stage1 import init as a
    from stage2 import init as b
    from stage3 import init as c
    a(quiet)
    b(quiet)
    c(quiet)

def init(quiet=False):
    main()
    if not quiet:
        print(f"{div}\nDone!!!\n{div}")
    else:
        print(div)

if __name__=="__main__":
    init()