from core.bc0 import bytecode_format
from logger import info


def format_to_bytecode(x: int):
    """
    Call the core function bytecode_format and print the value
    :param x:
    :return:
    """
    value = bytecode_format(x)
    info(f'{x} into micropy bcf: {value}')
