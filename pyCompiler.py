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
    # print(args)

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
    return re.match(r"^# ?include\s*([A-z\./aáoóöőuúüű0-9]+\.py)\s*$", text)

def getFileName(text):
    return isInclude(text).group(1)


def compile(file):
    text = read(file)

    ind = -1

    while ind < len(text) - 1:
        ind +=1

        line = text[ind]

        if not isInclude(line):
            continue

        filename = getFileName(line)

        # note that read returns a list of lines
        toCopy = read(filename)

        text = text[0:ind] + toCopy + text[ind + 1:]

        ind += 0 if RECURSON else (len(toCopy) - 1) 
        # print(text, ind)

        # print(line) 

        
    return text


def write(text, file):
    text = '\n'.join(text)
    with open(file, 'w+') as f:
        f.write(text)






if __name__ == '__main__':
    argParse()
    data = compile(file)
    write(data, saveTo)