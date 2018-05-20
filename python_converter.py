#   purpose         : Program to convert python 2.7 program in python 3.6
#   made by         : rakesh kumar
#   License         : MIT

""" function to convert major 2.7 function into 3.6 """
def converter():
    file = open("ZipCracker.py",'r')
    file1 = open("newzip.py",'w')
    for line in file:
        # print(line)
        if 'print' in line:
            line1 = line.replace('print','print(' )
            line2 = line1.replace('\n',' ')
            newline = line2+ ' ) \n'
            # print(newline)
            file1.write(newline)
        else:
            if 'raw_input' in line:
                line1 = line.replace('raw_input','input')
                file1.write(line1)
            else:
                if 'xrange' in line:
                    line1 = line.replace('xrange','range')
                else:    
                    file1.write(line)

    file.close()
    file1.close()
    print("Conversion Complete....Check your file")

""" call user defined function """
if __name__ == '__main__':
    converter()