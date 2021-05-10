import requests
r = requests.get('https://www.steamclown.org/projects/QInlIj_vIHev/Huch_QIn/all_robots_command_requests.txt')

whole_file = r.content
print(whole_file)
whole_file = r.text
print(whole_file)

