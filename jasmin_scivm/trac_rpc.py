
import xmlrpclib
import getpass

class CEDAServicesTransport(xmlrpclib.SafeTransport):
    """
    Based upon code at http://bytes.com/topic/python/answers/509382-solution-xml-rpc-over-proxy
    """

    def __init__(self, username, pw, verbose = None, use_datetime=0):
        self._username = username
        self._pw = pw
        self._realm = 'CEDA Services login'
        self.verbose = verbose
        self._use_datetime = use_datetime

    def request(self, host, handler, request_body, verbose):
        import urllib2

        url = 'http://'+host+handler
        request = urllib2.Request(url)
        request.add_data(request_body)
        # Note: 'Host' and 'Content-Length' are added automatically
        request.add_header("User-Agent", self.user_agent)
        request.add_header("Content-Type", "text/xml") # Important

        # setup authentication
        authhandler = urllib2.HTTPBasicAuthHandler()
        authhandler.add_password(self._realm, url, self._username, self._pw)
        opener = urllib2.build_opener(authhandler)

        f=opener.open(request)
        return(self.parse_response(f))

def make_proxy(username=None, password=None):
    if username is None:
        username = getpass.getuser()
    if password is None:
        password = getpass.getpass()
    transport = CEDAServicesTransport(username, password)
    server = xmlrpclib.ServerProxy("http://proj.badc.rl.ac.uk/cedaservices/login/xmlrpc", 
                                   transport=transport)
    return server

