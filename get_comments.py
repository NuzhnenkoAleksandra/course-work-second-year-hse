import requests
from tqdm.auto import tqdm
from datetime import datetime

def get_comments(owner_id, post_id, count, version, token):
    data = requests.get(
        get_comments_url, 
        params={
            "owner_id": owner_id,
            "post_id": post_id,
            "count": count,
            "need_likes": 1,
            "v": version,
            "access_token": token
        }
    ).json()

    data1 =  data["response"]["items"]

    texts_li = []
    for item in data1:
        texts_li.append(item["text"])

    return texts_li


def write_appropriate_comments(file, texts_li):
    with open(file, "a", encoding="utf-8") as f:
        for text in texts_li:
            text1 = text.replace("\n", " ")
            #print(text1)
            if len(text1) > 10 and ("тся" in text1 or "ться" in text1):
                if ("ётся" not in text1) and ("ются" not in text1) and ("ется" not in text1) and ("ваться" not in text1):
                    f.write(text1)
                    f.write("\n")

TOKEN = "a6288ca9a6288ca9a6288ca96fa652e07caa628a6288ca9c79a71557404f4d582e0d63a"
VERSION = "5.130"
owner = -138347372
post = 1343929
count = 152

get_comments_url = "https://api.vk.com/method/wall.getComments"

li_posts = []
    
comments = get_comments(owner, post, count, VERSION, TOKEN)
write_appropriate_comments("C:/Users/сергей/OneDrive/Рабочий стол/курсовая2/comments11.txt", comments)
