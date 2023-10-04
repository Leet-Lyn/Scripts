# 用 yt-dlp 下载视频。

# 导入 subprocess 模块。
import subprocess

def download_video():
    # 获取用户输入，确定下载类型
    link_type = input("你想下载单个链接还是列表文件中的链接？（输入 1 或 2）\n1. 单个链接\n2. 列表文件中的链接（默认）\n")
    
    if link_type == "1":  # 如果用户选择下载单个链接
        link = input("请输入要下载的链接：")  # 获取要下载的链接
        cookies = input("是否需要引入 cookies 文件？（输入 y 或 n）\n")  # 确定是否需要引入 cookies 文件
        
        if cookies == "y":  # 如果需要引入 cookies 文件
            cookie_file = input("请输入 cookies 文件的位置（按回车键使用默认位置 Cookies.txt）：") or "d:\ProApps\Youtube-dl\Cookies.txt"  # 获取 cookies 文件的位置
            proxy = input("是否需要代理？（输入 y 或 n）\n")  # 确定是否需要代理
            
            if proxy == "y":  # 如果需要代理
                proxy_address = input("请输入代理地址（按回车键使用默认地址 http://127.0.0.1:10809）：") or "127.0.0.1:10809"  # 获取代理地址
                subprocess.run(["d:\ProApps\Youtube-dl\yt-dlp.exe", "--cookies", cookie_file, "--proxy", proxy_address, link])  # 使用 yt-dlp 下载视频，带有 cookies 和代理
            else:
                subprocess.run(["d:\ProApps\Youtube-dl\yt-dlp.exe", "--cookies", cookie_file, link])  # 使用 yt-dlp 下载视频，只带有 cookies
                
        else:  # 如果不需要引入 cookies 文件
            proxy = input("是否需要代理？（输入 y 或 n）\n")  # 确定是否需要代理
            
            if proxy == "y":  # 如果需要代理
                proxy_address = input("请输入代理地址（按回车键使用默认地址 http://127.0.0.1:10809）：") or "127.0.0.1:10809"  # 获取代理地址
                subprocess.run(["d:\ProApps\Youtube-dl\yt-dlp.exe", "--proxy", proxy_address, link])  # 使用 yt-dlp 下载视频，只带有代理
            else:
                subprocess.run(["d:\ProApps\Youtube-dl\yt-dlp.exe", link])  # 使用 yt-dlp 下载视频，不带有任何额外参数
                
    elif link_type == "2":  # 如果用户选择从列表文件中下载链接
        list_file = input("请输入列表文件的位置（按回车键使用默认位置 Lists.txt）：") or "d:\ProApps\Youtube-dl\Lists.txt"  # 获取列表文件的位置
        cookies = input("是否需要引入 cookies 文件？（输入 y 或 n）\n")  # 确定是否需要引入 cookies 文件
        
        if cookies == "y":  # 如果需要引入 cookies 文件
            cookie_file = input("请输入 cookies 文件的位置（按回车键使用默认位置 Cookies.txt）：") or "d:\ProApps\Youtube-dl\Cookies.txt"  # 获取 cookies 文件的位置
            proxy = input("是否需要代理？（输入 y 或 n）\n")  # 确定是否需要代理
            
            if proxy == "y":  # 如果需要代理
                proxy_address = input("请输入代理地址（按回车键使用默认地址 http://127.0.0.1:10809）：") or "127.0.0.1:10809"  # 获取代理地址
                subprocess.run(["d:\ProApps\Youtube-dl\yt-dlp.exe", "--cookies", cookie_file, "--proxy", proxy_address, "-a", "-i", "--batch-file=" + list_file])  # 使用 yt-dlp 下载视频，带有 cookies 和代理，并从列表文件中获取链接
                
            else:
                subprocess.run(["d:\ProApps\Youtube-dl\yt-dlp.exe", "--cookies", cookie_file, "-a", "-i", "--batch-file=" + list_file])  # 使用 yt-dlp 下载视频，只带有 cookies，并从列表文件中获取链接
                
        else:  # 如果不需要引入 cookies 文件
            proxy = input("是否需要代理？（输入 y 或 n）\n")  # 确定是否需要代理
            
            if proxy == "y":  # 如果需要代理
                proxy_address = input("请输入代理地址（按回车键使用默认地址 http://127.0.0.1:10809）：") or "127.0.0.1:10809"  # 获取代理地址
                subprocess.run(["d:\ProApps\Youtube-dl\yt-dlp.exe", "--proxy", proxy_address, "-a", "-i", "--batch-file=" + list_file])  # 使用 yt-dlp 下载视频，只带有代理，并从列表文件中获取链接
                
            else:
                subprocess.run(["d:\ProApps\Youtube-dl\yt-dlp.exe", "-a", "-i", "--batch-file=" + list_file])  # 使用 yt-dlp 下载视频，不带有任何额外参数，并从列表文件中获取链接
                
    else:  # 如果用户输入的既不是 "1" 也不是 "2"
        print("无效的输入，请重新运行脚本。")  # 提示用户输入无效，并要求重新运行脚本

download_video()  # 运行 download_video 函数


# 按下回车键退出。
input("按回车键退出...")