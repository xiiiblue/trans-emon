url = 'http://http-dyn.abuyun.com:9020'
url_split = url.split('://')
url = f'{url_split[0]}://aaa:bbb@{url_split[1]}'
print(url)
