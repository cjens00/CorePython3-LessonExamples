import sys

# e.g. 'utf-8'
default_encoding = sys.getdefaultencoding()
print("This system's default encoding is: %s" % default_encoding)


def FileWriteText(filename):
    # mode: read, write, append : r/w/a
    # combine with selector: t or b, text or binary
    f = open(filename, mode='wt', encoding='utf-8')
    f.write('What are the roots that clutch, ')
    f.write('what branches grow\n')
    f.write('Out of this stony rubbish? ')
    f.close()


def FileReadText(filename):
    g = open(filename, mode='rt', encoding='utf-8')
    print(g.read(32))  # Reads exactly 32 characters (not bytes, as we are in text mode)
    print(g.read())  # Reads all remaining data from file
    g.seek(0)  # Even in text mode, seek(0) and seek(tell()) are valid
    print(g.readline())
    g.seek(0)
    print(g.readlines())  # Read all lines into a list
    g.close()



if __name__ == "__main__":
    FileWriteText('wasteland.txt')
    FileReadText('wasteland.txt')
