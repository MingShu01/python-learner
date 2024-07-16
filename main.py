import datetime, request

def main():
  Nowtime = datetime.datetime()
  response = request.get('https://www.github.com')
  time = datetime.datetime()
  return response.status_code time

if __name__ == '__main__':
  main()

