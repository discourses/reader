import pytest
import pandas
import random
import requests
import pathlib

import src.io.arguments
import src.io.source

import src.read.interface


class TestInterface:

    @pytest.fixture()
    def var(self):
        arguments = src.io.arguments.Arguments()
        urlstring = 'https://raw.githubusercontent.com/greyhypotheses/dictionaries/develop/readerpython/parameters.yml'

        req = arguments.url(urlstring)
        return arguments.parameters(req)

    @pytest.fixture()
    def metadata(self, var) -> pandas.DataFrame:
        source = src.io.source.Source(var=var)
        return source.exc()

    @pytest.fixture()
    def interface(self, var):
        return src.read.interface.Interface(var=var)

    def test_iterables(self, interface, metadata):
        urlstrings, filestrings = interface.iterables(metadata=metadata)

        assert isinstance(urlstrings, list)
        assert isinstance(filestrings, list)

    def test_exc(self, interface, metadata):
        urlstrings, filestrings = interface.iterables(metadata=metadata)

        i = random.randrange(start=0, stop=len(urlstrings))

        # urlstrings
        try:
            req = requests.get(urlstrings[i])
            assert req.status_code == 200
        except requests.exceptions.RequestException as e:
            raise e

        # filestrings
        extension = pathlib.Path(filestrings[i]).suffix
        assert extension.__len__() != 0




