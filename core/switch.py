from typing import List

from core.case import Case


def switch(value, cases):
    """
    Create a switch
    :param value:
    :param cases:
    :return:
    """
    if value:
        handle_cases(value, cases)


def handle_cases(value, cases: List[Case]):
    """
    Handle the cases
    :param value:
    :param cases:
    :return:
    """
    for case in cases:
        if case.equals(value):
            case.enact(value)
            break
