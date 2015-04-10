import xmlrpclib

from .auth import ConfluenceAuth
from .page import ConfluencePage
from .space import ConfluenceSpace
from .user import ConfluenceUser


class Api(object):

    def __init__(self, url, username, password):
        self.connect(url, username, password)

    def connect(self, url, username, password):
        url = "%s/rpc/xmlrpc" % url
        self.server = xmlrpclib.Server(url)
        self.token = ConfluenceAuth(self.server, username, password).login()

    def addpage(self, name, spacekey, content, label=None, parentpage=None):
        new_page = ConfluencePage(
            self.token, self.server, name,
            spacekey, content, label=label
        )
        new_page.add(parentpage)
        return new_page

    def updatepage(self, name, spacekey, content, page_id, label=None):
        page = ConfluencePage(self.token, self.server, name, spacekey, page_id, label=label)
        page.update(content, page_id)
        page.set_label()
        return page

    def getpagecontent(self, name, spacekey):
        return ConfluencePage(self.token, self.server, name, spacekey).get_content()

    def getpage(self, name, spacekey):
        return ConfluencePage(self.token, self.server, name, spacekey).get()

    def listpages(self, spacekey=None):
        if not spacekey:
            spaces = ConfluenceSpace(self.token, self.server).get_all()
        else:
            spaces = [ConfluenceSpace(self.token, self.server).get_by_key(spacekey)]

        for space in spaces:
            all_pages = ConfluenceSpace(self.token, self.server).get_all_pages(space['key'])
            for page in all_pages:
                yield page

    def removepage(self, name, spacekey):
        return ConfluencePage(self.token, self.server, name, spacekey).remove()

    def listspaces(self):
        return ConfluenceSpace(self.token, self.server).get_all()

    def adduser(self, newusername, fullname, email, userpassword):
        return ConfluenceUser(self.token, self.server, newusername).create(fullname, email, userpassword)

    def removeuser(self, username):
        return ConfluenceUser(self.token, self.server, username).remove()

    def deactivateuser(self, username):
        return ConfluenceUser(self.token, self.server, username).deactivate()

    def reactivateuser(self, username):
        return ConfluenceUser(self.token, self.server, username).reactivate()

    def changeuserpassword(self, username, newpassword):
        return ConfluenceUser(self.token, self.server, username).change_password(newpassword)

    def getuserinfo(self, username):
        return ConfluenceUser(self.token, self.server, username).get_info()
