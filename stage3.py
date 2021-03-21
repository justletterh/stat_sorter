import os

div="-"*os.get_terminal_size().columns

def main():
    print()

def init(quiet=False):
    main()
    if not quiet:
        print("Done!!!")

if __name__=="__main__":
    init()