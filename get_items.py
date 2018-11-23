import urllib.request
import urllib.parse
import json
import csv

def write_csv(data, filename):
    count = 0
    with open(filename, 'a') as outf:
        dw = csv.DictWriter(outf, fieldnames=["title","sold","commentCount","item_id","shipping","fastPostFee","userId","nick","userType","isB2c","location","sellerLoc","pic_path","type","tItemType","zkType","zkGroup","priceColor","priceWithRate","auctionURL","isP4p","itemNumId","originalPrice","freight","act","coinLimit","priceWap","price","category","auctionType","url","img2","wwimUrl","previewUrl","favoriteUrl","isMobileEcard","iswebp","name","iconList","icons","area"])
        if count == 0:
            # 第一行才写入头部
            dw.writeheader()
        count += 1
        for row in data:
            dw.writerow(row)

def get_items(searchWords, page):
    url = "https://s.m.taobao.com/search?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&q="+ str(urllib.parse.quote(searchWords)) +"&sst=1&n=20&buying=buyitnow&m=api4h5&token4h5=&abtest=20&wlsort=20&page="+str(page)
    f = urllib.request.urlopen(url)
    result = json.loads(f.read().decode('utf-8'))
    return result['listItem']

def get_items_by_keywords(searchWords, page):
    for i in range(1,page):
        result = get_items(searchWords ,i)
        try:
            write_csv(result,"./result/"+str(searchWords)+"_result.csv")
        except INdexError:
            # 关键词产品已抓取完
            print("该关键词产品已全部抓取完毕")

get_items_by_keywords("空气清新器", 100)