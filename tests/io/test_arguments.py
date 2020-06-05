import pytest

import src.io.arguments

arg = src.io.arguments.Arguments()


class TestArguments:

    @pytest.fixture
    def arguments(self):
        return src.io.arguments.Arguments()

    @pytest.fixture()
    def urlstring(self):
        return 'https://raw.githubusercontent.com/greyhypotheses/dictionaries/develop/readerpython/parameters.yml'

    def test_url(self, urlstring, arguments):
        string = arguments.url(urlstring)
        assert string is not None

    def test_parameters(self, urlstring, arguments):
        var = arguments.parameters(urlstring)
        assert isinstance(var.source.sourceURL, str)
        assert isinstance(var.source.archived, bool)
