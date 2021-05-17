import argparse

# borrowed usage from @netspooky/inhale
from cmd.bytecode_format_command import format_to_bytecode
from cmd.instruction_command import get_instr
from cmd.opcode_command import get_op

parser = argparse.ArgumentParser(description="mdis.py")

args = [
    ('-b', "INT_TO_BC", "shift into bytecode format", format_to_bytecode, 1),
    ('-f', "FILE", "get instructions of a given file", get_instr, 1),
    ('-op', "INT_TO_OP", "get opcode of a given integer", get_op, 1),
    ('-fr', "FROM", "from address", None, 1),
    ('-t', "TO", "to address", None, 1)
]


def set_up_arguments():
    """
    Set up the arguments
    :return:
    """
    for arg in args:
        add_argument(arg[0], arg[1], arg[2], arg[4])


def add_argument(flag: str, dest, _help: str, nargs: int):
    """
    Add an argument
    :param nargs: number of arguments
    :param flag: argument flag
    :param dest: destination
    :param _help: help message
    :return:
    """
    parser.add_argument(flag, dest=dest, nargs=nargs, help=_help)
