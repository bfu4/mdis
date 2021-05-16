from logger import err


def parse(hexdump, from_loc: str, to_loc: str):
    """
    Parse a hex dump from a location to another location
    :param hexdump: dump contents
    :param from_loc: starting location
    :param to_loc: end location
    :return: lines of hex between
    """
    dump_as_arr = str(hexdump).split("\n")
    from_index = find(hexdump, from_loc)
    to_index = find(hexdump, to_loc)
    if int(from_loc, 16) > int(to_loc, 16):
        err(f'Cannot parse locations backwards! Asked to find {from_loc} to {to_loc}')
        return

    return dump_as_arr[from_index:to_index]


def parse_bytes(hexdump, from_loc: str, to_loc: str):
    """
    Parse an array of bytes from a hexdump with a given from location and to location
    :param hexdump: dump contents
    :param from_loc: starting location
    :param to_loc: end location
    :return: bytes between
    """
    parsed = parse(hexdump, from_loc, to_loc)
    return get_bytes(parsed)


def find(hexdump, location: str):
    """
    Find the index of a location
    :param hexdump: hexdump to search
    :param location: location of line
    :return: index if found otherwise -1
    """
    split = str(hexdump).split("\n")
    loc = location if location.index("0x") == -1 else location.split("0x")[1]
    for line in split:
        if line[0:8] == loc:
            return split.index(line)
    return -1


def get_bytes(dumped_arr):
    """
    Get the bytes from an array of hex dumps
    :param dumped_arr: array of hex dumps
    :return: bytes
    """
    byte_array = []
    arr_index = 0
    for line in dumped_arr:
        current_line = line.split(":")[1]
        current_line = current_line[0:49]
        byte_array.insert(arr_index, ''.join(current_line.split("\u0020")))
        arr_index += 1
    return byte_array


def split_bytes_from_lines(lines_of_bytes):
    """
    Split the bytes in multiple lines into an array of arrays of bytes
    :param lines_of_bytes: lines to split
    :return: array of arrays of bytes
    """
    index = 0
    arr = []
    for line in lines_of_bytes:
        arr.insert(index, split_bytes(line))
        index += 1
    return arr


def split_bytes(line_of_bytes: str):
    """
    Split the bytes in a line into an array for pairs
    :param line_of_bytes: line of bytes
    :return: array of the bytes
    """
    ctx = 0
    append = []
    while ctx < len(line_of_bytes):
        append.insert(int(ctx / 2), str(line_of_bytes[ctx:ctx + 2]))
        ctx += 2
    return append
