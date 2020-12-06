from pymongo import MongoClient

client = MongoClient("mongodb+srv://robindermongo:root@cluster0.hon6x.mongodb.net/test")
mydb = client["ProcessedDb"]
mycol = mydb["ProcessedData"]
dict_obj = []

values_positive = ['accepted', 'acclaimed', 'accomplish', 'accomplishment', 'beaming', 'beautiful', 'believe',
                   'beneficial', 'bliss',
                   'calm', 'celebrated', 'certain', 'champ', 'champion', 'earnest', 'easy', 'ecstatic', 'effective',
                   'fabulous', 'fair',
                   'familiar', 'famous', 'generous', 'genius', 'genuine', 'giving', 'handsome', 'happy', 'harmonious',
                   'healing', 'health', 'safety']
values_negative = ['abysmal', 'adverse', 'alarming', 'angry', 'annoy', 'anxious', 'bad', 'banal', 'barbed',
                   'belligerent', 'bemoan', 'callous',
                   'clumsy', 'coarse', 'damage', 'damaging', 'dastardly', 'dead', 'decaying', 'deformed', 'enraged',
                   'eroding', 'evil', 'fail', 'faulty', 'fear', 'feeble', 'fight', 'filthy', 'gawky', 'ghastly',
                   'grave', 'greed', 'grim',
                   'grimace', 'haggard', 'hard', 'harmful', 'hate', 'negative']

for x in mycol.find():
    dict_obj.append(x)
value_list = []

for y in dict_obj:
    obj = {}
    text = y['text']
    split_words = text.split()
    # print(split_words)
    for words in split_words:
        if words in obj.keys():
            obj[words] += 1
        else:
            obj[words] = 1
    value_list.append(obj)


for words in value_list:
    words['polarity'] = 0
    pos_count = 0
    neg_count = 0
    words['match'] = set()
    for word_value in words.keys():
        if word_value.casefold() in values_positive:
            pos_count += 1
            words['polarity'] = words['polarity'] + pos_count
            words['match'].add(word_value)
        elif word_value.casefold() in values_negative:
            neg_count += 1
            words['polarity'] = words['polarity'] - neg_count
            words['match'].add(word_value)

for word_result in value_list:
    word_result['result_value'] = ""
    if word_result is None:
        pass
    elif word_result['polarity'] > 0:
        word_result['result_value'] = 'POSITIVE'
    elif word_result['polarity'] < 0:
        word_result['result_value'] = 'NEGATIVE'
    else:
        word_result['result_value'] = 'NEUTRAL'

print(value_list)
