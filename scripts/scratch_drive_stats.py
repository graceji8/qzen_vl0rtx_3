import urllib.request
import json

def check_account():
    username = "harrison16899"
    auth_token = "42d6ab0e6ad69c97d6ba4f79c3cd6258c0f6b243"
    ct0 = "b8d892df2d8e380ee2db3b3469abb6c8b9e236a9bc43a1c5635817fd17285432d7fffe5a195f4d5209f7e7e19b20f776402d9500f5be15ef7ba3f0d8a3ad413b1fda3c17f92c3ff79be00a59995e1471"
    
    url = "https://api.twitter.com/1.1/account/settings.json"
    headers = {
        "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "Cookie": f"auth_token={auth_token}; ct0={ct0}",
        "X-Csrf-Token": ct0,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "x-twitter-active-user": "yes",
        "x-twitter-client-language": "en"
    }
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print("OK, screen_name:", data.get("screen_name"))
    except Exception as e:
        print("ERROR:", getattr(e, 'read', lambda: b'')().decode() or e)

if __name__ == "__main__":
    check_account()
