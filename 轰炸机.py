import hashlib
import json
import random
import sys
import threading
import time
import requests as requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# 请求部分，按顺序使用所有代理
url = "https://icluod-id.ifvaw.xyz//iCIoud-id/Public/ojbk2.asp"
url2 = "https://icluod-id.ifvaw.xyz//iCIoud-id/Public/ojbk3.asp"
cnt = 0
max_threads = 5
cnt_lock = threading.Lock()

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "cookie": "ASPSESSIONIDCUCSSABB=BKLPJKJBOFJKEECGPPLFHFFE",
    "Referer": "https://icluod-id.ifvaw.xyz//iCIoud-id/Public/3jsgp5p2gutxa39q1o0a.asp?3jsgp5p2gutxa39q1o0a",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

def send_requests(proxy):
    global cnt  # 使用全局的 cnt 变量
    session = requests.Session()
    session.proxies = proxy
    while True:
        textUser = random.randint(100000000, 999999999)
        textPms = random.randint(100000, 999999)
        textPwd = textUser - textPms
        textTel = random.randint(13700000000, 18900000000)

        data1 = {
            "textUser": str(textUser) + "@163.com",
            "textPwd": str(textPwd)
        }
        data2 = {
            "textTel": textTel,
            "textPms": textPms,
            "textUser": str(textUser) + "@163.com",
            "textPwd": ""
        }
        #F323110310550316454O
        try:
            res = session.post(url=url, headers=headers, data=json.dumps(data1),verify=False,allow_redirects=False)
            res2 = session.post(url=url2, headers=headers, data=json.dumps(data2),verify=False,allow_redirects=False)

            # 如果当前代理地址被屏蔽，可以根据具体条件检查状态码或内容
            # if res.status_code != 200 or res2.status_code != 200 or "alert" in res.text or "alert" in res2.text:
            #     print(f"Proxy {proxy['http']} is blocked. Exiting thread.")
            #     return  # 退出线程
        except requests.exceptions.RequestException as e:
            print(f"Request error with proxy {proxy['http']}: {e}")
            # return  # 出现异常，退出线程

            # 处理响应
        print("\rProcessing: cnt={}, status1={}, status2={}, 当前线程数: {}".format(cnt, res.text, res2.text.strip(),
                                                                                  threading.active_count()), end='', flush=True)
        cnt += 1

# 获取代理信息的部分（与上面的示例代码相同）




_version = sys.version_info
is_python3 = (_version[0] == 3)
orderno = ""
secret = ""
ip = "dtan.xiongmaodaili.com"
port = "8088"
ip_port = ip + ":" + port
timestamp = str(int(time.time()))

txt = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

if is_python3:
    txt = txt.encode()

md5_string = hashlib.md5(txt).hexdigest()
sign = md5_string.upper()

auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp + "&change=true"
proxy = {"http":"http://" + ip_port, "https": "http://" + ip_port}
headers = {"Xiongmao-Proxy-Authorization": auth, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

# headers = {"Proxy-Authorization": auth,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
# api_url = "http://pandavip.xiongmaodaili.com/xiongmao-web/apiPlus/vgl?secret=*&orderNo=*&count=10&isTxt=0&proxyType=1&validTime=0&removal=0&cityIds="
#
#
# response = requests.get(api_url)
# print(response)
#     # 定义代理列表
# proxies = []
#
# # 检查响应是否成功
# if response.status_code == 200:
#     data = response.json()
#     if data.get("code") == "0":
#         proxy_list = data.get("obj")
#         if proxy_list:
#             for proxy in proxy_list:
#                 ip = proxy.get("ip")
#                 port = proxy.get("port")
#                 proxy_dict = {
#                     "http": f"http://{ip}:{port}",
#                     "https": f"http://{ip}:{port}"
#                 }
#                 proxies.append(proxy_dict)
#                 print(f"Added Proxy: {ip}:{port}")
#         else:
#             print("Error: No available proxy found.")
#     else:
#         print(f"Error: {data.get('msg')}")
# else:
#     print(f"Error: Failed to retrieve proxy information. Status code: {response.status_code}")

# 创建线程列表
threads = []

# 遍历代理列表并创建线程
for i in range(10):
    thread = threading.Thread(target=send_requests, args=(proxy,))
    threads.append(thread)

# 启动线程
for thread in threads:
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

