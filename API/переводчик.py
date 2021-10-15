import requests
url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"

a = input('введите текст для перевода: ')
s , j = input() , input()
ds = f'{s}|{j}'
querystring = {"langpair":ds,"q":a,"key":"b054735cf78d8a64ca2b"}

headers = {
    'x-rapidapi-host': "translated-mymemory---translation-memory.p.rapidapi.com",
    'x-rapidapi-key': "4a8442b275mshcaba0b215519cdap10cadcjsnd73e91828e3b"
    }

response = requests.get(url, headers=headers, params=querystring)
d = response.json()
hg = d['matches'][0]['translation']
print(hg)