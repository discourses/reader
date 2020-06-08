import os


class Directories:
    """
    Class Directories: Preparing directories
    """

    def __init__(self, var):
        """
        The constructor

        :param var: A dot map of parameters
        """

        self.var = var

    def cleanup(self):
        """
        Clears the directories for archived & de-archived data

        :return: None
        """

        # Foremost, delete files
        for path in [self.var.data]:
            files_ = [os.remove(os.path.join(base, file))
                      for base, _, files in os.walk(path) for file in files]

            if any(files_):
                raise Exception('Unable to delete all files within path {}'.format(path))

        # ... then, directories
        for path in [self.var.data]:
            directories_ = [os.removedirs(os.path.join(base, directory))
                            for base, directories, _ in os.walk(path, topdown=False) for directory in directories
                            if os.path.exists(os.path.join(base, directory))]

            if any(directories_):
                raise Exception('Unable to delete all directories within path {}'.format(path))

    def paths(self):
        """
        Creates directories for (a) archived files, (b) de-archived files

        :return: None
        """

        for path in [self.var.data]:
            if not os.path.exists(path):
                os.makedirs(path)

    def exc(self):
        """
        Entry point
        :return:
        """

        self.cleanup()
        self.paths()
