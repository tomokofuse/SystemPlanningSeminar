import json
import xmljson
from lxml.etree import parse

# xmlの読み込み
tree = parse('http://weather.livedoor.com/forecast/rss/primary_area.xml')
# すべてのタグの取得
root = tree.getroot()   

# JSONファイルへの書き込み
with open('sample.json', 'w') as fw:
    json.dump(xmljson.yahoo.data(root), fw, indent=2)

ld = open('sample.json')
lines = ld.readlines()
ld.close()

for line in lines:
    if line.find('"id":') >= 0:
        print(line[:-1])