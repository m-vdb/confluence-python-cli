import xmlrpclib

from .auth import ConfluenceAuth


def connect(url, username, password):
    url = "%s/rpc/xmlrpc" % url
    xml_server = xmlrpclib.Server(url)
    token = ConfluenceAuth(xml_server, username, password).login()
    return {"token": token, "xml_server": xml_server}
