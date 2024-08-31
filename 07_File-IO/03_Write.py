'''
Writing a File

# 1.write() -opens a file for writing, if the file doesn't exists, it creates a new file.if the fille already exits, it truncates(i.e,Removes the content) the File and overwrites in it
'''
# word ="Java is Programming Language\nPython is the Beginer frienndly"
# f = open("02_Demo.txt","w")
# f.write(word)
# print(word)
# f.close()

'''
# 2.writelines() - writes a list of strings
'''
# word ="""Hiii Hello Everybody
# Hacking is best
# ohk lets see
# """
# f = open("02_Demo.txt","w")
# f.writelines(word)
# print(word)
# f.close()

"""
# 3.Append() - opens a file for appending, if the file doesn't exists, it creates a new file.if the file already exits, it adds the new content to the end of the file without removing existing content
"""
# word = "\nWeb Deveopment"
# f = open("02_Demo.txt","a")
# f.write(word)
# print(word)
# f.close()

'''
#4.r+ , w+, a+
'''
# 1.r+ - it is wil not truncated(cursor start from  beginning)
# f = open("02_Demo.txt","r+")
# print(f.read())
# f.write("CodeWithHarry")
# f.close()

# 2.w+ - it is truncated(it overwrites from beginng and cursor start from  beginning)
f = open("02_Demo.txt","w+")
print(f.read())
f.write("Codewithpython")
f.close()

# 3.a+ - it is wil not truncated(Cursor Starts From End to append at end)
f = open("02_Demo.txt","a+")
print(f.read())
f.write("Codewithpython")
f.close()