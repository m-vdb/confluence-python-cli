class ConfluenceUser(object):
    def __init__(self,token,server,username):
        self.server = server
        self.token = token
        self.username = username

    def create(self,full_name,email,password):
        self.password = password
        self.email = email
        self.full_name = full_name
        self.user_to_create = {"name":self.username,"fullname":self.full_name,"email":self.email}
        self.server.confluence2.addUser(self.token,self.user_to_create,self.password)

    def get_info(self):
        return self.server.confluence2.getUser(self.token,self.username)

    def get_groups(self):
        return self.server.confluence2.getUserGroups(self.token,self.username)

    def remove(self):
        self.server.confluence2.removeUser(self.token,self.username)

    def deactivate(self):
        self.server.confluence2.deactivateUser(self.token,self.username)

    def reactivate(self):
        self.server.confluence2.reactivateUser(self.token,self.username)

    def add_to_group(self,group):
        self.group = group
        self.server.confluence2.addUserToGroup(self.token,self.username,self.group)

    def remove_from_group(self,group):
        self.group = group
        self.server.confluence2.removeUserFromGroup(self.token,self.username,self.group)   

    def change_password(self,password):
        self.password = password
        self.server.confluence2.changeUserPassword(self.token,self.username,self.password)   

    def get_all(self):
        return self.server.confluence2.getActiveUsers(self.token, True)
