import urllib.request
import urllib.parse
import json
import os
import ssl

TOKEN = os.environ["VERCEL_TOKEN"]
PROJECT_NAME = "jayeshs-personal-site"

HERE = os.path.dirname(os.path.abspath(__file__))


def read_file(rel_path):
    with open(os.path.join(HERE, rel_path), "r") as f:
        return f.read()


def collect_report_files():
    """Walk reports/ and include every HTML + the manifest.

    Each entry maps the on-disk relative path to the same path in the
    Vercel deployment, so reports/leading-indicators/2026-05-22.html stays at
    that URL.
    """
    files = []
    reports_dir = os.path.join(HERE, "reports")
    if not os.path.isdir(reports_dir):
        return files
    for root, _dirs, names in os.walk(reports_dir):
        for name in names:
            if name.startswith("."):
                continue
            abs_path = os.path.join(root, name)
            rel = os.path.relpath(abs_path, HERE).replace(os.sep, "/")
            if not (rel.endswith(".html") or rel.endswith(".json")):
                continue
            with open(abs_path, "r") as f:
                files.append({"file": rel, "data": f.read()})
    return files


payload = {
    "name": PROJECT_NAME,
    "files": [
        {"file": "index.html", "data": read_file("index.html")},
        {"file": "style.css", "data": read_file("style.css")},
        *collect_report_files(),
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
