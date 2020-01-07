import requests

def get():
  r = requests.get("http://www.baidu.com/")
  return r

print(get().encoding)
print(get().url)
print(get().text)