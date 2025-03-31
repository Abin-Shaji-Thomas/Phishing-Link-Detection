import tkinter as tk
from tkinter import messagebox, PhotoImage
import re
import whois
import datetime
import base64
import urllib.parse
import requests
from urllib.parse import urlparse
from PIL import Image, ImageTk

def extract_domain(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except:
        return None

def check_suspicious_tld(url):
    suspicious_tlds = {"ga", "tk", "ml", "cf", "gq"}
    domain = extract_domain(url)
    if domain:
        tld = domain.split('.')[-1]
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
    return len(url) > 75

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
            return age < 30
    except Exception:
        return False
    return False

def check_redirects(url):
    try:
        response = requests.get(url, allow_redirects=True, timeout=5)
        final_url = response.url
        return extract_domain(url) != extract_domain(final_url)
    except:
        return False

def check_url_encoding(url):
    decoded_url = urllib.parse.unquote(url)  # Decode URL
    encoded_chars = re.findall(r'%[0-9A-Fa-f]{2}', url)  # Count encoded characters
    return len(encoded_chars) > 3 and len(url) - len(decoded_url) > 5  # Flag if excessive encoding


def is_phishing_url(url):
    checks = {
        "Suspicious TLD": check_suspicious_tld(url),
        "Phishing Keywords": check_phishing_keywords(url),
        "No SSL": check_ssl(url),
        "Shortened URL": check_shortened_url(url),
        "IP-Based URL": check_ip_based_url(url),
        "Long URL": check_url_length(url),
        "Base64 Encoding": check_base64_encoding(url),
        "New Domain (<30 days)": check_domain_age(url),
        "Redirects to another site": check_redirects(url),
        "Excessive URL Encoding": check_url_encoding(url)
    }
    flagged = [key for key, value in checks.items() if value]
    return flagged if flagged else "Safe"

def check_url():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL")
        return
    result = is_phishing_url(url)
    if result == "Safe":
        result_label.config(text="✅ The URL is SAFE!", fg="green")
    else:
        result_label.config(text=f"⚠️ Phishing Indicators: {', '.join(result)}", fg="red")

# GUI Setup
root = tk.Tk()
root.title("Phishing URL Detector")
root.geometry("1200x700")

# Load background image
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((1200, 700), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=1200, height=700)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Frame for input
frame = tk.Frame(root, bg="white", bd=5)
frame.place(relx=0.5, rely=0.4, anchor="center")

tk.Label(frame, text="Enter URL:", font=("Arial", 14)).pack()
url_entry = tk.Entry(frame, width=50, font=("Arial", 14))
url_entry.pack(pady=10)

check_button = tk.Button(frame, text="Check URL", font=("Arial", 12), command=check_url)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="white")
result_label.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()