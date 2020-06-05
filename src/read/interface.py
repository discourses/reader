import multiprocessing as mp

import src.read.dearchive
import src.read.retrieve


class Interface:

    def __init__(self, var):
        self.var = var
        self.dearchive = src.read.dearchive.Dearchive(self.var)
        self.retrieve = src.read.retrieve.Retrieve(self.var)
        self.pool = mp.Pool(mp.cpu_count())

    @staticmethod
    def iterables(metadata):

        urlstrings = [{i} for i in metadata.urlstring.to_list()]
        filestrings = [{i} for i in metadata.filestring.to_list()]

        return urlstrings, filestrings

    def exc(self, metadata):

        urlstrings, filestrings = self.iterables(metadata=metadata)

        if self.var.source.archived:
            {
                '.zip': self.pool.starmap(self.dearchive.unzip, [i for i in urlstrings])
            }.get(self.var.source.ext, LookupError('Unknown extension'))
        else:
            self.pool.starmap(self.retrieve.exc, [(i, j) for (i, j) in zip(urlstrings, filestrings)])
