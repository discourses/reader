import pytest

import src.io.arguments


class TestArguments:

    @pytest.fixture
    def arguments(self):
        return src.io.arguments.Arguments()

    @pytest.fixture()
    def urlstring(self):
        return 'https://raw.githubusercontent.com/greyhypotheses/dictionaries/develop/readerpython/parameters.yml'

    def test_url(self, urlstring, arguments):
        req = arguments.url(urlstring)
        assert req.status_code == 200, "The input YAML mut be a valid URL string"

    def test_parameters(self, urlstring, arguments):
        req = arguments.url(urlstring)
        var = arguments.parameters(req)

        assert isinstance(var.kwargs, dict), "A dictionary of parameters is required for reading the metadata file"
        assert isinstance(var.data, str), "A directory name is required for the downloaded files"
