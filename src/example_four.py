import pythonbasic as pb
import math as math

N = 0

def factor_number():
    pb.disp("Integer?")
    pb.Prompt(N)

    pb.literal_tibasic("{0}→∟FTR")
    
    if N < 0:
        I = 1
    
    while I < pb.abs(N):
        D = N/I

        if pb.fPart(D) == 0:
            pb.literal_tibasic("D→∟FTR(1+dim(∟FTR))")
            pb.literal_tibasic("I→∟FTR(1+dim(∟FTR))")

            pb.STR1.set(pb.STR1.get() + pb.toString(D) + "_" + pb.toString(I) + "__")
            
            # Str1+toString(D)+"_"+toString(I)+"__"→Str1
        I += 1

    pb.clrHome()
    pb.output(1,1,pb.STR1.get())


pb.setup(globals(), __file__, factor_number)