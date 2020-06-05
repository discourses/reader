import os
import urllib.request


class Retrieve:

    def __init__(self, var):
        self.var = var
        self.r = urllib.request

    def exc(self, urlstring, filestring):
        self.r.urlretrieve(urlstring, os.path.join(self.var.data, filestring))
