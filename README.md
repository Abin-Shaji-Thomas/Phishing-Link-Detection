
**Phishing URL Detector 🔍**  

**A Flask-based web application that detects phishing URLs by analyzing various security factors. This tool helps users identify potentially harmful links by checking for suspicious TLDs, phishing keywords, SSL status, and domain age.**  

 **🚀 Features**  
- Detects phishing URLs using multiple security checks  
- Analyzes domain age, SSL certificate, and URL structure  
- Identifies suspicious keywords and short URLs  
- Easy-to-use web interface built with Flask  

 **🛠 Tech Stack**  
- **Backend**: Python, Flask  
- **Security Analysis**: WHOIS lookup, URL parsing, Regex  

 **📦 Installation**  
1. **Clone the repository**  
   bash
   git clone https://github.com/Abin-Shaji-Thomas/phishing-url-detector.git
   cd phishing-url-detector
   
2. **Install dependencies**  
   bash
   pip install -r requirements.txt
   
3. **Run the Flask app**  
   bash
   python app.py
   
4. Open your browser and visit **http://127.0.0.1:5000/**  

 **📝 How It Works**  
The system checks URLs based on:  
✔️ Suspicious TLDs (e.g., .tk, .ml)  
✔️ Phishing keywords in the URL  
✔️ SSL certificate (HTTPS or not)  
✔️ Shortened URLs (e.g., bit.ly, goo.gl)  
✔️ Recently registered domains (<30 days)  
  
 **📜 License**  
**This project is open-source and available under the [MIT License](LICENSE).**  

**Give it a ⭐ on GitHub if you like this project! 🚀**  
