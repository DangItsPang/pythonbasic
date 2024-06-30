# Python Basic
*An easier way to write TI-Basic*

Python Basic aims to simplify the process of writing code for Texas Instruments calculators.

For example, consider this code written in Basic:
```
Prompt A
Prompt B
A²+B²→C
Disp √(C)
```

If you wanted to write the same thing in Python Basic, it would be the following:
```
import pythonbasic as pb
import math

def theorum():
    pb.Prompt(A)
    pb.Prompt(B)
    C = pb.power(A, 2) + pb.power(B, 2)
    pb.disp(math.sqrt(C))

pb.setup(globals(), __file__, theorum)
```