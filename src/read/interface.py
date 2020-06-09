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

    @staticmethod
    def iterables(metadata: pandas.DataFrame) -> (list, list):
        """

        :param metadata: A dataframe that includes a field of url strings
                         and file name strings; each must include a file extension.
        :return:
        """

        urlstrings = metadata.urlstring.to_list()
        filestrings = metadata.filestring.to_list()

        return urlstrings, filestrings

    def exc(self, metadata: pandas.DataFrame) -> None:
        """
        Slow:
            '.zip': self.pool.starmap(self.dearchive.unzip, [{i} for i in urlstrings])
            self.pool.starmap(self.retrieve.exc, zip(urlstrings, filestrings))

        :param metadata: A dataframe that includes a field of url strings
                         and file name strings; each must include a file extension.
        :return:
        """

        urlstrings, filestrings = self.iterables(metadata=metadata)

        print('Download starting ...')

        # Parallel processing anchor
        pool = mp.Pool(mp.cpu_count())

        # This set-up makes it easy to consider other types of archived files over time
        if self.var.source.archived:
            {
                '.zip': pool.map_async(self.dearchive.unzip, urlstrings).get()
            }.get(self.var.source.ext, LookupError('Unknown extension'))

        else:
            pool.starmap_async(self.retrieve.exc, zip(urlstrings, filestrings)).get()

        # Close
        pool.close()

        print('Download finished')
