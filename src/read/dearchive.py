import requests
import zipfile
import io


class Dearchive:

    def __init__(self, var):
        """
        The constructor

        :param var: Dot map of ...
        """

        self.var = var

    @staticmethod
    def read(urlstring: str) -> bytes:
        """

        :param urlstring: The URL of the archived file that would be de-archived locally
        :return: The file contents, in byte form
        """

        try:
            req = requests.get(url=urlstring)
            req.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise e

        return req.content

    def unzip(self, urlstring: str):
        """
        De-archives a zip archive file
        :param urlstring:
        :return:
        """

        obj = zipfile.ZipFile(io.BytesIO(self.read(urlstring=urlstring)))
        obj.extractall(path=self.var.data)
