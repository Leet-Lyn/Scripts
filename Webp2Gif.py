# 批量将 Webp 文件转成 Gif 文件。

# 导入 os 模块。
from PIL import Image
import os

def convert_webp_to_gif(input_folder, output_folder):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)
    
    # 遍历输入文件夹中的WebP文件
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".webp"):
            filepath = os.path.join(input_folder, filename)
            im = Image.open(filepath)
            im.info.pop("background", None)  # 移除背景信息
            im.save(os.path.join(output_folder, filename.replace(".webp", ".gif")), "gif", save_all=True)

# 指定输入和输出文件夹路径
input_folder = input("请输入源文件夹位置（按回车键使用默认地址：t:\Temps\）：") or "t:\\Temps\\" 
output_folder = input("请输入目标文件夹位置（按回车键使用默认地址：t:\XXX\）：") or "t:\\XXX\\" 

# 执行批量转换
convert_webp_to_gif(input_folder, output_folder)


# 按下回车键退出。
input("按回车键退出...")
