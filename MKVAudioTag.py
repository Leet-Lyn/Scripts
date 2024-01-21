# 使用 mkvtoolnix 改变视频音轨，调整全局标签和章节信息。

# 导入必要的库
import os
import shutil
import subprocess

def adjust_audio_track(source_file, language_option):
    """
    调整音轨的语言和轨道名称。
    """
    track_name, language_code = "", ""
    if language_option == "0":
        track_name, language_code = "", "und"
    elif language_option == "1":
        track_name, language_code = "英语", "en"
    elif language_option == "2":
        track_name, language_code = "日语", "jp"
    elif language_option == "3":
        track_name, language_code = "国语", "zh-cmn"
    elif language_option == "4":
        track_name, language_code = "粤语", "zh-yue"

    command = [
        "mkvpropedit",
        source_file,
        "--edit",
        "track:a1",
        "--set",
        f"name={track_name}",
        "--set",
        f"language={language_code}"
    ]

    subprocess.run(command)

def convert_to_mkv(source_file, target_file):
    """
    将视频文件转换为MKV格式。
    """
    command = ["mkvmerge", "-o", target_file, source_file]
    subprocess.run(command)

def process_video_files(source_folder, target_folder, adjust_audio, remove_tags_chapters):
    """
    处理源文件夹中的所有支持的视频文件，并转换为MKV格式。记录任何处理错误。
    """
    error_files = []
    supported_extensions = [".mkv", ".avi", ".rm", ".rmvb", ".mpg", ".mpeg", ".wmv", ".asf", ".mov", ".mp4"]

    for file in os.listdir(source_folder):
        try:
            if any(file.endswith(ext) for ext in supported_extensions):
                source_file = os.path.join(source_folder, file)
                target_file_name = os.path.splitext(file)[0] + ".mkv"
                target_file = os.path.join(target_folder, target_file_name)

                if not file.endswith(".mkv"):
                    convert_to_mkv(source_file, target_file)
                else:
                    shutil.copy(source_file, target_file)

                if adjust_audio:
                    adjust_audio_track(target_file, adjust_audio)

                if remove_tags_chapters:
                    command_remove_tags = ["mkvpropedit", target_file, "--tags", "global:"]
                    command_remove_chapters = ["mkvpropedit", target_file, "--chapters", ""]
                    subprocess.run(command_remove_tags)
                    subprocess.run(command_remove_chapters)

                print(f"已处理 {source_file} 并转换/移动到 {target_file}")

        except Exception as e:
            print(f"处理文件 {source_file} 时出错: {e}")
            error_files.append(source_file)

    return error_files

def main():
    source_folder = input("请输入源文件夹的路径：")
    target_folder = input("请输入目标文件夹的路径：")
    adjust_audio = input("是否需要调整声音音轨语言？（是请输入1，否请输入0）：")
    if adjust_audio == "1":
        print("请选择音轨语言选项：")
        print("0. 未定")
        print("1. 英语")
        print("2. 日语")
        print("3. 国语")
        print("4. 粤语")
        adjust_audio = input("请输入选择的编号：")
    else:
        adjust_audio = None

    remove_tags_chapters = input("是否要移除全局标签和章节信息？（是请输入1，否请输入0）：") == "1"
    
    error_files = process_video_files(source_folder, target_folder, adjust_audio, remove_tags_chapters)

    if error_files:
        print("以下文件在处理过程中出错：")
        for error_file in error_files:
            print(error_file)

if __name__ == "__main__":
    main()

# 按下回车键退出。
input("按回车键退出...")