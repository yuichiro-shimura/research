import requests
from bs4 import BeautifulSoup

# ページ数の初期値
page_num_init = 1
page_num = page_num_init

# 検索条件
location = "名古屋市"
except_word_1 = "女子校"
except_word_2 = "中高一貫校"
url = "https://www.minkou.jp/hischool/search/pref=aichi/page={}/".format(page_num_init)

# Webページを取得
response = requests.get(url)

# HTMLを解析
soup = BeautifulSoup(response.content, "html.parser")
    
# 件数取得
school_num = int(soup.find("div", class_="mod-pagerNum").find("span").text)
print(f"件数: {school_num}")

# 総ページ数を取得
if school_num % 20 == 0:
    total_page_num = school_num // 20
    
else:
    total_page_num = school_num // 20 + 1

print(f"総ページ数: {total_page_num}")
print()

# 検索条件に適合した数
match_num = 0

while page_num <= total_page_num:
    url = "https://www.minkou.jp/hischool/search/pref=aichi/page={}/".format(page_num)
    
    # Webページを取得
    response = requests.get(url)

    # HTMLを解析
    soup = BeautifulSoup(response.content, "html.parser")
    
    # 検索結果を取得
    results = soup.find_all("div", class_="mod-listSearch-info")
   
    # 検索結果を表示
    for result in results:
        
        # 学校の所在地を取得
        school_summary = result.find("span").text
        
        if location not in school_summary:
            continue
        
        elif except_word_1 in school_summary:
            continue
        
        elif except_word_2 in school_summary:
            continue
        
        # 学校名を取得
        school_name = result.find("a").text
    
        # 偏差値を取得
        school_deviation = result.find("dd").text
    
        # 口コミの点数を取得
        school_review = result.find("div", class_="mod-listSearch-review").find("a").text
    
        # 結果を出力
        print(f"学校名: {school_name}")
        print(f"概要: {school_summary}")
        print(f"偏差値: {school_deviation}")
        print(f"評判: {school_review}")
        print()
        
        match_num += 1
    
    # ページ数増分
    page_num += 1

print(f"ヒット件数:{match_num}")