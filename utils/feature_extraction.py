# utils/feature_extraction.py
import re
from urllib.parse import urlparse

def has_ip_address(url):
    ip_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    return 1 if ip_pattern.search(url) else -1

def is_long_url(url, threshold=50):
    return -1 if len(url) > threshold else 1

def is_shortened(url):
    shortening_services = ['bit.ly', 'tinyurl.com', 'ow.ly', 'is.gd', 'goo.gl'] # Add more as needed
    return 1 if any(service in url for service in shortening_services) else -1

def has_at_symbol(url):
    return 1 if '@' in url else -1

def has_redirecting(url):
    return 1 if '//' in url[8:] else -1

def has_prefix_suffix(url):
    try:
        domain = urlparse(url).netloc
        return 1 if '-' in domain else -1
    except:
        return -1

def count_subdomains(url):
    try:
        domain = urlparse(url).netloc
        subdomains = domain.split('.')
        return len(subdomains) - 2 if len(subdomains) > 2 else -1 # -2 to exclude domain and top-level domain
    except:
        return -1

def uses_https(url):
    return 1 if url.startswith('https') else -1

def extract_features(url):
    """Extracts features from a URL."""
    features = {
        'UsingIP': has_ip_address(url),
        'LongURL': is_long_url(url),
        'ShortURL': is_shortened(url),
        'Symbol@': has_at_symbol(url),
        'Redirecting//': has_redirecting(url),
        'PrefixSuffix-': has_prefix_suffix(url),
        'SubDomains': count_subdomains(url),
        'HTTPS': uses_https(url),
        'DomainRegLen': -1, # Skipping because it requires external lookup
        'Favicon': -1,
        'NonStdPort': -1,
        'HTTPSDomainURL': -1,
        'RequestURL': -1,
        'AnchorURL': -1,
        'LinksInScriptTags': -1,
        'ServerFormHandler': -1,
        'InfoEmail': -1,
        'AbnormalURL': -1,
        'WebsiteForwarding': -1,
        'StatusBarCust': -1,
        'DisableRightClick': -1,
        'UsingPopupWindow': -1,
        'IframeRedirection': -1,
        'AgeofDomain': -1,
        'DNSRecording': -1,
        'WebsiteTraffic': -1,
        'PageRank': -1,
        'GoogleIndex': -1,
        'LinksPointingToPage': -1,
        'StatsReport': -1,
    }
    return features
