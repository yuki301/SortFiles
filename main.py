import os

def get_dirs(root_path):#获得路径下所有文件的名字、路径，并按照(文件名,文件路径)的元组存入列表all_fself
    all_fself=[]
    for curdir,dir,file in os.walk(root_path):
        if file:
            for fname in file:
                fself=(fname,curdir+ '\\' + fname)
                all_fself.append(fself)

    return all_fself

def get_size(all_fself):#获得每个文件的大小并且以(文件大小,)的元组与此前all_fself中的元组合并
    for i in range(0,len(all_fself)):
        fself=all_fself[i]
        all_fself[i]+=(os.path.getsize(fself[1]),)

def sort_file(all_fself):#对all_self中的元组按照第三个项(文件大小)的大小进行排序
    all_fself.sort(key=lambda x:x[2],reverse=True)

def show_res(all_fself,show_num=0):#输出排序结果，show_num为0或不填则显示全部
    n=-1
    if show_num>0:
        n=show_num
    i = 0
    for fself in all_fself:
        if n==0:
            break
        i+=1
        print(f'{i}.{fself[0]}:{fself[2]/(1024*1024)}MB')
        n-=1

def get_command():#获得用户输入的指令，处理后返回需要的变量
    user_command = input("Please enter a command.Like'\033[33m[FilePath] [ShowNumber(Optional)]\033[0m'.\n"
                        ">>>")
    if '[' in user_command:
        root_path, show_num = user_command.split(sep=' ')#考虑用正则提取
        root_path = root_path.replace('[', '')
        root_path = root_path.replace(']', '')
        show_num = show_num.replace('[', '')
        show_num = show_num.replace(']', '')
        return root_path,int(show_num)
    else:
        print("Warning: Each parameter requires a '[]' declaration.")



def main():
    while True:
        try:
            root_path,show_num=get_command()
        except BaseException as e:
            print('\033[31mFailed, please input again.\033[0m')
        input('Press enter to continue.')

        try:
            all_fself=get_dirs(root_path)
            get_size(all_fself)
            sort_file(all_fself)
            show_res(all_fself,show_num)
        except BaseException as e:
            print('\033[31mFailed.\033[0m')


if __name__ == '__main__':
    main()

#TODO:
#1.可选显示文件数量 （完成）
#2.添加文件使用时间排名
#3.添加扫描进度条
#4.优化扫描排列速度
#5.有空加一个GUI
#6.指令型交互 (完成)
#7.多语言选择