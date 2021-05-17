from core import get_opcode
from logger import excite, err


def get_op(x: str):
    to_plug = int(x) if x.find("0x") == -1 else int(x, 16)
    value = get_opcode(to_plug)
    if value is not None:
        excite(f'opcode for {x}: {value}')
    else:
        err(f'could not get opcode for {x}!')
