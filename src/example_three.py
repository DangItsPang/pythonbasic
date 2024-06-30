import pythonbasic as pb

def normal_probability():
    pb.clrHome()
    pb.disp("Lower bound?")
    pb.Prompt(L)
    pb.disp("Upper bound?")
    pb.Prompt(U)
    pb.disp("Mean?")
    pb.Prompt(M)
    pb.disp("Standard deviation?")
    pb.Prompt(S)
    P = pb.normalcdf(L, U, M, S)
    pb.disp(P)

pb.setup(globals(), __file__, normal_probability)