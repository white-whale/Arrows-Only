import sys, os
import fileinput

funcString = "function ("
openBracket = '('
closingBracket = ') {'
arrowSyntax = ') => {'

def main():

    if (len(sys.argv) < 2 or len(sys.argv) > 3):
        print 'ERROR:'
        print 'Please supply either a directory to a folder containing JavaScript files, or a JavaScript file and an optional output file name in the following formats:'
        print '----------------------------------------'
        print 'To convert all files in a directory:'
        print 'python func-to-arrow.py "directory-to-folder"'
        print 'To convert a single file with optional output file:'
        print 'python func-to-arrow.py "JavaScript-file.js" "output-file.js"'

    elif (len(sys.argv) == 2):
        input1 = sys.argv[1]
        jsFileExt = '.js'
        # newFileName = sys.argv[1].split('.')[0] + '-new.' + sys.argv[1].split('.')[1]
        if (jsFileExt in input1):
            parseFile(input1, False, False)
        else:
            for f in os.listdir(input1):
                if (jsFileExt in f):
                    parseFile(f, False, input1)

    elif (len(sys.argv) == 3):
        fileIn = sys.argv[1]
        fileOut = sys.argv[2]

        if ((jsFileExt in sys.argv[1]) and (jsFileExt in sys.argv[2])):
            parseFile(open(fileIn), fileOut, False)
        else:
            print 'Please check your file types'

    exit()


def parseFile(fileIn, fileOut, directory):
    if (fileOut):
        newFileName = fileOut

    else:
        newFileName = str(fileIn).split('.')[0] + '-new.' + fileIn.split('.')[1]

    if (directory):
        fileIn = os.path.join(directory, fileIn)
        newFile = open(os.path.join(directory, newFileName), 'a+')

    else:
        newFile = open(newFileName, 'a+')

    for line in open(fileIn):
        newFile.write(arrowStyle(line))

    newFile.close();

def arrowStyle(line):
    if (funcString in line):
        newLine = line.replace(funcString, openBracket)
        newLine = newLine.replace(closingBracket, arrowSyntax)
        return newLine
    else:
        return line

main()
