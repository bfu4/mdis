"""
This file is adapted from MicroPython's bc0.h

https://github.com/micropython/micropython/blob/master/py/bc0.h
"""
from core import switch, Case

MP_BC_MASK_FORMAT = 0xf0
MP_BC_MASK_EXTRA_BYTE = 0x9e

MP_BC_FORMAT_BYTE = 0
MP_BC_FORMAT_QSTR = 1
MP_BC_FORMAT_VAR_UINT = 2
MP_BC_FORMAT_OFFSET = 3


# Nibbles in magic number are: BB BB BB BB BB BO VV QU
def bytecode_format(op: int):
    return (0x000003a4 >> (2 * (op >> 4))) & 3


# Load, Store, Delete, Import, Make, Build, Unpack, Call, Jump, Exception, For, sTack, Return, Yield, Op
MP_BC_BASE_RESERVED = 0x00  # ----------------
MP_BC_BASE_QSTR_O = 0x10  # LLLLLLSSSDDII---
MP_BC_BASE_VINT_E = 0x20  # MMLLLLSSDDBBBBBB
MP_BC_BASE_VINT_O = 0x30  # UUMMCCCC--------
MP_BC_BASE_JUMP_E = 0x40  # J-JJJJJEEEEF----
MP_BC_BASE_BYTE_O = 0x50  # LLLLSSDTTTTTEEFF
MP_BC_BASE_BYTE_E = 0x60  # --BREEEYYI------
MP_BC_LOAD_CONST_SMALL_INT_MULTI = 0x70  # LLLLLLLLLLLLLLLL

"""
 (0x80) # LLLLLLLLLLLLLLLL
 (0x90) # LLLLLLLLLLLLLLLL
 (0xa0) # LLLLLLLLLLLLLLLL
"""

MP_BC_LOAD_FAST_MULTI = 0xb0  # LLLLLLLLLLLLLLLL
MP_BC_STORE_FAST_MULTI = 0xc0  # SSSSSSSSSSSSSSSS
MP_BC_UNARY_OP_MULTI = 0xd0  # OOOOOOO
MP_BC_BINARY_OP_MULTI = 0xd7  # OOOOOOOOO

#                                          (0xe0) # OOOOOOOOOOOOOOOO
#                                          (0xf0) # OOOOOOOOOO------

MP_BC_LOAD_CONST_SMALL_INT_MULTI_NUM = 64
MP_BC_LOAD_CONST_SMALL_INT_MULTI_EXCESS = 16
MP_BC_LOAD_FAST_MULTI_NUM = 16
MP_BC_STORE_FAST_MULTI_NUM = 16
MP_BC_UNARY_OP_MULTI_NUM = MP_BC_UNARY_OP_MULTI
MP_BC_BINARY_OP_MULTI_NUM = MP_BC_BINARY_OP_MULTI

MP_BC_LOAD_CONST_FALSE = (MP_BC_BASE_BYTE_O + 0x00)
MP_BC_LOAD_CONST_NONE = (MP_BC_BASE_BYTE_O + 0x01)
MP_BC_LOAD_CONST_TRUE = (MP_BC_BASE_BYTE_O + 0x02)
MP_BC_LOAD_CONST_SMALL_INT = (MP_BC_BASE_VINT_E + 0x02)  # signed var - int
MP_BC_LOAD_CONST_STRING = (MP_BC_BASE_QSTR_O + 0x00)  # qstr
MP_BC_LOAD_CONST_OBJ = (MP_BC_BASE_VINT_E + 0x03)  # ptr
MP_BC_LOAD_NULL = (MP_BC_BASE_BYTE_O + 0x03)

MP_BC_LOAD_FAST_N = (MP_BC_BASE_VINT_E + 0x04)  # uint
MP_BC_LOAD_DEREF = (MP_BC_BASE_VINT_E + 0x05)  # uint
MP_BC_LOAD_NAME = (MP_BC_BASE_QSTR_O + 0x01)  # qstr
MP_BC_LOAD_GLOBAL = (MP_BC_BASE_QSTR_O + 0x02)  # qstr
MP_BC_LOAD_ATTR = (MP_BC_BASE_QSTR_O + 0x03)  # qstr
MP_BC_LOAD_METHOD = (MP_BC_BASE_QSTR_O + 0x04)  # qstr
MP_BC_LOAD_SUPER_METHOD = (MP_BC_BASE_QSTR_O + 0x05)  # qstr
MP_BC_LOAD_BUILD_CLASS = (MP_BC_BASE_BYTE_O + 0x04)
MP_BC_LOAD_SUBSCR = (MP_BC_BASE_BYTE_O + 0x05)

