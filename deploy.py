import urllib.request
import urllib.parse
import json
import ssl

TOKEN = "vca_6sPp7HfBNfmAP0PhtN05vNy0b9JBE6avhcPAIyE9vq2jgO5oSP4M8T2J"
PROJECT_NAME = "jayeshs-personal-site"

def read_file(name):
    with open(name, "r") as f:
        return f.read()

payload = {
    "name": PROJECT_NAME,
    "files": [
        {
            "file": "index.html",
            "data": read_file("index.html")
        },
        {
            "file": "style.css",
            "data": read_file("style.css")
        }
    ],
    "projectSettings": {
        "framework": None
    }
}

json_data = json.dumps(payload).encode("utf-8")

req = urllib.request.Request(
    "https://api.vercel.com/v13/deployments",
    data=json_data,
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    context = ssl.create_default_context()
    with urllib.request.urlopen(req, context=context) as response:
        res = json.loads(response.read())
        print(f"SUCCESS: {res.get('url')}")
except Exception as e:
    print(f"FAILED: {e}")
    if hasattr(e, 'read'):
        print(e.read().decode())
