import requests
url_path = 'https://www.steamclown.org/projects/QInlIj_vIHev/Huch_QIn/' 
url_file = 'all_robots_command_requests.txt'
url = url_path + url_file # Concatenate url path and file name stirngs
r = requests.get(url)

whole_file = r.text
print(whole_file)
