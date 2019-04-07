# standard imports
import argparse


def cli():
    """ Defines and parses the command line arguments.

    Parameters:
        None

    Returns:
        args (obj): parsed arguments.
    """

    # create parser
    parser = argparse.ArgumentParser(
        description="Find nearest neighbors."
    )

    # define arguments
    parser.add_argument("origin",
                        action="store",
                        help="origin point.")
    parser.add_argument("-n", "--number",
                        action="store",
                        help="number of nearest neighbors to find.")
    parser.add_argument("neighbors",
                        action="store",
                        help="path to neighbors file.")
    parser.add_argument("-v", "--version",
                        action="version",
                        version="0.0.1",
                        help="display the version")

    # parse arguments
    args = parser.parse_args()

    return args
