import termcolor

from core import get_opcode, get_op_value
from typing import List, Tuple


def wrap_parsed_set(parsed: str) -> List[str]:
    return parsed.split("\n")


def parse_instruction_set(_bytes: List[str]) -> str:
    """
    Recursively parse an instruction from bytes
    :param _bytes: bytes to parse
    :return: instruction set
    """
    instr = ""
    needs_string = False
    last_byte = 0x00
    for byte in _bytes:
        _hex = int(str("0x" + byte), 16)
        op = get_opcode(_hex)
        if op is not None:
            tip = termcolor.colored(f'(0x{byte})', on_color="on_magenta")
            instr += f'\n{tip} {op}'
            if _hex == 16:
                needs_string = True
                last_byte = byte
                break
        else:
            instr += f'\u0020{byte}'
    if needs_string:
        last_byte, instr = get_string_from_ops(_bytes, last_byte, instr)
        index = _bytes.index(last_byte)
        instr += parse_instruction_set(_bytes[index + 1:])

    return instr


def get_string_from_ops(_bytes, last_byte, instr) -> Tuple[str, str]:
    """
    Get a string from opcode bytes
    :param _bytes:
    :param last_byte:
    :param instr:
    :return:
    """
    index = _bytes.index(last_byte)
    _hex = int(str("0x" + _bytes[index]), 16)
    op = get_opcode(_hex)
    op_value = get_op_value(op)
    ctx = index + 1
    # todo validity, this is a cheat, should remove for other validity
    while op_value != 0x00 and 0x4b >= op_value >= 0x40 and ctx < len(_bytes):
        instr += f'\u0020{_bytes[ctx]}'
        last_byte = _bytes[ctx]
        ctx += 1
        if ctx + 1 < len(_bytes):
            _hex = int(str("0x" + _bytes[ctx]), 16)
            op = get_opcode(_hex)
            op_value = get_op_value(op)
    return last_byte, instr
