import requests
from bs4 import BeautifulSoup
url = "http://ip.tool.chinaz.com/"
if __name__=='__main__':
    print("-"*50)
    print("服务器地址查询器".center(42, '+'))
    print("作者：HUII".center(47, '+'))
    print("开发时间：2020年3月6日".center(42, '+'))
    print("-"*50)
    while True:
        ip = input("请输入IP地址或者网址：")
        r = requests.get(url+ip)
        demo = r.text[18000:19000]
        soup = BeautifulSoup(demo, "html.parser")
        try:
            # print(soup.select('.w50-0')[-1].string)
            fr = soup.select('.w50-0')[-1].string
            print('-'*50)
            print("{} 来源于：{}".format(ip,fr))
            print('-'*50)
        except:
            print('-'*50)
            print("域名或IP解析失败，请检查是否输入错误或者网络环境是否正常。\n注意，部分域名（如百度）无法查询；被墙ip或域名可能无法查询\n查询域名时可以加上对应的协议(http或https)")
            print('-'*50)