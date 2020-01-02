import requests
import keyword

def get():
  r = requests.get("http://www.baidu.com/")
  return r

print(keyword.kwlist)

print(get().encoding)
print(get().url)
print(get().text)


