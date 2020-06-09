"""
Module main
"""
import argparse
import os
import sys


def main():
    """
    The entry point of te readerpython package.  It expects a single argument; the URL to a YAML. The
    YAML must hve the structure outlined in
        https://github.com/greyhypotheses/dictionaries/blob/master/readerpython/parameters.yml
    More notes at
        https://github.com/greyhypotheses/readerpython

    :return:
    """
    # Instances
    arguments = src.io.arguments.Arguments()

    # Parse the package's input
    parser = argparse.ArgumentParser()
    parser.add_argument('elements',
                        type=arguments.url,
                        help='The URL of a YAML of parameters; refer to the README notes.  The argument '
                             'parser returns a blob of elements')
    parser.add_argument('--limit',
                        type=arguments.select,
                        help='An optional integer that downloads the number of files requested rather '
                             'than all files')
    args = parser.parse_args()

    # Get the data parameters encoded by the input
    var = arguments.parameters(elements=args.elements)

    # Prepare directories
    src.io.directories.Directories(var=var).exc()

    # Read-in the metadata of files that would be downloaded
    metadata = src.io.source.Source(var=var).exc()

    # Unload: Beware of metadata.loc[:4], switch back to metadata after testing period.
    limit = metadata.shape[0] if not isinstance(args.limit, int) else args.limit

    if limit >= metadata.shape[0]:
        nfiles = metadata.shape[0]
    else:
        nfiles = args.limit

    # Hence
    src.read.interface.Interface(var=var).exc(metadata=metadata.loc[:nfiles])


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(os.path.join(root))
    sys.path.append(os.path.join(root, 'src'))
    import src.io.arguments
    import src.io.directories
    import src.io.source
    import src.read.interface

    main()
