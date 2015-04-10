class ConfluenceGroup(object):
    def __init__(self,token,server,groupname):
        self.server = server
        self.token = token
        self.groupname = groupname

    def get_all(self):
        return self.server.confluence2.getGroups(self.token)

    def add(self):
        self.server.confluence2.addGroup(self.token,self.groupname)

    def remove(self):
        self.server.confluence2.removeGroup(self.token,self.groupname,"confluence-users")
