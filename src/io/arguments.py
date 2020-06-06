import requests
import yaml
import dotmap
import os


class Arguments:

    def __init__(self):
        """
        The constructor
        """

        self.root = os.getcwd()

    @staticmethod
    def url(urlstring: str):
        """
        Ascertains that the URL argument is valid

        :param urlstring: A URL string (to a YAML file)
        :return: The URL string if it is a valid URL, otherwise raise an error
        """

        try:
            req = requests.get(url=urlstring)
            req.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise e

        return urlstring

    @staticmethod
    def ascertain(var):
        """
        A few verification steps for the input YAML

        :param var:
        :return:
        """

        assert isinstance(var.source.rootURL, str)
        assert isinstance(var.source.metadataFileURL, str)
        assert isinstance(var.source.fileStringsField, str)
        assert isinstance(var.source.fileStringsIncludeExt, bool)
        assert isinstance(var.source.archived, bool)

        if not var.source.fileStringsIncludeExt:
            assert var.source.ext is not None

    def parameters(self, urlstring: str):
        """
        Reads and structures the contents of the file that urlstring links to

        :param urlstring: A URL string (to a YAML file)
        :return: The dot map of the contents of the YAML file
        """

        req = requests.get(url=urlstring)
        text = yaml.safe_load(req.text)
        var = dotmap.DotMap(text)

        # Minimal verification of the contents of the YAML
        self.ascertain(var)

        # For var.source.metadataFileURL
        var.kwargs = {'usecols': [var.source.fileStringsField], 'header': 0, 'encoding': 'UTF-8',
                      'dtype': {var.source.fileStringsField: 'str'}}

        # Hence, add default directories
        var.data = os.path.join(self.root, 'data')

        return var
