import requests
#first parameter of the 'get' method is the 'url':
x = requests.get('https://www.steamclown.org/projects/red_pill.html')
# x = requests.get('https://www.steamclown.org/projects/red_pill.txt')
#print the response text (the content of the requested file):
print(x.text)
