from dellswor lost_archived

from urllib.request/parse import Request, urlopen/urlencode

def main():
    
    #prep args
    args = dict()
    args['username'] = sys.argv[2]
    args['password'] = sys.argv[3]
    args['role'] = sys.argv[4]
    data = urlencode(args)

    my_route = 'activate_user'
    req = Request(sys.argv[1] + my_route, data.encode(ascii), method='POST')

    res = urlopen(req)

    print("%s"%res.read())
