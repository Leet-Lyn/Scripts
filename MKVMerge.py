# 使用 mkvtoolnix 改变视频音轨，调整全局标签和章节信息。

# 导入必要的库
import os
import shutil
import subprocess

def process_mkv_files(source_folder, target_folder):
    """
    遍历源文件夹下所有的MKV文件，查找同名的M4A文件（如果存在）。
    使用mkvtoolnix将MKV文件连同对应的M4A文件重新生成，并放置在目标文件夹中。
    """
    for file in os.listdir(source_folder):
        if file.endswith(".mkv"):
            source_file_mkv = os.path.join(source_folder, file)
            source_file_m4a = os.path.join(source_folder, os.path.splitext(file)[0] + ".m4a")
            target_file = os.path.join(target_folder, file)

            command = ["mkvmerge", "-o", target_file, source_file_mkv]

            # 如果存在同名的M4A文件，添加到合并命令中
            if os.path.exists(source_file_m4a):
                command.append(source_file_m4a)

            # 执行合并命令
            subprocess.run(command)
            print(f"已处理并合并 {source_file_mkv} 和 {source_file_m4a} 到 {target_file}")

def main():
    # 向用户询问源文件夹和目标文件夹的路径
    source_folder = input("请输入源文件夹的路径：")
    target_folder = input("请输入目标文件夹的路径：")

    # 处理MKV文件
    process_mkv_files(source_folder, target_folder)

if __name__ == "__main__":
    main()

# 按下回车键退出。
input("按回车键退出...")