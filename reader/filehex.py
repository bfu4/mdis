from hexdump import hexdump


def dump_file_hex(file):
    """
    Dump a files hex
    :param file:
    :return: hex
    """
    return hexdump(read_file(file), result='return')


def read_file(file):
    """
    Read a file and return the stream
    :param file: file to read
    :return: stream
    """
    return open(file, "rb")
