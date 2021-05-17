from core.bc0 import bytecode_format
from logger import info


def format_to_bytecode(x: str):
    """
    Call the core function bytecode_format and print the value
    :param x:
    :return:
    """
    to_plug = int(x) if x.find("0x") == -1 else int(x, 16)
    value = bytecode_format(to_plug)
    info(f'{x} into micropy bcf: {value}')
