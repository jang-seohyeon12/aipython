import requests
from bs4 import BeautifulSoup

# 멜론 차트 URL
url = "https://www.melon.com/chart/index.htm"

# 요청 헤더 (멜론은 User-Agent가 없으면 접근을 차단할 가능성이 있음)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Referer": "https://www.melon.com/"
}

# 요청 보내기
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 노래 제목 가져오기
songs = soup.select("tr .ellipsis.rank01 span a")

# 가수명 가져오기
artists = soup.select("tr .ellipsis.rank02 span a")

# 차트 출력
for rank, (song, artist) in enumerate(zip(songs, artists), start=1):
    print(f"{rank}위: {song.text} - {artist.text}")
    
