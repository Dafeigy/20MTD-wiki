import pandas as pd
import re



with open ('static\ORIGIN\TextAsset\localization', 'r', encoding='utf-8') as f:
    texts =f.readlines()


def format_data(line:str):
    return re.findall('"(.*?)"',line)[:-1]
    
df = pd.DataFrame(columns=("key","en","jp","ch","tc","ru","sp","latam","gr","pl","it","tr","fr","br","pr","kr","hu"))

for index, data in enumerate(texts):
    if index == 0:
        continue
    df.loc[index] = format_data(data)

df.to_csv('static\localization.csv',index=False,encoding='utf_8_sig')

