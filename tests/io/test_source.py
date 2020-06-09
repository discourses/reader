import pytest

import pandas

import src.io.arguments
import src.io.source

class TestSource:

    @pytest.fixture()
    def var(self):
        arguments = src.io.arguments.Arguments()
        urlstring = 'https://raw.githubusercontent.com/greyhypotheses/dictionaries/develop/readerpython/parameters.yml'

        req = arguments.url(urlstring)
        return arguments.parameters(req)

    @pytest.fixture()
    def source(self, var):
        return src.io.source.Source(var=var)

    def test_read(self, source):
        metadata: pandas.DataFrame = source.read()

        assert not metadata.empty, "The metadata file of the data source should not be empty."
        assert metadata.shape[1] == 1, "The number of fields should be 1; the field of file names."

    def test_exc(self, source):
        metadata: pandas.DataFrame = source.exc()

        assert 'urlstring' in metadata.columns, "The field of URL strings is missing in the metadata data frame."
        assert 'filestring' in metadata.columns, "The field of file name strings is missing in the metadata data frame."

