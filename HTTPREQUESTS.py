import requests

url_get = "http://httpbin.org/get"
payload = {"name": "Joseph", "ID": "123"}

# r = requests.get(url_get, params=payload)
# print(r.url)

url_post = "http://httpbin.org/post"
r_post = requests.post(url_post, payload)

print(r_post.json()["form"])
