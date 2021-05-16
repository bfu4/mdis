from typing import List

from parser import parse_bytes, split_bytes_from_lines, get_bytes, parse_instruction_set, wrap_parsed_set
from reader import dump_file_hex_with_locs


class Translator:
    """
    Class handling file translations from *.mpy to hex dumps and opcodes
    """

    def __init__(self, file: str):
        """
        Create new translator
        :param file: location of the file
        """
        self.file = file

    def get_file_hex(self):
        """
        Get a full hex dump of the file
        :return:
        """
        return dump_file_hex_with_locs(self.file)

    def get_file_hex_at(self, _from: str, _to: str):
        """
        Get a byte dump at a specified location
        :param _from: from address
        :param _to: to address
        :return: bytes from address {_from} to address {_to}
        """
        return parse_bytes(self.get_file_hex(), _from, _to)

    def get_file(self):
        """
        Get the file name
        :return:
        """
        return self.file

    def get_magic(self) -> str:
        """
        Get the magic number
        :return:
        """
        return "".join(self.get_all_bytes()[0][:8])

    def get_all_bytes(self):
        """
        Get all of the bytes
        :return: all of the bytes
        """
        return get_bytes(self.get_file_hex().split("\n"))

    def get_split_bytes(self) -> List[List[str]]:
        """
        Get all of the bytes per line
        :return: bytes in list form
        """
        split = split_bytes_from_lines(self.get_all_bytes())
        split[0] = split[0][4:]
        return split

    def get_bytes_at(self, _from: str, _to: str) -> List[List[str]]:
        """
        Get the bytes between the specified locations
        :param _from: start address
        :param _to: end address
        :return: bytes
        """
        return split_bytes_from_lines(self.get_file_hex_at(_from, _to))

    def get_instruction_set(self) -> List[str]:
        """
        Get the file's instruction set
        :return: set
        """
        _bytes = self.__flatten(self.get_split_bytes())
        _set = parse_instruction_set(_bytes)
        return wrap_parsed_set(_set)

    def get_instructions_at(self, _from: str, _to: str) -> List[str]:
        """
        Get the instructions between addresses
        :param _from: start address
        :param _to: end address
        :return: instructions
        """
        _bytes = self.__flatten(self.get_bytes_at(_from, _to))
        _set = parse_instruction_set(_bytes)
        return wrap_parsed_set(_set)

    def __flatten(self, _list):
        return [item for sublist in _list for item in sublist]
