import webbrowser
import sys
try:
    if len(sys.argv) > 1 :
        # get argument string from command line
        address = ''.join(sys.argv[1:])
    webbrowser.open('https://www.google.com/maps/place/' + address)
except:
    print('no address provided') 
