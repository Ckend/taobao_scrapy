import urllib.request
import urllib.parse
import json
import csv

def write_csv(data, filename):
    count = 0
    with open(filename, 'a') as outf:
        dw = csv.DictWriter(outf, data[0].keys())
        if count == 0:
            # 第一行才写入头部
            dw.writeheader()
        count += 1
        for row in data:
            dw.writerow(row)


def get_review_cloud(itemID):
    # 评论云
    url="https://rate.tmall.com/listTagClouds.htm?itemId="+str(itemID)+"&isAll=true&isInner=true"
    f = urllib.request.urlopen(url)
    data = f.read().decode('utf-8')
    data = data.replace('(',"")
    data = data.rstrip(')')
    result = json.loads(data)
    print(result)
    return result['tags']['tagClouds']

def get_cloud_and_reviews(itemId, userId, page):
    cloud = get_review_cloud(itemId)
    write_csv(cloud,"./result/"+'cloud_'+itemId+'.csv')

itemId = "569753598854"
userId = "2873324802"
get_cloud_and_reviews(itemId,userId,10)