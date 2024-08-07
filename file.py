import pymysql

with pymysql.connect(**config) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()


import requests
url = "https://www.bilibili.com/"
html = requests.get(url=url)
html = html.text
print(html)
