import os
import urllib.request


class Retrieve:

    def __init__(self, var):
        self.var = var

    def exc(self, urlstring, filestring):
        urllib.request.urlretrieve(urlstring, os.path.join(self.var.data, filestring))
