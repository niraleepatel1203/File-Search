'''
abcd
ICS 32
Niralee Patel 43461165
Akshita Nathani 93016780
'''
from pathlib import Path
import shutil 

def D_or_R():
    '''
    this function gets an input (just "D" or "R") and makes path objects. It then returns a tuple of the input and the path object.
    '''
    path_name = input()
    while (path_name[0] != "R" and path_name[0] != "D") or (len(path_name) < 3) or Path(path_name[2:]).exists() == False:
        print("ERROR")
        path_name = input()
    p = Path(path_name[2:])
    return (path_name, p)

def path_for_D(path_name,p):
    '''
    This function iterates through the path and appends only files into a list, then returns that list.
    '''
    try:
        path_list = []
        if path_name[0].upper() == "D":
            for i in p.iterdir():
                if i.is_file() == True:
                    path_list.append(i)
        return path_list
                    
    except:
        print("ERROR")

def path_for_R(p,path_list=[]):
    '''
    This function uses recursion to return directories and all subdirectories in a list.
    '''
    for i in p.iterdir():
        if i.is_file():
            path_list.append(i)
        elif i.is_dir():
            path_list + (path_for_R(i))
    return path_list

def ANET():
    '''
    This function gets the second input and returns it.
    '''
    file_ext = input("")
    if file_ext[0] == "A":
        return file_ext
    while (file_ext[0] != "N" and file_ext[0] != "E" and file_ext[0] != "T" and file_ext[0] != "<" and file_ext[0] != ">") or (len(file_ext)< 3):
        print("ERROR")
        file_ext = input("")
    return file_ext

def path_for_A(path_list:list):
    '''
    This function returns a list of all interesting files.
    '''
    return path_list

def path_for_N(path_list:list,file_name):
    '''
    This function makes a list of files of the name(input) entered by the user and returns it.
    '''
    return_list = []
    for i in path_list:
        if i.name == file_name:
            return_list.append(i)
    return return_list

def path_for_E(path_list:list, file_ext):
    '''
    This function makes a list of all files ending with a particular extension and returns it.
    '''
    return_list = []
    if "." not in file_ext:
        file_ext = file_ext.split()
        file_ext.insert(0, ".")
        file_ext= "".join(file_ext)
    for i in path_list:
        if i.suffix == file_ext:
            return_list.append(i)
    return return_list

        
def path_for_T(path_list:list,text):
    '''
    This function makes a list of all files containing a particular word(s) and returns it.
    '''
    return_list = []
    for i in path_list:
        counter = 0 
        try:
            if i.is_file() == True:
                file = open(str(i),'r')
                for line in file:
                    if text in line:
                        counter +=1
                        if counter <=1:
                            return_list.append(i)
                            
        except:
            pass
        file.close()
    return return_list


def path_for_less_than(path_list:list, size):
    '''
    This function makes a list of all files that are less than the number of bytes entered by the user and returns it.
    '''
    return_list = []
    for i in path_list:
        if i.stat().st_size < int(size):
            return_list.append(i)
    return return_list

        
def path_for_more_than(path_list:list, size):
    '''
    This function makes a list of all files that are less than the number of bytes entered by the user and returns it.
    '''
    return_list = []
    for i in path_list:
        if i.stat().st_size > int(size):
            return_list.append(i)
    return return_list

def evaluate_ANET()->list:
    '''
    This function runs D_or_R and gets the path_name and path object. After that, it calls ANET(), which gets an input.
    According to the command, we send call the appropriate function.
    '''
    path_name, p = D_or_R()
    if path_name[0] == "D":
        path_list = path_for_D(path_name,p)
        print_lexi(path_list)
    elif path_name[0] == "R":
        path_list = path_for_R(p)
        print_lexi(path_list)
    command = ANET()       
    if command[0] == "A":
        return_list = path_for_A(path_list)
        sortL = print_lexi(return_list)
    elif command[0] == "N":
        return_list = path_for_N(path_list,command[2:])
        sortL = print_lexi(return_list)
    elif command[0] == "E":
        return_list = path_for_E(path_list,command[2:])
        sortL = print_lexi(return_list)
    elif command[0] == "T":
        return_list = path_for_T(path_list,command[2:])
        sortL = print_lexi(return_list)
    elif command[0] == "<":
        return_list = path_for_less_than(path_list,command[2:])
        sortL = print_lexi(return_list)
    elif command[0] == ">":
        return_list = path_for_more_than(path_list,command[2:])
        sortL = print_lexi(return_list)
    return sortL
        
def FDT()->str:
    '''
    This function gets the third input (only "F", "D", "T").
    '''
    fdt = input('')
    while fdt != "F" and fdt != "D" and fdt != "T":
        print("ERROR")
        fdt = input('')
    return fdt

def path_for_F(sortL: list):
    '''
    This function prints the first line of the files in the list of interesting files.
    '''
    for i in sortL:
        i = i[1]
        try:
            if i.is_file() == True:
                file = open(str(i),'r')
                print(file.readline()[:-1])
        except: 
            print("NOT TEXT")
    
def path_for_Dup(sortL: list):
    '''
    This function creates duplicates of the interesting files.
    '''
    for i in sortL:
        i = i[1]
        dup_path = str(i) + ".dup"
        shutil.copy(i, dup_path)
        
def path_for_Touch(sortL:list):
    '''
    This function modifies the time the interesting files were last touched.
    '''
    for i in sortL:
        i = i[1]
        i.touch()

def evaluate_FDT(sortL:list):
    '''
    This functions calls the appropriate functions according to the third input ("F", "D", or "T")
    '''
    command = FDT()
    if command[0] == "F":
        path_for_F(sortL)
    elif command[0] == "D":
        path_for_Dup(sortL)
    elif command[0] == "T":
        path_for_Touch(sortL)

def print_lexi(L:list):
    '''
    This function prints the files lexicographically and returns a sorted list
    '''
    paths = []
    for i in L:
        paths.append((str(i).count('/'),i))
    for j in sorted(paths):
        print(j[1])
    return sorted(paths)
    
if __name__ == "__main__":
    sortL = evaluate_ANET()
    evaluate_FDT(sortL)

