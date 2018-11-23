# 简单的淘宝商品爬虫

> 语言：Python3
> 
> 爬取平台：手机端
> 
> PS：在当前文件夹下先创建好result文件夹

## get_items.py

> 输入：关键词，页数
>
> 调用函数：get_items_by_keywords(关键词, 页数)
>
> 输出：result文件夹下的csv文件, 名字为: 关键词_result.csv

## get_review_cloud.py

> 输入：itemId, userId, 页数
>
> 调用函数：get_cloud_and_reviews(itemId, userId, 页数)
> 
> 输出：result文件夹下的csv文件, 名字为: cloud_itemId.csv
> 
> PS: 先调用get_items获得itemID和userId再使用这个函数获得评论云。