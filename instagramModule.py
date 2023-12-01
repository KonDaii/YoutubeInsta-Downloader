from instascrape import Reel
import time

def downloadReel(link):
    # session id
    sessionID = '1987763607%3AwpycPlvX2mdLxo%3A20%3AAYeMRylgU5Jg58JkEaciqldbhhhsGrw_37qiK3aCFWk'
    reelLink = link

    # Header with session id
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
        Safari/537.36 Edg/79.0.309.43",
        "cookie": f'sessionid={sessionID};'
    }

    # Passing Instagram reel link as argument in Reel Module
    insta_reel = Reel(
        reelLink)

    # Using  scrape function and passing the headers
    insta_reel.scrape(headers=headers)

    # Giving path where we want to download reel to the
    # download function
    insta_reel.download(fp=f".\\Desktop\\reel{int(time.time())}.mp4")

    # printing success Message
    print('Downloaded Successfully.')
