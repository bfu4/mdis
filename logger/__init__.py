import termcolor


def err(message):
    """
    Send an error message
    :param message: message to send
    :return: nothing, print error message
    """
    err_format = termcolor.colored("[!]", "red")
    print(f'{err_format} {message}')
    exit(1)


def info(message):
    """
    Send an info message
    :param message: message to send
    :return: nothing, print info message
    """
    info_format = termcolor.colored(":: ", "blue")
    print(f'{info_format} {message}')


def excite(message):
    """
    Send an excited message
    :param message: message to send
    :return: nothing, print excite message
    """
    excite_format = termcolor.colored("(\u0020\u26A1️\u0020)", "yellow")
    print(f'{excite_format} {message}')
