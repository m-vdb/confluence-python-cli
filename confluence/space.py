class ConfluenceSpace(object):
    def __init__(self, token, server):
        self.server = server
        self.token = token

    def get_all(self):
        self.spaces = self.server.confluence2.getSpaces(self.token)
        return self.spaces

    def get_by_key(self,space_key):
        self.space_key = space_key
        self.space = self.server.confluence2.getSpace(self.token,self.space_key)
        return self.space

    def create(self,space_key,space_name):
        self.space_key = space_key
        self.space_name = space_name
        self.space_to_create = {"key":self.space_key,"name":self.space_name}
        self.server.confluence2.addSpace(self.token,self.space_to_create)
        return self.get_by_key(space_key)

    def remove(self,space_key):
        self.space_key = space_key
        self.server.confluence2.removeSpace(self.token,self.space_key)

    def get_all_pages(self,spaceKey):
        self.spacekey = spaceKey
        return self.server.confluence2.getPages(self.token, self.spacekey)
