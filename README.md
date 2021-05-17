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

## References
* [micropython/py/bc0.h](https://github.com/micropython/micropython/blob/master/py/bc0.h)
* [micropython/tools/mpy-tool.py#L130](https://github.com/micropython/micropython/blob/605b74f390e1ce9acdbca32d0b3215d37b96852e/tools/mpy-tool.py#L130)
