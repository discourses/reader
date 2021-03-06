"""
Module source
"""
import pandas as pd


class Source:
    """
    Class Source: Structures the metadata of a source
    """

    def __init__(self, var):
        """

        :param var: The dot map of parameters
        """
        self.var = var

    def read(self) -> pd.DataFrame:
        """
        Reads-in the metadata file

        data = dask.dataframe.read_csv(urlpath=self.var.source.metadataFileURL,
                                       **self.var.kwargs).repartition(npartitions=8)

        :return:
        """

        try:
            data = pd.read_csv(filepath_or_buffer=self.var.source.metadataFileURL, sep=',',
                               header=self.var.kwargs['header'], usecols=self.var.kwargs['usecols'],
                               encoding=self.var.kwargs['encoding'], dtype=self.var.kwargs['dtype'])
        except OSError as error:
            raise error

        return data

    def filestring(self, filename):
        """

        :param filename: The name of a file
        :return: A URL file string, including the file extension
        """

        if self.var.source.fileStringsIncludeExt:
            string = filename
        else:
            string = filename + self.var.source.ext

        return string

    def urlstring(self, filename):
        """

        :param filename: The name of a file
        :return: A URL file string, including the file extension
        """

        value = self.var.source.rootURL + filename

        if self.var.source.fileStringsIncludeExt:
            string = value
        else:
            string = value + self.var.source.ext

        return string

    def exc(self) -> pd.DataFrame:
        """

        :return: A DataFrame of URL & file strings; each includes file extensions
        """
        data = self.read()

        # Create the fields of interest via vectorised functions
        # https://kanoki.org/2020/02/24/parallelize-pandas-apply-using-dask-and-swifter/
        data['urlstring'] = self.urlstring(data[self.var.source.fileStringsField])
        data['filestring'] = self.filestring(data[self.var.source.fileStringsField])

        return data
