import os
print("the current work directory is: ")
currentDirectory = os.getcwd()
print(os.getcwd())
print("\n")


os.chdir(currentDirectory + "/data")
print("the current work directory is: ")
print(os.getcwd())
# os.getcwd()
data = open("testTxt.txt")
for each_line in data:
    print(each_line)
