'''
script for deleting all RAWs, whose JPGs don't exist (anymore)
-> lone JPGs won't be removed
'''
import sys, os, glob


'''
mandatory args:
    path:str -> path to where RAWs are to be deleted

optional args:
    raw_ext:str -> file extensions of the RAWs that are to be deleted (std "CR2")
    file_begin:str -> beginning of the image files (std "_MG_"), if given, number_begin is calculated automatically
    number_begin:int -> index where the numbering of the files begins
    number_len:int -> length of the file numbering
    respect_lowercase:bool -> set 1 if files also occure with lowercase file extension, otherwise only given file extension will be used

file_list:[] -> list containing all RAW files in the dir given by path
'''
path:str = ""

raw_ext:str = "CR2"
file_begin:str = "_MG_"
number_begin:int = len(file_begin)
number_len:int = 4
number_end:int = number_begin + number_len
respect_lowercase:bool = False

file_list:list


try:
    path = sys.argv[1]
except:
    print("no search path given")
    exit(0)

try:
    raw_ext = sys.argv[2]
except:
    pass

try:
    file_begin = sys.argv[3]
    number_begin = len(file_begin)
except:
    pass    
    
try:
    number_begin = int(sys.argv[4])
except:
    pass

try:
    number_len = int(sys.argv[5])
    number_end = number_begin + number_len
except:
    pass

try:
    respect_lowercase = bool(sys.argv[6])
except:
    pass


# let path end with "/" if not given
if path.endswith(" "):
    path = path[:-1]
if not path.endswith("/"):
    path += "/"


# read only RAWs -> only JPGs for existing RAWs are relevant
if (respect_lowercase):
    file_list = glob.glob(path + file_begin + "*." + raw_ext.upper())
    file_list.append(glob.glob(path + file_begin + "*." + raw_ext.lower()))
else:
    file_list = glob.glob(path + file_begin + "*." + raw_ext)


# get file numbering
# t_filename contains file name w/out path
for i in range(len(file_list)):
    t_filename = str(file_list[i])[-(number_begin+number_len+1+len(raw_ext)):]
    file_list[i] = t_filename[number_begin:number_end]


# iterate through file_list, remove RAWs from dir if their JPGs don't exist anymore
for file_ in file_list:
    if not ((os.path.isfile(path + file_begin + file_ + ".JPG")) or (os.path.isfile(path + file_begin + file_ + ".jpg"))):
        if (respect_lowercase):
            try:
                os.remove(path + file_begin + file_ + "." + raw_ext.upper())
            except:
                try:
                    os.remove(path + file_begin + file_ + "." + raw_ext.lower())
                except:
                    print("neither " + path + file_begin + file_ + "." + raw_ext.upper() + " nor " + path + file_begin + file_ + "." + raw_ext.lower() + " exist")
        else:
            try:
                os.remove(path + file_begin + file_ + "." + raw_ext)
            except:
                pass
