from .greeting import greet
from .http_client import HTTPClient

def main():
  print(greet("roronya"))
  print(HTTPClient.get("http://example.com"))

if __name__ == '__main__':
  main()
