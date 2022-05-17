import webbrowser
import sys
try:
    if len(sys.argv) > 1 :
        # get argument string from command line
        cmd_parameter1 = ''.join(sys.argv[1:])
    print(cmd_parameter1)
except:
    print('no cmd argument provided') 
