from flask import Flask, request
from datetime import datetime
import os # أضفنا هذا السطر لجلب البورت من السيرفر

app = Flask(__name__)

def log_to_termux(ip, agent, lang, platform):
    time_now = datetime.now().strftime("%H:%M:%S")
    print("\n" + "="*50)
    print(f" {time_now} | NEW VISITOR DETECTED!")
    print("="*50)
    print(f" IP ADDRESS : {ip}")
    print(f" PLATFORM   : {platform}")
    print(f" LANGUAGE   : {lang}")
    print(f" BROWSER    : {agent[:60]}...") 
    
    device = "Unknown"
    if "iPhone" in agent: device = "Apple iPhone"
    elif "Android" in agent: device = "Android Mobile"
    elif "Windows" in agent: device = "Windows PC"
    elif "Macintosh" in agent: device = "MacBook/iMac"
    
    print(f" DEVICE TYPE: {device}")
    print("="*50 + "\n")

@app.route('/')
def home():
    # في السيرفرات العالمية، نحتاج جلب الـ IP الحقيقي عبر X-Forwarded-For
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent', 'Unknown')
    accept_lang = request.headers.get('Accept-Language', 'Unknown')
    platform = request.user_agent.platform
    
    log_to_termux(ip_address, user_agent, accept_lang, platform)
    
    return """
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { background: #0f172a; color: white; font-family: sans-serif; text-align: center; padding-top: 50px; }
            .box { border: 2px solid #3b82f6; display: inline-block; padding: 30px; border-radius: 20px; background: #1e293b; }
            h1 { color: #fbbf24; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>كل عام وأنتم بخير ✨</h1>
            <p>أخوكم بلال علي</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    # تعديل مهم جداً لريندر: جلب البورت ديناميكياً
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
