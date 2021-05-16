from core.case import Case
from core.switch import switch


def handle(opcode):
    switch(opcode, [
        # todo: implement, this is just a test
        Case(0x40, lambda value: print(f'{value}'))
    ])
