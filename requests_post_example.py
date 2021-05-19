import requests

url = 'https://www.steamclown.org/projects/QInlIj_vIHev/QInlIj_vIHev.php'
robot_line={'robotName':'robot2','robotDevice':'rgb-led','robotInstruction':'red'} 

x = requests.post(url, data = robot_line)

#print the response text (the content of the requested file):
print(robot_line)
print(x.text) # message retured from the request.post()
