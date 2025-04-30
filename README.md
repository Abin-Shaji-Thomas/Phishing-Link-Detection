# Phishing URL Detector

## 🛡️ About
This is a Python-based GUI tool that detects phishing URLs using various heuristic checks. It analyzes URLs for suspicious characteristics like:
- Suspicious TLDs
- Phishing-related keywords
- Lack of SSL (HTTPS)
- Shortened URLs
- IP-based domains
- Excessive URL encoding
- Domain age (WHOIS lookup)
- Redirect chains
- Base64 encoding

## 🚀 Features
- **Easy-to-use GUI** built with Tkinter
- **Real-time phishing analysis** using multiple detection methods
- **WHOIS domain age verification**
- **Background image support** for UI customization

## 📌 Requirements
To run the project, install the dependencies:
```sh
pip install -r requirements.txt
```

## 🖥️ Usage
1. **Run the script**
   ```sh
   python phishing_detector.py
   ```
2. **Enter a URL** in the input box
3. **Click 'Check URL'** to analyze
4. The tool will display whether the URL is safe or suspicious.


