import requests

url = 'https://www.steamclown.org/projects/QInlIj_vIHev/QInlIj_vIHev.php'
robot_line={'robotName':'Your-Robot-Name','robotDevice':'rgb-led','robotInstruction':'#FF001F'} 

x = requests.post(url, data = robot_line)

#print the response text (the content of the requested file):
print(robot_line)
print(x.text) # message retured from the request.post()
