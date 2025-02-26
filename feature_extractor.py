import pandas as pd
import re
from urllib.parse import urlparse
import whois
from datetime import datetime

def extract_features(url):
    features = {}
    
    features['url_length'] = len(url)
    features['num_special_chars'] = len(re.findall(r'[^a-zA-Z0-9]', url))
    features['has_ip'] = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    
    try:
        domain = urlparse(url).netloc
        features['domain_length'] = len(domain)
        
        features['num_subdomains'] = domain.count('.')
        
        try:
            domain_info = whois.whois(domain)
            creation_date = domain_info.creation_date
            if isinstance(creation_date, list):
                creation_date = creation_date[0]
            features['domain_age'] = (datetime.now() - creation_date).days
        except:
            features['domain_age'] = 36500  
    except:
        features['domain_length'] = 0
        features['num_subdomains'] = 0
        features['domain_age'] = 36500 
    
    suspicious_keywords = ['login', 'verify', 'bank', 'secure', 'account']
    features['has_suspicious_keyword'] = 1 if any(keyword in url for keyword in suspicious_keywords) else 0
    
    return features

if __name__ == "__main__":
    data = pd.read_csv('datasets/url_dataset.csv')
    data['features'] = data['url'].apply(extract_features)
    features_df = data['features'].apply(pd.Series)
    data = pd.concat([data.drop(columns=['features']), features_df], axis=1)
    data.to_csv('datasets/url_dataset_with_features.csv', index=False)
    print("Dataset with features saved as 'url_dataset_with_features.csv'")