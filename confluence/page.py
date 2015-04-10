import logging


class ConfluencePage(object):
    def __init__(self,token,server,name,spaceKey,content="",page_id="",label=""):
        self.server = server
        self.token = token
        self.name = name
        self.spaceKey = spaceKey
        self.content = content
        self.label = label
        self.logger = logging.getLogger(
            __name__ + '.'+ self.__class__.__name__
        )
        self.logger.debug('Creating a new instance (name="{}", label="{}")'.format(name, label))

    def add(self,parent_id=0,content=""):
        self.logger.debug("Add page '{}'; label = [{}]".format(self.name, self.label))
        if content:
            self.content = content 
        self.parent_id = parent_id
        self.newPost = {"title":self.name,"content":self.content,"space":self.spaceKey,"parentId":str(self.parent_id)}
        self.post_to_wiki = self.server.confluence2.storePage(self.token,self.newPost)
        self.created_page = self.server.confluence2.getPage(self.token, self.spaceKey, self.name)
        self.page_url = self.created_page["url"]
        self.page_id = self.created_page["id"]
        if self.label:
            self.set_label()
        return {"url": self.page_url, "id": self.page_id}

    def update(self,content,parent_id=0):
        self.remove()
        self.parent_id = parent_id
        self.add(str(parent_id),content)

    def get(self):
        self.wanted_page = self.server.confluence2.getPage(self.token, self.spaceKey, self.name)
        return self.wanted_page

    def get_content(self):
        self.wanted_page_id = self.get_page_id
        self.content_values = {"style": "clean"}
        self.page_content = self.wanted_page = self.server.confluence2.renderContet(self.token, self.wanted_page_id,self.content_values)
        return self.page_content

    def get_id(self):
        return self.get()['id']

    def get_content(self):
        return self.get()['content']

    def remove(self):
        self.page = self.server.confluence2.getPage(self.token, self.spaceKey, self.name)
        self.server.confluence2.removePage(self.token, self.page["id"])

    def set_label(self):
        self.page_id = self.get_id()
        self.logger.debug("Set label '{}' on page {}".format(
            self.label, self.page_id))
        if not self.server.confluence2.addLabelByName(self.token, self.label, self.page_id):
            self.logger.debug("Unable to set label '{}' on page ID {}".format(
                self.label, self.page_id))

    def get_content(self):
        return self.get()['content']

    def get_version(self):
        return self.get()['version']
