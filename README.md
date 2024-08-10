# SimpleConfig - easy to parse config!

### How to install? 
```bash
$ pip install smpl_config
```
# Methods

Available methods of `simpleconfig.SimpleConfig`:
* `SimpleConfig.parse`
* `SimpleConfig.get`
* `SimpleConfig.int`
* `SimpleConfig.bool`
* `SimpleConfig.float`
* `SimpleConfig.generate_iter`

# `SimpleConfig.parse`

File parsing function

Arguments:
* `path` - path to config file

Returns:
* `NoneType`

# `SimpleConfig.get`

Function to get the value of a variable

Arguments:
* `item` - variable name to get the value

Returns:
* `str` - If successful, a string will be received

Exceptions:
* `KeyError` - If variable is not found

# `SimpleConfig.int`

Function to get the integer value of a variable

Arguments:
* `item` - variable name to get the value

Returns:
* `int` - If successful, a integer will be received
* `NoneType` - If the value cannot be an integer, a NoneType will be received

Exceptions:
* `KeyError` - If variable is not found

# `SimpleConfig.boolean`

Function to get the boolean value of a variable

Arguments:
* `item` - variable name to get the value

Returns:
* `bool` - If successful, a booleaan will be received
* `NoneType` - If the value cannot be an boolean (is this possible?), a NoneType will be received

Exceptions:
* `KeyError` - If variable is not found

# `SimpleConfig.float`

Function to get the float value of a variable

Arguments:
* `item` - variable name to get the value

Returns:
* `float` - If successful, a float will be received
* `NoneType` - If the value cannot be an float, a NoneType will be received

Exceptions:
* `KeyError` - If variable is not found
