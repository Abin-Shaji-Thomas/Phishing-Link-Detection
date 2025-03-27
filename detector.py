import re
import whois
import datetime
import base64
import urllib.parse
from urllib.parse import urlparse

def extract_domain(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if domain.startswith("www."):
            domain = domain[4:]  # Remove 'www.'
        return domain
    except:
        return None

def check_suspicious_tld(url):
    suspicious_tlds = {"ga", "tk", "ml", "cf", "gq"}
    domain = extract_domain(url)
    if domain:
        tld = domain.split('.')[-1]  # Get the last part of domain (TLD)
        return tld in suspicious_tlds
    return False

def check_phishing_keywords(url):
    phishing_keywords = {"secure-login", "banking", "verification", "confirm", "update", "account"}
    return any(keyword in url.lower() for keyword in phishing_keywords)

def check_ssl(url):
    return not url.startswith("https://")

def check_shortened_url(url):
    shortened_domains = {"bit.ly", "goo.gl", "tinyurl.com", "ow.ly", "is.gd"}
    domain = extract_domain(url)
    return domain in shortened_domains

def check_ip_based_url(url):
    return bool(re.match(r"^\d{1,3}(\.\d{1,3}){3}$", extract_domain(url)))

def check_url_length(url):
    return len(url) > 75  # Flag URLs longer than 75 characters

def check_base64_encoding(url):
    parts = url.split('/')
    for part in parts:
        if len(part) % 4 == 0 and re.match("^[A-Za-z0-9+/=]+$", part):
            try:
                decoded = base64.b64decode(part).decode('utf-8')
                return True
            except Exception:
                continue
    return False

def check_domain_age(url):
    try:
        domain = extract_domain(url)
        if not domain:
            return False
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date
        
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        
        if creation_date and isinstance(creation_date, datetime.datetime):
            age = (datetime.datetime.now() - creation_date).days
            return age < 30  # Flag domains younger than 30 days
    except Exception:
        return False
    return False

def is_phishing_url(url):
    checks = {
        "Suspicious TLD": check_suspicious_tld(url),
        "Phishing Keywords": check_phishing_keywords(url),
        "No SSL": check_ssl(url),
        "Shortened URL": check_shortened_url(url),
        "IP-Based URL": check_ip_based_url(url),
        "Long URL": check_url_length(url),
        "Base64 Encoding": check_base64_encoding(url),
        "New Domain (<30 days)": check_domain_age(url)
    }
    
    flagged = [key for key, value in checks.items() if value]
    return flagged if flagged else "Safe"
