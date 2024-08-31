"""
Topic :- Files I/O

Files I/O - Python can be used to perform operations on a file.(read & Write data)

Files are two types -
a.Text Files : txt, docx, .log etc
b.Binary Files : mp4, .mov, .png, .jpeg etc

Syntax of writing File :-
Open,read & Closing File
 f = open("file_name", "mode")

 mode: r-"read", w-"write"
 file_name: sample.txt, mobile.docx
 data= f.read()
 f.close()

"""
'''
Character(mode)            Meaning
'r' Open for reading(default)
'w' open for writing, truncating the file first
'x' creates a newfile and open it for writing
'a' open for writing, appending to the end of the fille if it is exists
'b' Binary mode
't' text mode(default)
'+' open disk file for updating(reading and writing)

'''

"""  Reading a File """
# 1.Read()- Read a entire file content in a string
f = open("04_sample.txt")
line = f.read()
print(line)
f.close()

# 2.Readline - Read one line from a file at a Time(afterr printing one line it prints space(Escape sequence\n))
f = open("04_sample.txt")
line1 = f.readline()
print(line1)

line1 = f.readline()
print(line1)
f.close()

# 3.Readlines - Read all the lines of the file and return them as a list of strings
f = open("04_Sample.txt")
line1 = f.readlines()
print(line1)
f.close()