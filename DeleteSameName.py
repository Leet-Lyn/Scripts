# 删除同名文件。

# 导入 os 模块。
import os

def remove_duplicates(source_folder, target_folder):
    """
    如果源文件夹中的文件在目标文件夹中存在同名文件，则删除源文件夹中的文件。
    """
    # 检查源文件夹和目标文件夹是否存在
    if not os.path.exists(source_folder):
        print(f"源文件夹 '{source_folder}' 不存在。")
        return
    if not os.path.exists(target_folder):
        print(f"目标文件夹 '{target_folder}' 不存在。")
        return

    # 获取目标文件夹中的文件列表
    target_files = set(os.listdir(target_folder))

    # 遍历源文件夹中的文件
    for file in os.listdir(source_folder):
        # 检查文件是否在目标文件夹中存在
        if file in target_files:
            # 构建源文件夹中文件的完整路径
            file_path = os.path.join(source_folder, file)
            # 删除文件
            os.remove(file_path)
            print(f"已从源文件夹中移除 '{file}'。")

if __name__ == "__main__":
    # 请求用户输入源文件夹和目标文件夹的路径
    source_folder = input("请输入源文件夹路径: ")
    target_folder = input("请输入目标文件夹路径: ")

    # 执行函数
    remove_duplicates(source_folder, target_folder)

# 按下回车键退出。
input("按回车键退出...")