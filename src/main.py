import argparse
import os
import sys


def main():
    # Instances
    arguments = src.io.arguments.Arguments()

    # Parse the package's input
    parser = argparse.ArgumentParser()
    parser.add_argument('urlstring',
                        type=arguments.url,
                        help='The URL of a YAML of parameters; refer to the README notes.')
    args = parser.parse_args()

    # Get the data parameters encoded by the input
    var = arguments.parameters(urlstring=args.urlstring)

    # Prepare directories
    src.io.directories.Directories(var=var).exc()

    # Read-in the metadata of files that would be downloaded
    metadata = src.io.source.Source(var=var).exc()

    # Unload
    src.read.interface.Interface(var=var).exc(metadata=metadata)


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(os.path.join(root))
    sys.path.append(os.path.join(root, 'src'))
    import src.io.arguments
    import src.io.directories
    import src.io.source
    import src.read.interface
    main()
