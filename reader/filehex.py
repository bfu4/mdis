from hexdump import genchunks, dump


def dump_file_hex(file):
    """
    Dump a files hex
    :param file:
    :return: hex
    """
    return '\0'.join(generate_hex(read_file(file)))


def read_file(file):
    """
    Read a file and return the stream
    :param file: file to read
    :return: stream
    """
    return open(file, "rb")


def generate_hex(data):
    """
    A modified version of hexdump's dumpgen to only generate bytes, without format.
    """
    generator = genchunks(data, 16)
    for addr, d in enumerate(generator):
        dump_str = dump(d, sep='\00')
        line = dump_str[:8 * 3]
        if len(d) > 8:
            line += dump_str[8 * 3:]

        yield line
