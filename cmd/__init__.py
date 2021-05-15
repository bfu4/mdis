from .parser import *


def call_command(command, _args):
    """
    Call the given command with arguments
    :param command: command
    :param _args: arguments
    :return:
    """
    find(command)(_args)


def find(switch):
    """
    Iterate through commands to find the correct command to call
    :param switch: name of the command
    :return: method reference
    """
    for arg in args:
        if switch in arg[0]:
            return arg[3]
