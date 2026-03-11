import requests
from datetime import datetime
import os

# 建立 data 資料夾
os.makedirs("data", exist_ok=True)

# 抓 API
url = "https://water.taiwanstat.com/data/data.json"
resp = requests.get(url)
resp.raise_for_status()  # 有問題會跳錯誤

# 生成 UTC+8 時間字串
TIME = datetime.utcnow().timestamp() + 8*3600  # 加8小時
TIME_STR = datetime.utcfromtimestamp(TIME).strftime("%Y%m%d_%H%M%S")

# 儲存檔案
filename = f"data/data_{TIME_STR}.json"
with open(filename, "w", encoding="utf-8") as f:
    f.write(resp.text)

print(f"Saved {filename}")