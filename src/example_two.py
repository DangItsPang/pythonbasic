import pythonbasic as pb

def main_menu_function(option):
    if option == "Add":
        pb.Prompt(A)
        pb.Prompt(B)
        S = A + B
        pb.disp(S)
        pb.pause()
        pb.clrHome()
        pb.goToMenu(main_menu)
    if option == "Subtract":
        pb.Prompt(A)
        pb.Prompt(B)
        pb.disp(A - B)
        pb.pause()
        pb.clrHome()
        pb.goToMenu(main_menu)
    if option == "Multiply":
        pb.Prompt(A)
        pb.Prompt(B)
        pb.disp(A * B)
        pb.pause()
        pb.clrHome()
        pb.goToMenu(main_menu)
    if option == "Divide":
        pb.Prompt(A)
        pb.Prompt(B)
        pb.disp(A / B)
        pb.pause()
        pb.clrHome()
        pb.goToMenu(main_menu)
    if option == "Quit":
        pb.Stop()

main_menu = pb.Menu("Main Menu", main_menu_function, [pb.MenuOption("Add"), pb.MenuOption("Subtract"), pb.MenuOption("Multiply"),
                    pb.MenuOption("Divide"), pb.MenuOption("Quit")])

pb.setup(globals(), __file__)