# Basic Input and Output with files

# Location of test files
#"C:\Users\Deodat\Desktop\New folder\text.txt"

# how to open the file
myfile = open(r"C:\Users\Deodat\Desktop\New folder\text.txt")
print(myfile.read())
# You may need to reset the cursor
myfile.seek(0)
print(myfile.read())

test=myfile.readlines()
print("this is the readlines section:" + str(test))

