import pandas as pd
import requests

phish_url = "../datasets/verified_online.csv"
phish_data = pd.read_csv(phish_url)
phish_data = phish_data[['url']]  
phish_data['label'] = 1  

alexa_url = "../datasets/top-1m.csv"
alexa_data = pd.read_csv(alexa_url, header=None, names=['rank', 'url'])
alexa_data = alexa_data[['url']]  
alexa_data['label'] = 0  

data = pd.concat([phish_data, alexa_data], ignore_index=True)

data.to_csv('../datasets/url_dataset.csv', index=False)
print("Dataset saved as 'url_dataset.csv'")