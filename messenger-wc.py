import json
from wordcloud import WordCloud, STOPWORDS
import random
import os
from PIL import Image
import numpy as np
from stop_words import get_stop_words
import multidict as multidict



extra_words = """
å alle at av både båe bare begge ble blei bli blir blitt då da de deg dei deim deira deires dem den denne der dere deres det dette di din disse ditt du dykk dykkar eg ein eit eitt eller elles en enn er et ett etter før for fordi fra ha hadde han hans har hennar henne hennes her hjå ho hoe honom hoss hossen hun hva hvem hver hvilke hvilken hvis hvor hvordan hvorfor i ikke ikkje ingen ingi inkje inn inni ja jeg kan kom korleis korso kun kunne kva kvar kvarhelst kven kvi kvifor man mange me med medan meg meget mellom men mi min mine mitt mot mykje nå når ned no noe noen noka noko nokon nokor nokre og også om opp oss over på så sånn samme seg selv si sia sidan siden sin sine sitt sjøl skal skulle slik so som somme somt til um upp ut uten vår være vært var vart varte ved vere verte vi vil ville vore vors vort
""".split()

norwegian_stop_words = get_stop_words('norwegian')
currdir = os.path.dirname(__file__)
def color_func(word, font_size, position, orientation,  **kwargs):
    return "hsl(223, 96%, " + str(random.randint(40,60)) + "%)"

def get_json_data_from_file(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

def update_table_senders(table, message):
    if message["sender_name"].split()[0] in table:
        table[message["sender_name"].split()[0]] +=1
    else:
        table[message["sender_name"].split()[0]] = 0
    
def create_table_from_senders():
    data = []
    for i in range(num_files):
        data.append(get_json_data_from_file("message_" + str(i+1)+ ".json"))

    table =dict()
    for i in range(num_files):
        for message in data[i]["messages"]:
            update_table_senders(table, message)

    multiDictTable = multidict.MultiDict()
    total, maxFreq, maxName = 0, 0, ""
    i = 0
    for key in table:
        if table[key] > maxFreq:
            maxFreq = table[key]
            maxName = key
        multiDictTable.add(key, table[key])
        i+=1
        total += int(table[key])
        
    for name in table:
        print(name, " has ", int(table[name])/float(total)*100, "% ")
    return multiDictTable


def update_table_content(table, message):
    stopwords = set(STOPWORDS) | set(norwegian_stop_words) |set(extra_words)
    if "content" in message:
        message["content"] = message["content"].encode('latin_1').decode('utf-8')
        content = message["content"].split()
        for word in content:
            word = word.lower()
            if word not in stopwords:
                if word in table:
                    table[word] +=1
                else:
                    table[word] = 0

def create_table_from_content():
    data = []
    for i in range(num_files):
        data.append(get_json_data_from_file("message_" + str(i+1)+ ".json"))

    table =dict()
    for i in range(num_files):
        for message in data[i]["messages"]:
            update_table_content(table, message)
    multiDictTable = multidict.MultiDict()
    i = 0
    for key in table:
        multiDictTable.add(key, table[key])
    return multiDictTable
    

def create_wordcloud_freq(table, shapeFile="cloud.png", outFile="wordcloud.png"):
    mask = np.array(Image.open(os.path.join(currdir+ "shapes/"+shapeFile)))
    wc = WordCloud(stopwords=[], mask=mask, background_color="white", max_words=600)
    wc.generate_from_frequencies(table)
    wc.recolor(color_func=color_func)
    wc.to_file(os.path.join(currdir + "generated-wordclouds/", outFile ))

num_files = 0
for file in os.listdir():
    if file.endswith(".json"):
        num_files += 1

shapeFileSenders = input("Name of shape-file for senders? Press enter for default: cloud.png")
if shapeFileSenders == "":
    shapeFileSenders = "cloud.png"
while not (shapeFileSenders.endswith(".png")):
    shapeFileSenders = input("File name must end with .png")

outFileSenders = input("Name of wordcloud-file for senders? Press enter for default: senders-wordcloud.png")
if outFileSenders == "":
    outFileSenders = "senders-wordcloud.png"
while not (outFileSenders.endswith(".png")):
    outFileSenders = input("File name must end with .png")

shapeFileContent = input("Name of shape-file for senders? Press enter for default: cloud.png")
if shapeFileContent == "":
    shapeFileContent = "facebook-logo.png"
while not (shapeFileContent.endswith(".png")):
    shapeFileContent = input("File name must end with .png")

outFileContent = input("Name of wordcloud-file for message content? Press enter for default: content-wordcloud.png")
if outFileContent == "":
    outFileContent = "content-wordcloud.png"
while not (outFileContent.endswith(".png")):
    outFileContent = input("File name must end with .png")

create_wordcloud_freq(create_table_from_senders(), shapeFileSenders, outFileSenders)

create_wordcloud_freq(create_table_from_content(), shapeFileContent, outFileContent)
