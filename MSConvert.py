# 将文件夹下所有的 doc、xsl、ppt 文件转为 docx、xslx、pptx 文件。

# 导入 os 模块与 comtypes.client 模块。
import os
import comtypes.client

# 询问用户源文件夹路径。
source_folder = input("请输入源文件夹路径（按回车则为“T:\Temps\”）：")
if source_folder == "":
    source_folder = "T:\\Temps\\"

# 询问用户目标文件夹路径。
target_folder = input("请输入目标文件夹路径（按回车则为“T:\XXX\”）：")
if target_folder == "":
    target_folder = "T:\\XXX\\"

def convert_files(source_folder, target_folder):
    for file_name in os.listdir(source_folder):  
    # 遍历源文件夹中的所有文件
        full_file_name = os.path.join(source_folder, file_name)  
        # 获取文件的完整路径
        if os.path.splitext(file_name)[1].lower() == '.doc':  
        # 检查文件是否为 doc 文件
            new_file_name = os.path.splitext(file_name)[0].replace("[", "(").replace("]", ")") + '.docx'  
            # 将文件名中的“[”替换为“（”，将“]”替换为“）”，并将扩展名改为“.docx”
            full_new_file_name = os.path.join(target_folder, new_file_name)  
            # 获取目标文件的完整路径
            word = comtypes.client.CreateObject('Word.Application')  
            # 创建 Word 应用程序对象
            doc = word.Documents.Open(full_file_name)  
            # 打开源文件
            doc.SaveAs(full_new_file_name, FileFormat=16)  
            # 将文件另存为 docx 格式
            doc.Close()  
            # 关闭源文件
            word.Quit()  
            # 关闭 Word 应用程序对象
        elif os.path.splitext(file_name)[1].lower() == '.xls':  
        # 检查文件是否为 xls 文件
            new_file_name = os.path.splitext(file_name)[0].replace("[", "(").replace("]", ")") + '.xlsx'  
            # 将文件名中的“[”替换为“（”，将“]”替换为“）”，并将扩展名改为“.xlsx”
            full_new_file_name = os.path.join(target_folder, new_file_name)  
            # 获取目标文件的完整路径
            excel = comtypes.client.CreateObject('Excel.Application')  
            # 创建 Excel 应用程序对象
            wb = excel.Workbooks.Open(full_file_name)  
            # 打开源文件
            wb.SaveAs(full_new_file_name, FileFormat=51)  
            # 将文件另存为 xlsx 格式
            wb.Close()  
            # 关闭源文件
            excel.Quit()  
            # 关闭 Excel 应用程序对象
        elif os.path.splitext(file_name)[1].lower() == '.xls':  
        # 检查文件是否为 ppt 文件
            new_file_name = os.path.splitext(file_name)[0].replace("[", "(").replace("]", ")") + '.pptx'  
            # 将文件名中的“[”替换为“（”，将“]”替换为“）”，并将扩展名改为“.pptx”
            full_new_file_name = os.path.join(target_folder, new_file_name)  
            # 获取目标文件的完整路径
            powerpoint = comtypes.client.CreateObject('Powerpoint.Application')  
            # 创建 Powerpoint 应用程序对象
            ppt = powerpoint.Presentations.Open(full_file_name)  
            # 打开源文件
            ppt.SaveAs(full_new_file_name, FileFormat=24)  
            # 将文件另存为 pptx 格式
            ppt.Close()  
            # 关闭源文件
            powerpoint.Quit()  
            # 关闭 Powerpoint 应用程序对象

# 调用函数将源文件夹中的所有文件转换并保存到目标文件夹中
convert_files(source_folder, target_folder)

def rename_files(target_folder):
    for file_name in os.listdir(target_folder):  
    # 遍历文件夹中的所有文件
        old_file_path = os.path.join(target_folder, file_name)  
        # 获取旧文件路径
        new_file_name = file_name.replace("(", "[").replace(")", "]")  
        # 将文件名中的“(”替换为“[”，将“)”替换为“]”
        new_file_path = os.path.join(target_folder, new_file_name)  
        # 获取新文件路径
        os.rename(old_file_path, new_file_path)  
        # 重命名文件

rename_files(target_folder)  # 调用重命名函数

# 按下回车键退出。
input("按回车键退出...")