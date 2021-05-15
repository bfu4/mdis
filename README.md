# mdis
An attempt at a disassembler for Micropython bytecode.
Largely inspired by [DC540's MicroPython Challenge](https://github.com/mytechnotalent/dc540-0x00002).

## Usage

```bash
$ python ./mdis.py -h
```

| command | arguments | type | description |
|---------|-----------|------|-------------|
| `-h`, `-help` | none | n/a | show the help menu |
| `-bcf`, `-bytecode-format` |  int to format | integer | format an integer into the micropython bytecode format |
| `-file-hex`, `-fhx` | file | name of file | print all bytes of a file (raw) |

## Contributing
There are not too many contribution guidelines. Contributions should follow a decent code style and documentation style, and should be verbose with the changes.

### Source Tree
* `cmd` - cli commands
* `core` - disassembler core
* `io` - base io / file io
* `logger` - logging
* `parser` - file parsing
* `reader` - file reading

## Dependencies
* filemagic [1.6]
* termcolor [1.1.0]
## References
* [micropython/py/bc0.h](https://github.com/micropython/micropython/blob/master/py/bc0.h)
* [micropython/tools/mpy-tool.py#L130](https://github.com/micropython/micropython/blob/605b74f390e1ce9acdbca32d0b3215d37b96852e/tools/mpy-tool.py#L130)