import pythonbasic as pb
import math

def theorum():
    pb.Prompt(A)
    pb.Prompt(B)
    C = pb.power(A, 2) + pb.power(B, 2)
    pb.disp(math.sqrt(C))

pb.setup(globals(), __file__, theorum)