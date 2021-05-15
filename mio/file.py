def read_file(file):
    """
    Read a file and return the stream
    :param file: file to read
    :return: stream
    """
    # todo: handle file type validation
    # print(identified)
    return open(file, "rb")


def is_valid_mpy(file):
    """
    Implementation of https://github.com/micropython/micropython/blob/605b74f390e1ce9acdbca32d0b3215d37b96852e/tools/mpy-tool.py#L791
    to validate a valid micropython file
    :param file:
    :return: whether the file is a valid micropython file
    """
