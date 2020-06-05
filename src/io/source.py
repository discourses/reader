import dask.dataframe as dd


class Source:

    def __init__(self, var):
        self.name = ''
        self.var = var

    def read(self):
        return dd.read_csv(urlpath=self.var.source.metadataFileURL,
                           **self.var.kwargs).repartition(npartitions=8)

    def filestring(self, filename):

        if self.var.source.fileStringsIncludeExt:
            return filename
        else:
            return filename + self.var.source.ext

    def urlstring(self, filename):

        value = self.var.source.sourceURL + filename

        if self.var.source.fileStringsIncludeExt:
            return value
        else:
            return value + self.var.source.ext

    def exc(self):
        data = self.read()
        data['urlstring'] = self.urlstring(data.filename)
        data['filestring'] = self.filestring(data.filename)
        return data.compute(scheduler='processes')
