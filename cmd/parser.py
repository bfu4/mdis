import argparse

# borrowed usage from @netspooky/inhale
from cmd.bytecode_format_command import format_to_bytecode
from cmd.file_hex_command import file_hex

parser = argparse.ArgumentParser(description="mdis.py")

args = [
    ('-bytecode-format, -bcf', "int", "shift into bytecode format", format_to_bytecode),
    ('-file-hex, -fhx', "file", "get hex of a given file", file_hex)
]


def set_up_arguments():
    """
    Set up the arguments
    :return:
    """
    for arg in args:
        add_argument(arg[0], arg[1], arg[2])


def add_argument(flag: str, dest: str, _help: str):
    """
    Add an argument
    :param flag: argument flag
    :param dest: destination
    :param _help: help message
    :return:
    """
    parser.add_argument(flag, dest=dest, help=_help)
