# File Input/Output

# 1) Open, Read and Close File
# we have to open a file before reading or writing

"""
# SYNTAX =>
1) f = open("file_name", "mode")
# here file_name means name of the file with its extension
#  and mode is r : read mode, w : Write mode
# By default the mode is always read mode

2) data = f.read()
3) f.close()
"""
"""
f= open("Python-7\demo.txt", "r")
# data = f.read() # Reads the entire file
#data = f.read(15) # Reads the first 15 characters of the file
line1 = f.readline() # Reads the first line of the file
# print(data)
print(line1)
f.close()
"""
"""
# 2) Write mode

f= open("Python-7\demo.txt", "w")
f.write("I'll start learning DSA") # W mode overites the whole previously written file
f.close()
"""

"""
# 3) Append Mode

f= open("Python-7\demo.txt", "a") # if this file does not exit in w or a mode then python will create a new file
f.write("\nwith python") # W mode add the new data at the bottom of the file
f.close()
"""

"""
NOTE :->
 The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream is positioned at the beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing. The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not exist, otherwise it is truncated.  The stream is positioned at the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist. The stream is positioned at the end of the file.  Subsequent writes to the file will always end up at the then current end of file, irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not exist.  The stream is positioned at the end of the file. Subsequent writes to the file will always end up at the then current end of file, irrespective of any intervening fseek(3) or similar.
"""

"""
# with syntax

with open("Python-7\demo.txt", "r") as f:
    data = f.read()
    print(data)
#NOTE in with syntax file is automatically closed
"""

# 4) Deleting a file
# A file is deletedusing OS module
# Module(like a code library) is a file written by another programmer that generally has a function we can use

import os

os.remove("Python-7\sample.txt")