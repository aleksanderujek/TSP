def fetchFromFile(url: str) -> str:
  text = open(url, "r")
  return text.read()