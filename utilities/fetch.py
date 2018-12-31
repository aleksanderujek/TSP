import urllib3

def fetchFromRemote(url: str) -> str:
  http = urllib3.PoolManager()
  response = http.request('GET', url)
  return response.data.decode('UTF-8')

def fetchFromFile(url: str) -> str:
  text = open(url, "r")
  return text.read()