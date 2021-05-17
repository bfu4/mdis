import termcolor

from codecs import decode
from core import get_opcode, get_op_value
from typing import List, Tuple

from core.bc0 import requires_extra_byte, bytecode_format, MP_BC_FORMAT_QSTR, MP_BC_MASK_EXTRA_BYTE, \
    MP_BC_FORMAT_VAR_UINT, MP_BC_FORMAT_OFFSET, valid_operation, is_call_function


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
            if requires_extra_byte(get_op_value(op)):
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


def opcode_format(last_byte, count_var_uint: bool) -> Tuple[int, int]:
    """
    Python implementation of https://github.com/micropython/micropython/blob/47e6c52f0c2bf058c5d099dd2993192e0978e172/py/bc.c#L313
    :param last_byte: last byte (ip)
    :param op_size: size of op
    :param count_var_uint: should we could varuint
    :return: opcode format
    """
    # TODO: (@bfu4) this is probably wrong, should learn more about what this does and lack of ptr..
    f = bytecode_format(last_byte)
    ip_start = last_byte
    # avoid modifying original value
    ip = last_byte
    if f == MP_BC_FORMAT_QSTR:
        if requires_extra_byte(last_byte):
            ip += 1
        ip += 3
    else:
        extra_byte = (ip & MP_BC_MASK_EXTRA_BYTE) == 0
        ip += 1

        def incr(val: int):
            val += 1

        if f == MP_BC_FORMAT_VAR_UINT:
            if count_var_uint:
                # while ((ip++) & 0x80) != 0) {}
                while (ip & 0x80) != 0:
                    incr(ip)
        elif f == MP_BC_FORMAT_OFFSET:
            ip += 2
        ip += extra_byte
    op_size = ip - ip_start
    return f, op_size


def get_string_from_ops(_bytes, last_byte, instr) -> Tuple[str, str]:
    """
    Get a string from opcode bytes
    :param _bytes:
    :param last_byte:
    :param instr:
    :return:
    """
    index = _bytes.index(last_byte)
    has_entered = False
    _hex = int(str("0x" + _bytes[index + 1]), 16)
    op = get_opcode(_hex)
    op_value = get_op_value(op)
    ctx = index + 1
    def is_ascii(byte: str): return 126 >= int(str("0x" + byte), 16) >= 32
    # todo validity, this is a cheat, should remove for other validity
    while (op is None or op_value > 0x20) \
            and not is_call_function(op_value) \
            or (not has_entered and op_value == 0x0) \
            and ctx < len(_bytes):
        to_add = ""
        if not has_entered:
            to_add = "\u0020"
        to_add += decode(_bytes[ctx], "hex").decode("utf-8") if is_ascii(_bytes[ctx]) else _bytes[ctx] + "\u0020"
        instr += f'{to_add}'
        has_entered = True
        last_byte = _bytes[ctx]
        ctx += 1
        if ctx + 1 < len(_bytes):
            _hex = int(str("0x" + _bytes[ctx]), 16)
            op = get_opcode(_hex)
            op_value = get_op_value(op)
    return last_byte, instr
