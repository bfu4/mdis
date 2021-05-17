#!/usr/bin/env python3
from cmd import call_command, set_up_arguments, parser
from logger import err

if __name__ == '__main__':

    set_up_arguments()
    args = parser.parse_args()

    to_format = args.INT_TO_BC
    to_dump = args.FILE
    to_op = args.INT_TO_OP
    from_loc = args.FROM
    to_loc = args.TO

    no_args = not to_format and not to_dump and not to_op

    if no_args:
        err("Missing arguments! Use [-h] for more information.")

    if to_format:
        call_command('-b', to_format)
    elif to_op:
        call_command('-op', to_op)
    elif to_dump:
        call_command('-f', [(to_dump, from_loc, to_loc)])
