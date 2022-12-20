import requests
import json

apikey = ''
url = f"https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key={apikey}"

payload = json.dumps({
  "dynamicLinkInfo": {
    "domainUriPrefix": "https://fcmflutter.page.link",
    "link": "https://www.example.com/",
    "androidInfo": {
      "androidPackageName": "com.example.android"
    },
    "iosInfo": {
      "iosBundleId": "com.example.ios"
    }
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
