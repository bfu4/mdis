# mdis
![https://img.shields.io](https://img.shields.io/badge/license-MIT-fecde0?style=for-the-badge) ![https://img.shields.io](https://img.shields.io/badge/written%20in-python-4b8bbe?style=for-the-badge)

An attempt at a disassembler for Micropython bytecode.
Largely inspired by [DC540's MicroPython Challenge](https://github.com/mytechnotalent/dc540-0x00002).

## Usage

```bash
$ python ./mdis.py -h
```

| argument | type | description |
|---------|------|-------------|
| `-h`, `-help` | none | show the help menu |
| `-b INTEGER`|  int to format  | format an integer into the micropython bytecode format |
| `-op INTEGER` | int to get opcode of | integer | get an opcode of a valid integer |
| `-f FILE` | file | supply a file to print disassembly for |
| `-fr FROM` |  0 offset addr | supply a from address for instruction dump. ***constraint: must be a 0 offset address***. requires to address (`-t`). |
| `-t TO` |  0 offset addr | supply a to address for instruction dump. ***constraint: must be a 0 offset address***. requires from address (`-fr`). |

## Contributing
There are not too many contribution guidelines. Contributions should follow a decent code style and documentation style, and should be verbose with the changes.


### Source Tree
* `cmd` - cli commands
* `core` - disassembler core
* `mio` - base io / file io
* `logger` - logging
* `parser` - file parsing
* `reader` - file reading

## Dependencies
* hexdump **[3.3]**
* termcolor **[1.1.0]**
* six **[1.16.0]**

## Some Notes
There are a few things that are important to know with this very experimental project!

* Aforementioned `0-offset addresses` are addresses that have no offset. Similar to the addresses seen in an xxd dump.
* The bytes parsed are **big-endian**
* Sometimes it won't dump an entire file.
* MicroPython deals with strings as shown [here](https://docs.micropython.org/en/v1.10/micropython-docs.pdf) on page 139. This is unsupported as of currently.
* There is a hidden parser feature that is not utilised but prints out EVERY SINGLE HEX BYTE in the file, without addresses.
* This project essentially provides a level of "pseudocode", but with the actual MicroPython instructions. Due to previously listed, things, they are not the most accurate, but relatively enough.

## Outputs

### `./mdis.py -f ./__tests__/print.mpy`
The file `print.mpy` is compiled through mpy-cross, and is a file with the following code:

```python
print('hi')
```

Since it originates from a python file, we can look at the original disassembly:

```python
"""
  2           0 LOAD_NAME                0 (print)
              2 LOAD_CONST               0 ('hi')
              4 CALL_FUNCTION            1
              6 POP_TOP
              8 LOAD_CONST               1 (None)
             10 RETURN_VALUE
"""
```

Disassembling the .mpy file, we get this output:

![out](https://media.discordapp.net/attachments/831349942890659841/843669954079227904/unknown.png)

Similar, but not entirely accurate.

This output highlights each opcode's hex value as seen on the left. These values are reflected in [bc0.h](https://github.com/micropython/micropython/blob/master/py/bc0.h).

### `./mdis.py -op 0x40`
![opcode](https://cdn.discordapp.com/attachments/832660182672080969/843716173840252978/unknown.png)

### `./mdis.py -b 0x30`
![bytecode formatted uint](https://cdn.discordapp.com/attachments/832660182672080969/843716471473438730/unknown.png)

## References
* [micropython/py/bc0.h](https://github.com/micropython/micropython/blob/master/py/bc0.h)
* [micropython/tools/mpy-tool.py#L130](https://github.com/micropython/micropython/blob/605b74f390e1ce9acdbca32d0b3215d37b96852e/tools/mpy-tool.py#L130)
* [DC540's MicroPython Challenge](https://github.com/mytechnotalent/dc540-0x00002)