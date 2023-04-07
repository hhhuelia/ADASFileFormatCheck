import os
from collections import Counter
import tkinter as tk
import argparse
folder_name_stand=['OEM','ProjectID','VehicleType','VehicleNumber','Comment','Year','MONTH','DAY','RecordTime#CANapeID']
file_name_stand=['OEM','ProjectID','VehicleType','VehicleNumber','Comment','Year','MONTH','DAY','RecordTime#CANapeID','FileType','FileCount']
folder_count = len(folder_name_stand)
file_count = len(file_name_stand)
print (file_count)
path = 'C:\ADAS Data\Zeekr'
cur_path = 'c:\ADAS Data\Zeekr'

# 用来打印选型表单
def print_table(my_str):
   table_char = '#'
   os.system('cls')
   print (table_char * 100)
   #print ('现在的Path ='+ path)
   print (' ')
   print (' ')
   print (my_str.center(100))
   print (' ')
   print (' ')
   print (table_char * 100)
# 用来返回主页面
def callback():
    ifnext=input ('是否还有其他任务？ 1.Yes 2.No :')
    if ifnext == '1':
        print_manu()
    else:
        print('task close')
# 主菜单
def print_manu():
   print_table('1. 文件格式检查   2. 文件夹&文件改名   3. 通过TXT更改文件名   4. 云端文件名检查  5. 退出')
   option = input('请输入你的选项：')
   if option == '1':
        path_check()
   elif option == '2':
        File_format_check()    
   elif option == '3':
        txt_change()
        print('Exit')
   elif option == '4':
        cloud_filename_check()
   else:
        print('input error')
        print_manu()
# 第一级选项
def path_check():
   print_table('1.1 List Folder  1.2 Folder Check 1.3 Back ') 
   option = input('请输入你的选项：')
   if option == '1':
        my_path = input('请输入根目录名称：')
        for root, dirs, files in os.walk(my_path):
            for name in dirs:
               print(os.path.join(root, name))
        #this_input = input("需要更改文件夹名吗？  1. Yes  2. No:")
        callback()
   elif option == '2':
        File_format_check()
   elif option == '3':
        print_manu()
   else:
        print('input error')
        path_check()
# 第二级选项
def File_format_check():
    print_table('2.1 文件夹改名  2.2 文件改名  2.3 返回' )
    option = input('请输入你的选项：')
    if option == '1':
        #File_format_check()
        Folder_name_change()
        #1
        # print('下面进行文件格式检查')
    elif option == '2':
        File_name_change()
        callback()    
    elif option == '3':
        print_manu()
    else:
        print('input error')
        File_format_check()
# 第三级选项
def txt_change():
   print_table('3.1  进行文件改名   3.2 确认TXT 格式 3.3 返回')
   option = input('请输入你的选项：')
   if option == '1':
        txt_import()
   elif option == '2':
        print_txtformat()       
   elif option == '3':
        print_manu()
   else:
        txt_change()
# 第四级选型 云端文件夹命名规则检查
def cloud_filename_check():
    print_table('4.1 连接Azure Blob 4.2 列出云端文件夹 4.3 云端文件改名 4.4 返回')
    option = input('请输入你的选项：')
    if option == '1':
        print_table('请选择你要连接的Azure Blob  1. Azure EU Pangoo  2. Azure US Zeekr')
        option = input('请输入你的选项：')
    elif option == '2':
        print("以下是云端目录：")      
    elif option == '3':
        print('开始进行云端文件改名')
    else:
        print_manu()
# 2.1 文件夹名字更改函数
def folder_change(path_org,path_new):
    return 0
#3.1 通过txt 更改文件函数
def txt_import():
    os.system('cls')
    txt_path = input('请输入你需要导入的改名txt文件路径:')
    print ('需要更改的文件夹&文件名如下：')
    with open(txt_path, 'r') as file:
       my_lines = file.readlines()
       for line in my_lines:
           my_str = line.rstrip("\n")
           array = my_str.split(';')
           print (array)
    my_option = input('是否需要开始根据此列表进行改名？  ---- 1. Yes  2. No')
    if my_option == '1':
        print ('start to change file name:')
        with open(txt_path, 'r') as file:
           _lines = file.readlines()
           for line in _lines:
                my_str = line.rstrip("\n")
                array = my_str.split(';')
                File_name_change_arry(array)
                print("目录更改完成")
        print ("File name change finished")
        my_option = input('是否返回  ---- 1. Yes  2. No ：')
    elif my_option == '2':
        callback()
    else:
        print('input error')
        callback()
#3.2 TXT 格式说明信息
def print_txtformat():
   os.system('cls')
   print ('')
   print (' TXT 改名格式要求：')
   print (' 字符间通过; 分隔. 1. 文件夹名字  2. 需要更改的字段  3. 需要改成的字段')
   print (' C:\ADAS Data\Zeekr\Zeekr_PR60126_BX1E_514_R04C00-ARDAY001_2023_03_08_115137#CANape001;R04C00-ARDAY001;R04C00ARDAY001')
   print ('                                                         ')
   print (' ')
   print (' ')
   print (' ')
   ifnext=input ('是否还有其他任务？ 1.Yes 2.No :')
   if ifnext == '1':
        txt_change()
   else:
        print ('End')
# 文件名更改函数 -1
def f_change(path,file_name_org,file_name_new):
 for _filename in os.listdir(path):
    if file_name_org in _filename:
        new_filename = _filename.replace(file_name_org, file_name_new)
        os.rename(os.path.join(path, _filename), os.path.join(path, new_filename))
        print(_filename + 'Change to:' + new_filename)
    else:
        print("No file name change")
    
# 文件名更改函数 - 单个文件夹更改 
def File_name_change():
    print_table('现在开始进行文件名更改:')   
    my_change_path =  input('请输入你要更改的文件夹路径:')
    my_change_filename_org = input('请输入你要更改的文件的字段:')
    my_change_filename_new = input('请输入你要更改为的文件的字段:')
    f_change(my_change_path,my_change_filename_org,my_change_filename_new)
    ifnext=input ('是否还有其他任务？ 1.Yes 2.No')
    if ifnext == '1':
        print_manu()
    else:
        print('task close')
        print_manu()
# 文件名更改函数 - 读取txt 进行遍历更改
def File_name_change_arry(arry):
    my_change_path =  arry[0]
    my_change_filename_org = arry[1]
    my_change_filename_new = arry[2]
    f_change(my_change_path,my_change_filename_org,my_change_filename_new)

def Folder_name_change():
    print_table('现在开始进行文件夹名称更改:')   
    for root, dirs, files in os.walk(cur_path):
            for name in dirs:
               print(os.path.join(root, name))
    #my_change_path =  input('请输入你要更改的文件夹名字:')
    my_change_folder_org = input('请输入你要更改的文件夹里错误的字段:')
    my_change_folder_new = input('请输入你要更改为的文件夹正确的字段:')
    #f_change(my_change_path,my_change_filename_org,my_change_filename_new)
    ifnext=input ('是否还有其他任务？ 1.Yes 2.No')
    if ifnext == '1':
        print_manu()
    else:
        print('task close')
        print_manu()


if __name__ == '__main__':
    print_manu()
    
