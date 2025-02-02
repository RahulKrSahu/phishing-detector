import re
from urllib.parse import urlparse

def extract_features(url):
    features = {}

    # Feature 1: Length of URL
    features['url_length'] = len(url)

    # Feature 2: Number of special characters
    features['num_special_chars'] = len(re.findall(r'[^\w\s]', url))

    # Feature 3: Presence of HTTPS
    features['has_https'] = 1 if url.startswith('https') else 0

    # Feature 4: Number of subdomains
    parsed_url = urlparse(url)
    features['num_subdomains'] = parsed_url.netloc.count('.')

    # Feature 5: Presence of IP address in URL
    features['has_ip'] = 1 if re.match(r'\d+\.\d+\.\d+\.\d+', parsed_url.netloc) else 0

    return list(features.values())