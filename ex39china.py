#!/bin/python3
# -*- coding: utf-8 -*-
# ex39China: Dictionaries, Oh Lovely Dictionaries


# create a mapping of province to abbreviation
cn_province = {
    '廣東': '粵',
    '湖南': '湘',
    '四川': '川',
    '雲南': '滇',
    }

# create a basic set of provinces and some cities in them
cn_cities = {
    '粵': '廣州',
    '湘': '長沙',
    '川': '成都',
    }

# add some more data
cn_province['台灣'] = '台'

cn_cities['滇'] = '昆明'
cn_cities['台'] = '高雄'

print('-' * 10)
for prov, abbr in cn_province.items():
    print("%s省的縮寫是%s" % (prov, abbr))

print('-' * 10)
cn_abbrevs = {values: keys for keys, values in cn_province.items()}
for abbrev, prov in cn_abbrevs.items():
    print("%s是%s省的縮寫" % (abbrev, prov))

print('-' * 10)
for abbrev, city in cn_cities.items():
    print("%s市位於我國的%s省" % (city, cn_abbrevs[abbrev]))
