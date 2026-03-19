from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

def log_to_termux(ip, agent, lang, platform):
    time_now = datetime.now().strftime("%H:%M:%S")
    print("\n" + "="*50)
    print(f" {time_now} | NEW VISITOR DETECTED!")
    print("="*50)
    print(f" IP ADDRESS : {ip}")
    print(f" PLATFORM   : {platform}")
    print(f" LANGUAGE   : {lang}")
    print(f" BROWSER    : {agent[:60]}...") # Showing first 60 chars of Agent
    
    # Simple Device Detection Logic
    device = "Unknown"
    if "iPhone" in agent: device = "Apple iPhone"
    elif "Android" in agent: device = "Android Mobile"
    elif "Windows" in agent: device = "Windows PC"
    elif "Macintosh" in agent: device = "MacBook/iMac"
    
    print(f" DEVICE TYPE: {device}")
    print("="*50 + "\n")

@app.route('/')
def home():
    # Gathering more data
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Unknown')
    accept_lang = request.headers.get('Accept-Language', 'Unknown')
    platform = request.user_agent.platform
    
    # Print to Termux (English)
    log_to_termux(ip_address, user_agent, accept_lang, platform)
    
    # Website Content (Arabic for the visitor)
    return """
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { background: #0f172a; color: white; font-family: sans-serif; text-align: center; padding-top: 50px; }
            .box { border: 2px solid #3b82f6; display: inline-block; padding: 30px; border-radius: 20px; background: #1e293b; }
            h1 { color: #fbbf24; }
            .alert { color: #f87171; font-weight: bold; margin-top: 20px; border: 1px solid #f87171; padding: 10px; border-radius: 10px; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>كل عام وأنتم بخير ✨</h1>
            <p>أخوكم بلال علي</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Running the app
    app.run(host='0.0.0.0', port=8080)

