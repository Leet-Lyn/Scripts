# 使用 gifsicle 命令来压缩 gif 文件。

# 导入模块。
import os
from PIL import Image

def move_large_palette_gifs(source_folder, target_folder):
    """
    移动拥有大于256种颜色的GIF文件到目标文件夹。

    参数:
    source_folder: 源文件夹的路径。
    target_folder: 目标文件夹的路径。
    """
    # 检查源文件夹和目标文件夹是否存在
    if not os.path.exists(source_folder):
        print(f"源文件夹 {source_folder} 不存在。")
        return
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        if filename.endswith(".gif"):
            file_path = os.path.join(source_folder, filename)
            try:
                with Image.open(file_path) as img:
                    # 检查GIF文件的颜色数量
                    if img.palette and len(img.palette.palette) // 3 > 256:
                        # 将文件移动到目标文件夹
                        os.rename(file_path, os.path.join(target_folder, filename))
                        print(f"已将 '{filename}' 移动到 '{target_folder}'。")
            except IOError:
                print(f"处理文件时出错: {filename}")

# 示例使用方法
source_folder = input("请输入源文件夹的路径: ")
target_folder = input("请输入目标文件夹的路径: ")

move_large_palette_gifs(source_folder, target_folder)


# 等待用户按下回车键后退出
input("按回车键退出...")