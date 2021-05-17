from core import Translator
from logger import err, info


def get_instr(args):
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
    # Weird list parsing
    translator = Translator(file[0])
    # todo: buggy
    instr = translator.get_instruction_set()
    # Should never be none
    if instr is not None:
        for line in instr:
            info(line)


def get_instr_s(file, from_loc, to_loc):
    # Weird list parsing
    translator = Translator(file[0])
    instr = translator.get_instructions_at(from_loc[0], to_loc[0])
    # Should never be none
    if instr is not None:
        for line in instr:
            info(line)


def calculate_real_len(args):
    i = 0
    for arg in args:
        if arg is not None:
            i += 1
    return i