MP_BC_STORE_FAST_N = (MP_BC_BASE_VINT_E + 0x06)  # uint
MP_BC_STORE_DEREF = (MP_BC_BASE_VINT_E + 0x07)  # uint
MP_BC_STORE_NAME = (MP_BC_BASE_QSTR_O + 0x06)  # qstr
MP_BC_STORE_GLOBAL = (MP_BC_BASE_QSTR_O + 0x07)  # qstr
MP_BC_STORE_ATTR = (MP_BC_BASE_QSTR_O + 0x08)  # qstr
MP_BC_STORE_SUBSCR = (MP_BC_BASE_BYTE_O + 0x06)

MP_BC_DELETE_FAST = (MP_BC_BASE_VINT_E + 0x08)  # uint
MP_BC_DELETE_DEREF = (MP_BC_BASE_VINT_E + 0x09)  # uint
MP_BC_DELETE_NAME = (MP_BC_BASE_QSTR_O + 0x09)  # qstr
MP_BC_DELETE_GLOBAL = (MP_BC_BASE_QSTR_O + 0x0a)  # qstr

MP_BC_DUP_TOP = (MP_BC_BASE_BYTE_O + 0x07)
MP_BC_DUP_TOP_TWO = (MP_BC_BASE_BYTE_O + 0x08)
MP_BC_POP_TOP = (MP_BC_BASE_BYTE_O + 0x09)
MP_BC_ROT_TWO = (MP_BC_BASE_BYTE_O + 0x0a)
MP_BC_ROT_THREE = (MP_BC_BASE_BYTE_O + 0x0b)

MP_BC_JUMP = (MP_BC_BASE_JUMP_E + 0x02)  # rel bytecode offset, 16 - bit signed, in excess

MP_BC_POP_JUMP_IF_TRUE = (MP_BC_BASE_JUMP_E + 0x03)  # rel bytecode offset, 16 - bit signed, in excess
MP_BC_POP_JUMP_IF_FALSE = (MP_BC_BASE_JUMP_E + 0x04)  # rel bytecode offset, 16 - bit signed, in excess

MP_BC_JUMP_IF_TRUE_OR_POP = (MP_BC_BASE_JUMP_E + 0x05)  # rel bytecode offset, 16 - bit signed, in excess
MP_BC_JUMP_IF_FALSE_OR_POP = (MP_BC_BASE_JUMP_E + 0x06)  # rel bytecode offset, 16 - bit signed, in excess

MP_BC_UNWIND_JUMP = (MP_BC_BASE_JUMP_E + 0x00)  # rel bytecode offset, 16 - bit signed, in excess; then a byte

MP_BC_SETUP_WITH = (MP_BC_BASE_JUMP_E + 0x07)  # rel bytecode offset, 16 - bit unsigned
MP_BC_SETUP_EXCEPT = (MP_BC_BASE_JUMP_E + 0x08)  # rel bytecode offset, 16 - bit unsigned
MP_BC_SETUP_FINALLY = (MP_BC_BASE_JUMP_E + 0x09)  # rel bytecode offset, 16 - bit unsigned

MP_BC_POP_EXCEPT_JUMP = (MP_BC_BASE_JUMP_E + 0x0a)  # rel bytecode offset, 16 - bit unsigned

MP_BC_FOR_ITER = (MP_BC_BASE_JUMP_E + 0x0b)  # rel bytecode offset, 16 - bit unsigned
MP_BC_WITH_CLEANUP = (MP_BC_BASE_BYTE_O + 0x0c)
MP_BC_END_FINALLY = (MP_BC_BASE_BYTE_O + 0x0d)

MP_BC_GET_ITER = (MP_BC_BASE_BYTE_O + 0x0e)
MP_BC_GET_ITER_STACK = (MP_BC_BASE_BYTE_O + 0x0f)

MP_BC_BUILD_TUPLE = (MP_BC_BASE_VINT_E + 0x0a)  # uint
MP_BC_BUILD_LIST = (MP_BC_BASE_VINT_E + 0x0b)  # uint

MP_BC_BUILD_MAP = (MP_BC_BASE_VINT_E + 0x0c)  # uint
MP_BC_STORE_MAP = (MP_BC_BASE_BYTE_E + 0x02)

