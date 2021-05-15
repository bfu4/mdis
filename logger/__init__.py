import termcolor


def err(message):
    """
    Send an error message
    :param message: message to send
    :return: nothing, print error message
    """
    err_format = termcolor.colored("[!]", "red")
    print(f'{err_format} {message}')


def info(message):
    """
    Send an info message
    :param message: message to send
    :return: nothing, print info message
    """
    info_format = termcolor.colored(":: ", "blue")
    print(f'{info_format} {message}')
