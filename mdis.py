#!/usr/bin/env python3

from logger import err
from cmd import set_up_arguments, parser, call_command

if __name__ == '__main__':
    set_up_arguments()
    args = parser.parse_args()

    to_format = args.int

    if not to_format:
        err("Missing arguments! Use [-h] for more information.")

    if to_format:
        # handle dec versus hex :thonk:
        if str(to_format).find("0x") == -1:
            call_command('-bcf', int(to_format))
        else:
            call_command('-bcf', int(to_format, 0))