MP_BC_BUILD_SET = (MP_BC_BASE_VINT_E + 0x0d)  # uint
MP_BC_BUILD_SLICE = (MP_BC_BASE_VINT_E + 0x0e)  # uint

MP_BC_STORE_COMP = (MP_BC_BASE_VINT_E + 0x0f)  # uint

MP_BC_UNPACK_SEQUENCE = (MP_BC_BASE_VINT_O + 0x00)  # uint
MP_BC_UNPACK_EX = (MP_BC_BASE_VINT_O + 0x01)  # uint

MP_BC_RETURN_VALUE = (MP_BC_BASE_BYTE_E + 0x03)

MP_BC_RAISE_LAST = (MP_BC_BASE_BYTE_E + 0x04)
MP_BC_RAISE_OBJ = (MP_BC_BASE_BYTE_E + 0x05)
MP_BC_RAISE_FROM = (MP_BC_BASE_BYTE_E + 0x06)

MP_BC_YIELD_VALUE = (MP_BC_BASE_BYTE_E + 0x07)
MP_BC_YIELD_FROM = (MP_BC_BASE_BYTE_E + 0x08)

MP_BC_MAKE_FUNCTION = (MP_BC_BASE_VINT_O + 0x02)  # uint
MP_BC_MAKE_FUNCTION_DEFARGS = (MP_BC_BASE_VINT_O + 0x03)  # uint

MP_BC_MAKE_CLOSURE = (MP_BC_BASE_VINT_E + 0x00)  # uint; extra byte
MP_BC_MAKE_CLOSURE_DEFARGS = (MP_BC_BASE_VINT_E + 0x01)  # uint; extra byte

MP_BC_CALL_FUNCTION = (MP_BC_BASE_VINT_O + 0x04)  # uint
MP_BC_CALL_FUNCTION_VAR_KW = (MP_BC_BASE_VINT_O + 0x05)  # uint
MP_BC_CALL_METHOD = (MP_BC_BASE_VINT_O + 0x06)  # uint
MP_BC_CALL_METHOD_VAR_KW = (MP_BC_BASE_VINT_O + 0x07)  # uint

MP_BC_IMPORT_NAME = (MP_BC_BASE_QSTR_O + 0x0b)  # qstr
MP_BC_IMPORT_FROM = (MP_BC_BASE_QSTR_O + 0x0c)  # qstr
MP_BC_IMPORT_STAR = (MP_BC_BASE_BYTE_E + 0x09)

OPCODES = dir()


def get(x: int):
    """
    Get an opcode by hex
    :param x: hex
    :return: opcode
    """
    for op in OPCODES:
        if not op.startswith("__") and not op == "bytecode_format":
            if eval(op) == x:
                return op


def get_op_value(opcode: str) -> int:
    """
    Get the value of an {opcode}
    :param opcode: name of opcode
    :return: value if found otherwise -1
    """
    if opcode is None or not valid_operation(opcode):
        return -1
    for op in OPCODES:
        if valid_operation(op) and op == opcode:
            return eval(op)


def valid_operation(x: str) -> bool:
    """
    Whether or not an opcode is valid
    :param x: opcode
    :return: whether or not the supplied opcode is valid
    """
    return not x.startswith("__") and not x == "bytecode_format"


def requires_extra_byte(op_code: int) -> bool:
    """
    Check if an opcode requires an extra byte
    :param op_code: opcode
    :return: if the code requires an extra byte
    """
    if op_code is None or not valid_operation(f'0x{op_code}'):
        return False
    # https://github.com/micropython/micropython/blob/47e6c52f0c2bf058c5d099dd2993192e0978e172/py/bc.c#L309
    valid = [MP_BC_LOAD_GLOBAL, MP_BC_LOAD_NAME, MP_BC_LOAD_ATTR, MP_BC_STORE_ATTR, MP_BC_BASE_QSTR_O]
    if op_code in valid:
        return True
    return False


def is_call_function(op_code: int) -> bool:
    """
    Check if an opcode is a call function
    :param op_code: opcode
    :return: if the code is a call function
    """
    if op_code is None or not valid_operation(f'0x{op_code}'):
        return False
    valid = [MP_BC_CALL_FUNCTION, MP_BC_CALL_METHOD, MP_BC_CALL_METHOD_VAR_KW, MP_BC_CALL_FUNCTION_VAR_KW]
    if op_code in valid:
        return True
    return False
