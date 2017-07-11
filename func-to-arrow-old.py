import sys
import fileinput


funcString = "function ("
openBracket = '('
closingBracket = ') {'
arrowSyntax = ') => {'

def main():

    if (len(sys.argv) < 2 or len(sys.argv) > 3):
        print 'Please supply a JavaScript file and an optional output file name in the format:'
        print 'python func-to-arrow.py "JavaScript-file.js" "output-file.js"'
        return

    elif (len(sys.argv) == 2):
        newFileName = sys.argv[1].split('.')[0] + '-new.' + sys.argv[1].split('.')[1]
        # print 'length 2 ' + newFileName
        # return

    elif (len(sys.argv) == 3):
        newFileName = sys.argv[2]
        # print 'length 3 ' + newFileName
        # return

    newFile = open(newFileName, 'a+')

    for line in fileinput.input():
        newFile.write(arrowStyle(line))

    newFile.close();
    exit()

def arrowStyle(line):
    if (funcString in line):
        newLine = line.replace(funcString, openBracket)
        newLine = newLine.replace(closingBracket, arrowSyntax)
        return newLine
    else:
        return line


main()
