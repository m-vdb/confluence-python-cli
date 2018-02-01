import xmlrpc
import xmlrpc.client
import xmlrpc.server

from .auth import ConfluenceAuth
from .group import ConfluenceGroup
from .page import ConfluencePage
from .space import ConfluenceSpace
from .user import ConfluenceUser


class Api(object):

    def __init__(self, url, username, password):
        self.connect(url, username, password)

    def connect(self, url, username, password):
        url = "%s/rpc/xmlrpc" % url
        self.server = xmlrpc.client.Server(url)
        self.token = ConfluenceAuth(self.server, username, password).login()

    def addpage(self, name, spacekey, content, label="", parentpage=""):
        new_page = ConfluencePage(
            self.token, self.server, name,
            spacekey, content, label=label
        )
        new_page.add(parentpage)
        return new_page

    def updatepage(self, name, spacekey, content, page_id, label=""):
        page = ConfluencePage(self.token, self.server, name, spacekey, page_id, label=label)
        page.update(content, page_id)
        page.set_label()
        return page

    def getpagecontent(self, name, spacekey):
        return ConfluencePage(self.token, self.server, name, spacekey).get_content()

    def getpage(self, name, spacekey):
        return ConfluencePage(self.token, self.server, name, spacekey).get()

    def update_or_add_page(self, *args, **kwargs):
        try:
            return self.updatepage(*args, **kwargs)
        except xmlrpc.Fault:
            return self.addpage(*args, **kwargs)

    def listpages(self, spacekey=""):
        if not spacekey:
            spaces = ConfluenceSpace(self.token, self.server).get_all()
        else:
            spaces = [ConfluenceSpace(self.token, self.server).get_by_key(spacekey)]

        for space in spaces:
            all_pages = ConfluenceSpace(self.token, self.server).get_all_pages(space['key'])
            for page in all_pages:
                yield page, space

    def getallpages(self, spacekey=""):
        all_pages = api.listpages()
        for page, space in all_pages:
            page_content = ConfluencePage(self.token, self.server, page['title'],space['key']).get_content()
            yield page, page_content

    def removepage(self, name, spacekey):
        return ConfluencePage(self.token, self.server, name, spacekey).remove()

    def addspace(self, spacekey, name):
        return ConfluenceSpace(self.token, self.server).create(spacekey, name)

    def removespace(self, spacekey):
        return ConfluenceSpace(self.token, self.server).remove(spacekey)

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

    def addgroup(self, groupname):
        return ConfluenceGroup(self.token, self.server, groupname).add()

    def removegroup(self, groupname):
        return ConfluenceGroup(self.token, self.server, groupname).remove()

    def addusertogroup(self, username, groupname):
        return ConfluenceUser(self.token, self.server, username).add_to_group(groupname)

    def removeuserfromgroup(self, username, groupname):
        return ConfluenceUser(self.token, self.server, username).remove_from_group(groupname)

    def getgroups(self):
        return ConfluenceGroup(self.token, self.server, "users").get_all()

    def getusers(self):
        return ConfluenceUser(self.token, self.server, "users").get_all()

    def getusergroups(self, username):
        return ConfluenceUser(self.token, self.server, username).get_groups()
