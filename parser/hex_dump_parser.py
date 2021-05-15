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
    if from_index > to_index:
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
    byte_array = []
    arr_index = 0
    for line in dumped_arr:
        current_line = line.split(":")[1]
        current_line = current_line[0:49]
        byte_array.insert(arr_index, '\0'.join(current_line.split("\u0020")))
        arr_index += 1
    return byte_array
