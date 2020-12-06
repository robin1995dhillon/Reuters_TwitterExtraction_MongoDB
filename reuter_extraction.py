import math

from pymongo import MongoClient

client = MongoClient("mongodb+srv://robindermongo:root@cluster0.hon6x.mongodb.net/test")
mydb = client["ReutersDb"]
mycol = mydb["ReutersData"]

dict_obj = []
list_canada = []
dict_canada = dict()
values = ['canada', 'rain', 'hot', 'cold']
val = 'canada'
count_doc = 0
count_canada = 0
count_rain = 0
count_hot = 0
count_cold = 0
div_canada = 0
div_rain = 0
div_hot = 0
div_cold = 0
log_canada = 0
log_rain = 0
log_hot = 0
log_cold = 0

dict_count = 0
count = 0

for x in mycol.find():
    dict_obj.append(x)
    count_doc += 1

for y in dict_obj:
    title = y['title']
    body = y['body']
    for value in values:
        if title is None:
            pass
        elif value in title.casefold():
            if value == 'canada':
                count_canada += 1
            elif value == 'rain':
                count_rain += 1
            elif value == 'hot':
                count_hot += 1
            elif value == 'cold':
                count_cold += 1
            continue
        if body is None:
            continue
        elif value in body.casefold():
            if value == 'canada':
                count_canada += 1
            elif value == 'rain':
                count_rain += 1
            elif value == 'hot':
                count_hot += 1
            elif value == 'cold':
                count_cold += 1
            continue


div_canada = count_doc / count_canada
div_rain = count_doc / count_rain
div_hot = count_doc / count_hot
div_cold = count_doc / count_cold

log_canada = math.log10(div_canada)
log_rain = math.log10(div_rain)
log_hot = math.log10(div_hot)
log_cold = math.log10(div_cold)

for a in dict_obj:
    total_words = 0
    total_words_title = 0
    count_frequency = 0
    title = a['title']
    body = a['body']
    if title is None:
        pass
    elif val in title.casefold():
        total_words_title += len(title.split())
        count_frequency += title.casefold().count(val)
        print(total_words_title)
        print(count_frequency)
        dict_canada[title] = count_frequency / total_words_title
        print(dict_canada)

    if body is None:
        pass
    elif val in body.casefold():
        total_words = total_words_title + len(body.split())
        count_frequency += body.casefold().count(val)
        print(total_words)
        print(count_frequency)
        dict_canada[title] = count_frequency / total_words
        print(dict_canada)

print("dictionary iss", dict_canada.values())

max_key = max(dict_canada, key=dict_canada.get)
print("Highest relative frequency is ", max_key, dict_canada[max_key])
