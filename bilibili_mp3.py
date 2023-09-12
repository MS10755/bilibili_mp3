import sys
import os
import re

def get_mp4_file_name():
    files = os.listdir(os.getcwd())
    for file in files:
        match = re.search(r'([\s\S]+).mp4', file)
        if match is not None:
            name = match.group(1)
            return name


def download(url):
    os.system('you-get -k -F dash-flv480 --no-caption %s' % url)
    name = get_mp4_file_name()
    cmd = 'ffmpeg -i "%s.mp4" -vn "%s.mp3"' % (name, name)
    os.system(cmd)
    os.remove("%s.mp4" % name)


if __name__ == '__main__':
    while True:
        url = input("请输入下载地址：")
        download(url)


# 需要you-get和ffmpeg的支持
# 运行pip install you-get 安装you-get
# 下载ffmpeg并设置环境变量路径