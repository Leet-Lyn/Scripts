# 将源文件下所有文件移动到目标文件夹下“动图”与“非动图”的子文件夹中。 

# 导入 os 模块。
import os
from PIL import Image

def is_animated_webp(file_path):
    """
    检查一个 WEBP 图片是否为动态图像。
    """
    try:
        image = Image.open(file_path)
        return getattr(image, "is_animated", False)
    except IOError:
        return False

def move_webp_images(source_folder, target_folder):
    """
    将 WEBP 图片从源文件夹移动到目标文件夹，
    并根据图片是动态的还是非动态的进行分类。
    """
    # 在目标文件夹中创建子文件夹用于存放动态和非动态图片
    animated_folder = os.path.join(target_folder, "animated")
    non_animated_folder = os.path.join(target_folder, "non_animated")
    os.makedirs(animated_folder, exist_ok=True)
    os.makedirs(non_animated_folder, exist_ok=True)

    # 遍历源文件夹中的所有 WEBP 文件
    for file in os.listdir(source_folder):
        if file.lower().endswith('.webp'):
            file_path = os.path.join(source_folder, file)
            
            # 检查图片是否为动态图像，并将其移动到相应的文件夹
            if is_animated_webp(file_path):
                os.rename(file_path, os.path.join(animated_folder, file))
            else:
                os.rename(file_path, os.path.join(non_animated_folder, file))

if __name__ == "__main__":
    # 询问用户输入源文件夹和目标文件夹的路径
    source_folder = input("请输入源文件夹的路径: ")
    target_folder = input("请输入目标文件夹的路径: ")

    move_webp_images(source_folder, target_folder)
    print("WEBP 图片已成功移动。")
    
# 按下回车键退出。
input("按回车键退出...")