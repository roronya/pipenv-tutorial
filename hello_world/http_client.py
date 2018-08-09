import requests

class HTTPClient:
  def get(url):
    return requests.get(url).content
