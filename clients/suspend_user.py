#adapted from client scripts on dellswor@github.com

import sys
import json
import datetime

# URL lib parts
from urllib.request import Request, urlopen
from urllib.parse   import urlencode

def main():
    # Check the CLI arguments
    if len(sys.argv)<3 :
        print("Usage: python3 %s <url> <username>"%sys.argv[0])
        return
    
    # Prep the arguments blob
    args = dict()
    args['timestamp'] = datetime.datetime.utcnow().isoformat()
    args['username']  = sys.argv[2]

    # Print a message to let the user know what is being tried
    print("Suspending user: %s"%args['username'])

    # Setup the data to send
    sargs = dict()
    sargs['arguments']=json.dumps(args)
    sargs['signature']=''
    data = urlencode(sargs)
    #print("sending:\n%s"%data)
    
    # Make the resquest
    url_str = sys.argv[1] + 'rest/suspend_user'
    req = Request(url_str,data.encode('ascii'),method='POST')
    res = urlopen(req)
    
    # Parse the response
    #resp = json.loads(res.read().decode('ascii'))
    
    # Print the result code
    print("Call to LOST returned: %s"%res.read())#p['result'])
    

if __name__=='__main__':
    main()
    
