import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 定义你的URLs
# 修改此处jx0404id=xxxx为你的课程ID
base_url = "http://jwxt.upc.edu.cn/jsxsd/kscj/pscj_list.do?xs0101id={}&jx0404id=xxxx&zcj="

# 定义你的cookies和headers
# 修改此处JSESSIONID=xxxx和SERVERID=xxxx为你的cookies
cookies = {
    "JSESSIONID": "",
    "SERVERID": ""
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Connection": "keep-alive"
}

# 自定义四舍五入函数
def round_half_up(n):
    return int(n) + int((n * 10) % 10 >= 5)

# 定义一个函数来获取成绩并保存到Excel文件中
def get_scores(start, end, filename):
    # 创建一个新的Workbook
    wb = Workbook()
    ws = wb.active

    # 对每个URL发送HTTP请求
    data_found = False
    for i in range(start, end+1):
        url = base_url.format(i)
        response = requests.get(url, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'id': 'dataList'})
        if table:
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) > 17:
                    total_score = 0
                    for j in range(1, 17, 2):
                        score = float(cells[j].text) if cells[j].text else 0
                        weight = float(cells[j+1].text.replace('%', '')) / 100 if cells[j+1].text and '%' in cells[j+1].text else 0
                        total_score += score * weight
                    total_score = round_half_up(total_score)  # 使用自定义的四舍五入函数
                    ws.append([i, total_score])
                    data_found = True

    # 检查是否有任何有效的URL
    if data_found:
        # 保存Workbook到Excel文件中
        wb.save(filename + '.xlsx')
    else:
        print("无匹配")

# 调用函数来获取成绩并保存到不同的Excel文件中
# 修改此处的2000000101和2000000128为你要查询的学号范围，此处为2000000101到2000000128，即为查询1班01到28号同学的成绩
get_scores(2000000101, 2000000128, 'scores1ban')

