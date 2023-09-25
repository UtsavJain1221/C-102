import os
import shutil

#print(dir(os))

#os.getcwd()
##os.mkdir("102")

#os.listdir()

path = "C:/Users/Test"

source = "feather.jfif"

destination = "C:/Users/Test/C-102/102/copyfeature.jfif"

shutil.move(source, destination)


dest =shutil.copy(source, destination)

print("After copying file:")



print(os.listdir(path))

