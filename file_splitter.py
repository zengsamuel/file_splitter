import sys
import os

BUF_SIZE = 1000

def split(input_filename, size):
    statinfo = os.stat(input_filename)
    
    with open(input_filename, 'rb') as input_file:
        i = 0
        output = "{}.{}".format(input_filename, i)
        len = 0
        output_file = open(output, 'wb')
        while len < statinfo.st_size:
            data = input_file.read(BUF_SIZE)
            output_file.write(data)
            len += BUF_SIZE
        
            if len % size == 0:
                output_file.close()
                i += 1
                output = "{}.{}".format(input_filename, i)
                output_file = open(output, 'wb')

        output_file.close()

def merge(input_filename_prefix, output_filename):
    i = 0
    input_filename = "{}.{}".format(input_filename_prefix, i)
    with open(output_filename, 'wb') as output_file:
        while os.path.isfile(input_filename):
            with open(input_filename, 'rb') as input_file:
                while True:
                    data = input_file.read(BUF_SIZE)
                    if not data:
                        break
                    output_file.write(data)

            i += 1
            input_filename = "{}.{}".format(input_filename_prefix, i)
    
"""
   python file_splitter split inputfile_name file_size
   python file_splitter merge inputfile_prefix outputfile_name
   for example:
     split:  python file_splitter split a.avi 1000000000
     merge:  python file_splitter merge a.avi a.avi
"""
if sys.argv[1] == 'split': 
    split(sys.argv[2], int(sys.argv[3]))
elif sys.argv[1] == 'merge':
    merge(sys.argv[2], sys.argv[3])
