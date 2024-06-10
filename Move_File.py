import os 
import shutil
from_dir = "C:/Users/Hp/Downloads"
to_dir = "C:/Users/Hp/Downloads/Document_files"
listOfFiles=os.listdir(from_dir)
print(listOfFiles)
for i in listOfFiles:
    name,extension=os.path.splitext(i)
    print(extension)
    if extension=="":
        continue
    
    if extension in  [ '.txt', '.doc', '.docx', '.pdf']:
        path1=from_dir+"/"+i
        path2=to_dir+"/"+"Documents_Folder"
        path3=to_dir+"/"+"Documents_Folder"+"/"+i

        if os.path.exists(path2):
            print(f"moving {i}... ")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print(f"moving {i}... ")
            shutil.move(path1,path3)    