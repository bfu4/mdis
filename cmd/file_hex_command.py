from logger import info
from reader import dump_file_hex


def file_hex(file):
    """
    Call the core function bytecode_format and print the value
    :param file: file to dump hex
    :return:
    """
    hex = dump_file_hex(file)
    info(f'hex: {hex}')
