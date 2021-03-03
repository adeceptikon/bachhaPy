import os

a = os.listdir()
for i in a : 
    print(os.stat(i))


b  = os.scandir('E:\\')
for i in b:
    if i.is_file():
        pass
    else:
        print(os.stat(i).st_size ,  end ="\t")
        print(i.path )


