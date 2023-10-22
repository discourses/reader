"""
Module arguments
"""
import argparse
import os

import dotmap
import requests
import yaml


class Arguments:
    """
    Class Arguments: Disaggregates the input argument
    """

    def __init__(self):
        """
        The constructor
        """

        self.root = os.getcwd()

    @staticmethod
    def url(urlstring: str) -> requests.models.Response:
        """
        Ascertains that the URL argument is valid

        :param urlstring: A URL string (to a YAML file)
        :return: The URL string if it is a valid URL, otherwise raise an error
        """

        try:
            req = requests.get(url=urlstring, timeout=180)
            req.raise_for_status()
        except requests.exceptions.RequestException as err:
            raise err

        return req

    @staticmethod
    def select(limit) -> int:
        """
        Ascertains that the optional --limit argument is valid

        :param limit: An optional text denoting the number of files to download

        :return: Integer denoting the number of files to download
        """
        if int(limit) <= 0:
            raise argparse.ArgumentTypeError("The argument '--select' must be a positive integer "
                                             "greater than or 0")
        return int(limit)

    @staticmethod
    def ascertain(var):
        """
        A few verification steps for the input YAML

        :param var:
        :return:
        """

        assert isinstance(var.source.rootURL, str)

        assert isinstance(var.source.metadataFileURL, str)
        try:
            req = requests.get(url=var.source.metadataFileURL,timeout=180)
            req.raise_for_status()
        except requests.exceptions.RequestException as err:
            raise err

        assert isinstance(var.source.fileStringsField, str)
        assert isinstance(var.source.fileStringsIncludeExt, bool)
        assert isinstance(var.source.archived, bool)

        if not var.source.fileStringsIncludeExt:
            assert var.source.ext is not None

    def parameters(self, elements: requests.models.Response):
        """
        :param elements: The content of the input YAML file
        :return: A dot map of the parameters in the YAML file; and supplementary parameters
        """

        text = yaml.safe_load(elements.text)
        var = dotmap.DotMap(text)

        # Minimal verification of the contents of the YAML
        self.ascertain(var)

        # For var.source.metadataFileURL
        var.kwargs = {'usecols': [var.source.fileStringsField], 'header': 0, 'encoding': 'UTF-8',
                      'dtype': {var.source.fileStringsField: 'str'}}

        # Hence, add default directories
        var.data = os.path.join(self.root, 'data')

        return var
