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