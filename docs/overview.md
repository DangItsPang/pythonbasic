# Overview

**Python Basic aims to simplify the process of writing code for Texas Instruments calculators.**

Python Basic allows the user to write code in Python, and the module will turn the Python code into TI-Basic. This is achieved by functions within the module that correspond to commands in TI calculators. For example, consider the following Python code:

```python
import pythonbasic as pb
import math

def theorum():
    pb.Prompt(A)
    pb.Prompt(B)
    C = pb.power(A, 2) + pb.power(B, 2) 
    pb.Disp(math.sqrt(C))

pb.setup(globals(), __file__, theorum)
```

And here's its TI-Basic translation:
```
Prompt A
Prompt B
A²+B²→C
Disp √(C)
```

This is, in its simpliest form, what Python Basic does. It goes line by line, converting the various module functions into commands that your calculator can understand.

## Capabilities

Python Basic tries to support as much of TI-Basic as possible. This includes, but is not limited to:
* Input commmands such as Prompt and Input
* Output commands such as Disp and Output
* Support for menus and submenus
* Many statistical functions, such as normalcdf and invNorm
* Support for lists

## Drawbacks

Ultimately, Python Basic was created and is maintained by one person, so certain feature may have been overlooked. Namely:
* Matrices
* Many more statistical function, such as 2-PropZTest and χ²GOF-Test
* Whatever else was forgotten

You can find a pretty comprehensive list of TI-Basic's commands [here](http://tibasicdev.wikidot.com/command-index), and you're encourage you to request a command/feature if it's not already supported. Most of the time, additional commands aren't too difficult to implement. You can also report bugs and ask questions if you wish. You can find that link [here](https://github.com/DangItsPang/pythonbasic/issues).

Now that you have an overview of Python Basic, you can move on to the [installation guide](./installation.md)!