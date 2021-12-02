import requests
from PIL import Image
from io import BytesIO
import random
import pandas as pd

def get_insults():
    df = pd.read_csv('../data/impermium_verification_labels.csv')
    df.Comment.replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)
    return df.loc[df['Insult']==1]['Comment']

def get_temps():
    temp = r"https://api.memegen.link/templates/"
    r = requests.get(temp)
    if r.status_code!=200:
        print("NO TEMPLATE FOR YOU")
        return None
    else:
        return [i['id'] for i in r.json()]         
    
# MEME API 
def get_meme():
    temp = random.choice(get_temps())
    text = random.choice(get_insults().values.tolist())
    url = f"https://api.memegen.link/images/{temp}/{text}.png"
    r  =  requests.get(url)
    if r.status_code !=200:
        print("NO MEME FOR YOU")
        return None 
    else:
        img = Image.open((BytesIO(r.content)))
        img.show()
            
                    
if __name__ == '__main__':
    get_meme()
    