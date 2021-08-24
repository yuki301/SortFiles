import os

def get_dirs(root_path):
    all_fself=[]
    for curdir,dir,file in os.walk(root_path):
        if file:
            for fname in file:
                fself=(fname,curdir+ '\\' + fname)
                all_fself.append(fself)

    return all_fself

def get_size(all_fself):
    for i in range(0,len(all_fself)):
        fself=all_fself[i]
        all_fself[i]+=(os.path.getsize(fself[1]),)

def sort_file(all_fself):
    all_fself.sort(key=lambda x:x[2],reverse=True)

def show_res(all_fself):
    i=0
    for fself in all_fself:
        i+=1
        print(f'{i}.{fself[0]}:{fself[2]/(1024*1024)}MB')

if __name__ == '__main__':
    while True:
        root_path=input('Please enter the path of the file you want to scan:')
        all_fself=get_dirs(root_path)
        get_size(all_fself)
        sort_file(all_fself)
        show_res(all_fself)
        input('Press enter to continue.')
