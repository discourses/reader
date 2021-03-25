import os


class Config:

    # noinspection SpellCheckingInspection
    def __init__(self):

        # Root
        self.root = os.path.abspath(__package__)

        # URL
        self.urlstring = 'https://raw.githubusercontent.com/discourses/reader/' \
                         'develop/resources/augmentations.yml'
