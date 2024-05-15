#create a new text file
#f = open("PythonNotes.txt","x")

#Write to the file
#rule 1 use open function
#f = open("PythonNotes.txt","w")
#rule 2 use write function
#f.write("Session topic: File Handling")
#rule 3 close the file
#f.close()
# w to overwrite and a to append
"""f = open("PythonNotes.txt","w")
f.write("Session Topic: File Handling")
f.close()"""
#adding second line to file
#--> Python Programming
"""f = open("PythonNotes.txt","a")
f.write("Python Programming")
f.close()"""



#read file contents
#rule 1 open function with r
#rule 2 f.read method() inside print
"""f = open("PythonNotes.txt","r")
print(f.read())"""

class FileHandler:
    def __init__(self) -> None:
        pass

    #1st function ; create a new file
    def filecreator(self):
        filename = str(input("Enter name of file you want to create\n"))
        f = open("FileName","x")
        print ("File has been created.")

    #2nd function write to file
    def filewriter(self):
        filename = str(input("Enter name of file you want to write"))
        fcontent = str(input("Insert text below...\n"))
        f = open(filename,"w")
        f.write(fcontent)
        f.close()
        print("You have written to this file.")

    #3rd function read file content
    def filereader(self):
        filename = str(input("Enter name of file you want to read"))
        f = open(filename,"r")
        print(f.read())

    #object initialization
fileobj1 = FileHandler()

#USE OBJECT
fileobj1.filecreator()
fileobj1.filereader()
fileobj1.filewriter()

"""GITHUB CLONING
1. GOT CLONE LINK
2. GIT STATUS
3. IF FATAL ERROR APPEARS / LS TO SEE CONTENTS
CD CEITPYTHON2024
4. GIT ADD
5. GIT COMMIT -M ADDING NEW FILE
6. #GIT CONFIG -- EDIT
7. #: QA
8. 

"""