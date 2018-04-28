'''
script for deleting all RAWs (.CR2), whose JPGs don't exist (anymore)
'''
import sys, os

path:str
file_list:[]

try:
    path = sys.argv[1]
except:
    print("kein Pfad zum Suchen angegeben")
    exit(0)


# let path end with "/"
if path.endswith(" "):
    path = path[:-1]
if not path.endswith("/"):
    path += "/"


# read file names into file_list
file_list = os.listdir(path)

# get file numbering
for i in range(len(file_list)):
    file_list[i] = file_list[i][4:8]

# sort
file_list.sort()

# iterate through file_list backwards, remove RAWs from dir if their JPGs don't exist anymore
for i in range(len(file_list)-1, -1, -1):
    if (i > 0) and (file_list[i] != file_list[i-1]) and (file_list[i] != file_list[i+1]):
        try:
            os.remove(path + "_MG_" + file_list[i] + ".CR2")
        except Exception as e:
            print(e)
