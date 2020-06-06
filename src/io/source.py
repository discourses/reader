import dask.dataframe as dd


class Source:

    def __init__(self, var):
        self.name = ''
        self.var = var

    def read(self) -> dd.DataFrame:
        """
        Reads-in the metadata file
        :return:
        """

        try:
            data = dd.read_csv(urlpath=self.var.source.metadataFileURL,
                               **self.var.kwargs).repartition(npartitions=8)
        except OSError as error:
            raise error

        return data

    def filestring(self, filename):
        """

        :param filename: The name of a file
        :return: A URL file string, including the file extension
        """

        if self.var.source.fileStringsIncludeExt:
            return filename
        else:
            return filename + self.var.source.ext

    def urlstring(self, filename):
        """

        :param filename: The name of a file
        :return: A URL file string, including the file extension
        """

        value = self.var.source.rootURL + filename

        if self.var.source.fileStringsIncludeExt:
            return value
        else:
            return value + self.var.source.ext

    def exc(self):
        """

        :return: A DataFrame of URL & file strings; each includes file extensions
        """
        data = self.read()

        # Create the fields of interest via vectorised functions
        # https://kanoki.org/2020/02/24/parallelize-pandas-apply-using-dask-and-swifter/
        data['urlstring'] = self.urlstring(data[self.var.source.fileStringsField])
        data['filestring'] = self.filestring(data[self.var.source.fileStringsField])

        # Hence
        return data.compute(scheduler='processes')
