class ConfluenceAuth(object):
    def __init__(self,server,username,password):
        self.server = server
        self.username = username
        self.password = password

    def login(self):
        self.token = self.server.confluence2.login(self.username, self.password)
        return self.token
