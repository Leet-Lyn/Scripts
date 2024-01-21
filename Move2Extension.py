# 将源文件下所有文件移动到目标文件夹下“以文件扩展名为文件名”的子文件夹中。 

# 导入 shutil 和 os 模块。
import os
import shutil

def move_files(source_folder, target_folder):
    # 确保目标文件夹存在
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        # 跳过文件夹
        if os.path.isdir(file_path):
            continue

        # 获取文件扩展名，并创建目标子文件夹
        extension = os.path.splitext(filename)[1].lstrip('.').lower()
        if extension == '':
            extension = 'no_extension'
        extension_folder = os.path.join(target_folder, extension)

        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)

        # 移动文件
        shutil.move(file_path, os.path.join(extension_folder, filename))

def main():
    # 询问用户输入
    source_folder = input("请输入源文件夹的路径: ")
    target_folder = input("请输入目标文件夹的路径: ")

    move_files(source_folder, target_folder)
    print("文件移动完成。")

if __name__ == "__main__":
    main()
    
# 按下回车键退出。
input("按回车键退出...")