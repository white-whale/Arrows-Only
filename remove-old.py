import os, sys

def main():
    if (len(sys.argv) == 2):
        if os.path.isdir(sys.argv[1]):
            parseDir(sys.argv[1])

def parseDir(folder):
    for f in os.listdir(folder):
        if ('-old.' in f):
            os.remove(os.path.join(folder, f))
        elif (os.path.isdir(os.path.join(folder, f)) and (f != 'node_modules')):
            parseDir(os.path.join(folder, f))

main()
