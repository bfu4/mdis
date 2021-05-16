#!/usr/bin/env python3

from core import Translator
from logger import info, excite

if __name__ == '__main__':

    # Lambda replaced by def flatten due to E731
    def flatten(_list): return [item for sublist in _list for item in sublist]

    translator = Translator("./__test__/print.mpy")
    excite(translator.get_magic())

    # todo: support for other addresses besides for default base10
    for line in translator.get_instruction_set():
        info(line)
"""
    set_up_arguments()
    args = parser.parse_args()

    to_format = args.int
    to_dump = args.file

    if not to_format and not to_dump:
        err("Missing arguments! Use [-h] for more information.")

    if to_format:
        # handle dec versus hex :thonk:
        if str(to_format).find("0x") == -1:
            call_command('-bcf', int(to_format))
        else:
            call_command('-bcf', int(to_format, 0))
    elif to_dump:
        info(f'dumping {to_dump}')
        call_command('-fhx', to_dump)
"""
