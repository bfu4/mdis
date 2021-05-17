from core import Translator
from logger import err, info


def get_instr(args):
    """
    Get instructions for file with given arguments
    :param args: arguments
    :return: none, prints respectively
    """
    # Weird list parsing
    _len = calculate_real_len(args)
    if _len == 3:
        if args[1] is not None and args[2] is not None:
            get_instr_s(*args)
    elif _len == 1:
        get_instr_a(args[0])
    else:
        err(f'Invalid arguments! Given: {args}')


def get_instr_a(file):
    """
    Get all instructions of a file
    :param file: file
    :return: none
    """
    # Weird list parsing
    translator = Translator(file[0])
    # todo: buggy
    instr = translator.get_instruction_set()
    # Should never be none
    if instr is not None:
        for line in instr:
            info(line)


def get_instr_s(file, from_loc, to_loc):
    """
    Get instructions with location
    :param file: file
    :param from_loc: start
    :param to_loc: end
    :return: none
    """
    # Weird list parsing
    translator = Translator(file[0])
    instr = translator.get_instructions_at(from_loc[0], to_loc[0])
    # Should never be none
    if instr is not None:
        for line in instr:
            info(line)


def calculate_real_len(args):
    """
    Calculate the real length of supplied arguments
    :param args: args
    :return: real length
    """
    i = 0
    for arg in args:
        if arg is not None:
            i += 1
    return i
