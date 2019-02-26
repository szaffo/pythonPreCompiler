import sys
import re

# GLOBALS
file = ""
RECURSON = False
saveTo = "compiled.py"


def argParse():
    global file
    global RECURSON
    global saveTo

    args = sys.argv[1:]
    print(args)

    ind = 0
    while ind < len(args):

        arg = args[ind]

        if re.match(r"[A-z\*0-9aáöőüűuú/\.]*.py$", arg):
            # File
            file = arg

        elif re.match(r"^-{1,2}[rR](ecursion|ecurson|ecursive)?$", arg):
            # -recursive switch
            RECURSON = True

        elif re.match(r"^-{1,2}[sS](ave)?$", arg):
            # save to

            try:
                saveTo = args[ind + 1]
                ind += 1
            except:
                pass

        ind += 1


def read(file):
    try:
        with open(file, 'r') as f:
            text = f.read().split("\n")

    except:
        print("Can't open file. ", file)
        return []

    return text


def isInclude(text):
    return re.match(r"^# ?include\s*[A-z\./aáoóöőuúüű]+\.py\s*$", text)


def compile(file):
    text = read(file)

    for line in text:
        # print(">{}<".format(line))

        if isInclude(line):
            print(line)
        else:
            # print(line)
            continue




if __name__ == '__main__':
    argParse()

    print(file)
    print(saveTo)

    compile(file)
