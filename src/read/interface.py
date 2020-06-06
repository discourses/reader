import multiprocessing as mp

import pandas

import src.read.dearchive
import src.read.retrieve


class Interface:

    def __init__(self, var):
        """
        The constructor
        :param var: The dot map of parameters
        """
        self.var = var

        # Instances of dearchive & retrieve
        self.dearchive = src.read.dearchive.Dearchive(self.var)
        self.retrieve = src.read.retrieve.Retrieve(self.var)

        # Parallel processing anchor
        self.pool = mp.Pool(mp.cpu_count())

    @staticmethod
    def iterables(metadata: pandas.DataFrame) -> (list, list):
        """

        :param metadata: A dataframe that includes a field of url strings
                         and file name strings; each must include a file extension.
        :return:
        """

        urlstrings = [{i} for i in metadata.urlstring.to_list()]
        filestrings = [{i} for i in metadata.filestring.to_list()]

        return urlstrings, filestrings

    def exc(self, metadata: pandas.DataFrame) -> None:
        """

        :param metadata: A dataframe that includes a field of url strings
                         and file name strings; each must include a file extension.
        :return:
        """

        urlstrings, filestrings = self.iterables(metadata=metadata)

        print('Download step starting ...')

        # This set-up makes it easy to consider other types of archived files over time
        if self.var.source.archived:
            {
                '.zip': self.pool.starmap(self.dearchive.unzip, [i for i in urlstrings])
            }.get(self.var.source.ext, LookupError('Unknown extension'))
        else:
            self.pool.starmap(self.retrieve.exc, [(i, j) for (i, j) in zip(urlstrings, filestrings)])

        print('Download step ended')
