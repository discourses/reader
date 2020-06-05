import os


class Config:

    def __init__(self):
        # Root
        self.root = os.path.abspath(__package__)
