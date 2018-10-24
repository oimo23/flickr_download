# ***************************************
# 必要ライブラリインポート
# ***************************************
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# ***************************************
# API情報
# ***************************************
key = "YOURFlickrKEY"
secret = "YOURFlickrSECRET"
wait_time = 1

# ***************************************
# 保存先指定
# ***************************************
search_name = sys.argv[1]
savedir = "./" + animalname

# ***************************************
# 設定
# ***************************************
flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
	text = search_name,
	per_page = 400,
	media = 'photos',
	sort = 'relevance',
	safe_search = 1,
	extras = 'url_q, licence'
)

# ***************************************
# ダウンロード実行
# ***************************************
photos = result['photos']

for i, photo in enumerate(photos['photo']):
	try:
		url_q = photo['url_q']
		filepath = savedir + '/' + photo['id'] + '.jpg'
		if os.path.exists(filepath): continue
		urlretrieve(url_q, filepath)
		time.sleep(wait_time)
	except:
		continue