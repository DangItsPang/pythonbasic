# Creating a menu-based program

## What is a menu-based program?
A *menu-based program* is one of the two ways you can translate Python to TI-Basic using Python Basic. The other way is a [*function-based program*](./function_program.md). A menu-based program is a python script that contains one or more instances of the **Menu** class and a function that corresponds to each one. These is generally more complex to work with than function-based programs.

## Your first menu-based program
While the idea of creating instances of a class and a function for each menu may sound terrifying, it's not as bad as it sounds. This page will walk you through creating a program with a menu-based layout.

Here's the layout: There is a main menu with three options, *Add*, *Subtract*, and *Quit*. If quit is selected, the program ends. If add or subtract is selected, the user is then prompted for a number, which is saved as *X*. When the user provides *X*, they are then shown the submenu for either addition or subtraction, depending on which was selected. In this submenu, the user can then decide to add/subtract 1, 3, or 5, or go back. If they decide to go back, the main menu is again displayed. Otherwise, *X* is added/subtracted by the selected number, and the sum or difference is displayed to the user.

Hopefully the above explanation makes sense. If not, no worries - that's what you're about to create!

### Creating the menu objects
The **Menu** object takes three arguments: a title, a corresponding function, and a list of **MenuOption** objects.

For the main menu described above, here's what its constructor would look like:

```python
main_menu = pb.Menu("Main Menu", main_menu_function, [pb.MenuOption("Add"), pb.MenuOption("Subtract"), pb.MenuOption("Quit")])
```

*Main Menu* is the title, *main_menu_function* is the currently nonexistent function that will hold all the code for this menu, and the list of **MenuOption** objects represents every option the user will have on the menu.

---
**NOTE**

Whatever you specify as the option name for a **MenuOption** will be reformatted to all capital letters in the calculator, so you don't have to capitalize them in your script.

---

Now that you have created the **Menu** object for the main menu, it's time to do the same for the other two menus. Once complete, your program should look something like this:

```python
import pythonbasic as pb

main_menu = pb.Menu("Main Menu", main_menu_function, [pb.MenuOption("Add"), pb.MenuOption("Subtract"), pb.MenuOption("Quit")])

add_menu = pb.Menu("Add", add_function, [pb.MenuOption("Add 1"), pb.MenuOption("Add 3"), pb.MenuOption("Add 5"), pb.MenuOption("Back")])

subtract_menu = pb.Menu("Subtract", subtract_function, [pb.MenuOption("Subtract 1"), pb.MenuOption("Subtract 3"), pb.MenuOption("Subtract 5"), pb.MenuOption("Back")])
```

---
**IMPORTANT**

Whatever **Menu** object you create first will be the one that is intially shown to the user within the calculator. Since we want the main menu to be displayed first upon opening the program, make sure that it is declared before the addition or subtraction menus! 

Also note: the order in which all submenus are created doesn't matter.

---

### Creating the functions
Now that the **Menu** objects have been declared, we must write a function to correspond with each one. We'll once again start with the main menu. Here is what its function looks like:

```python
def main_menu_function(option): # Where option is the title of any MenuOption for this menu
    if option == "Add":
        pb.Prompt(X)
        pb.goto_menu(add_menu)
    if option == "Subtract":
        pb.Prompt(X)
        pb.goto_menu(subtract_menu)
    if option == "Quit":
        pb.Stop()
```

Ensure that the title of the function matches the function name specified when you declared the **Menu** object.

For each **MenuOption** belonging to the main menu, we must have an if statement for it in our function, following the syntax above. Within each if statement is where each option's code will be housed. For example, when the user selects *Add* from the main menu, they will be prompted for a number *X*, then taken to the addition submenu.

It's important to note that the the string in your if statement is case-sensitive. If you declared the **MenuOption** as
`pb.MenuOption("Add")`, then your function should look like the following:
```python
def main_menu_function(option):
    if option == "Add":
```

Another important fact is that `option` doesn't have to be the name of the argument. For example, consider the following code blocks, all of which are legitimate:

```python
def main_menu_function(choice):
    if choice == "Add":

def main_menu_function(selection):
    if selection == "Add":

def main_menu_function(your_word_here):
    if your_word_here == "Add":
```

You also don't have to use an if statement for each option. You could also choose to use `if` for the first option, and then `elif` for each subsequent option. It's up to you.

Here are the functions for the addition and subtraction menus:
```python
def add_function(option):
    if option == "Add 1":
        X += 1
        pb.Disp(X)
    if option == "Add 3":
        X += 3
        pb.Disp(X)
    if option == "Add 5":
        X += 5
        pb.Disp(X)
    if option == "Back":
        pb.goto_menu(main_menu)

def subtract_function(option):
    if option == "Subtract 1":
        X -= 1
        pb.Disp(X)
    if option == "Subtract 3":
        X -= 3
        pb.Disp(X)
    if option == "Subtract 5":
        X -= 5
        pb.Disp(X)
    if option == "Back":
        pb.goto_menu(main_menu)
```

Unlike the **Menu** objects, there is no order in which the `if` statements for each option must go; they can be completely randomized if you wish.

One last thing to point out. You may have noticed the `goto_menu()` command that is used to take the user to another menu. If you use this command, its argument must be the name of the **Menu** object you created. for example, recall how the main menu was created:

```python
main_menu = pb.Menu("Main Menu", main_menu_function, [pb.MenuOption("Add"), pb.MenuOption("Subtract"), pb.MenuOption("Quit")])
```

Because this **Menu** object is called *main_menu*, the user can be sent there at any time by calling `goto_menu(main_menu)`. If you wish, there are also other ways to send a user to a different menu:

```python
# 1. Specify a label
goto_label(main_menu.get_label())

# 2. Specify a menu title
pb.goto_menu_title("Main Menu")
```

Putting all three **Menu** objects along with their functions into the script, we get this final result:
```python
import pythonbasic as pb

def main_menu_function(option): # Where option is the title of any MenuOption for this menu
    if option == "Subtract":
        pb.Prompt(X)
        pb.goto_menu(subtract_menu)
    if option == "Quit":
        pb.Stop()
    if option == "Add":
        pb.Prompt(X)
        pb.goto_menu(add_menu)

def add_function(option):
    if option == "Add 1":
        X += 1
        pb.Disp(X)
    if option == "Add 3":
        X += 3
        pb.Disp(X)
    if option == "Add 5":
        X += 5
        pb.Disp(X)
    if option == "Back":
        pb.goto_menu(main_menu)

def subtract_function(option):
    if option == "Subtract 1":
        X -= 1
        pb.Disp(X)
    if option == "Subtract 3":
        X -= 3
        pb.Disp(X)
    if option == "Subtract 5":
        X -= 5
        pb.Disp(X)
    if option == "Back":
        pb.goto_menu(main_menu)


main_menu = pb.Menu("Main Menu", main_menu_function, [pb.MenuOption("Add"), pb.MenuOption("Subtract"), pb.MenuOption("Quit")])

add_menu = pb.Menu("Add", add_function, [pb.MenuOption("Add 1"), pb.MenuOption("Add 3"), pb.MenuOption("Add 5"), pb.MenuOption("Back")])

subtract_menu = pb.Menu("Subtract", subtract_function, [pb.MenuOption("Subtract 1"), pb.MenuOption("Subtract 3"), pb.MenuOption("Subtract 5"), pb.MenuOption("Back")])

pb.translate(globals(), __file__)
```

As opposed to a function-based program, you do not need to specify a function for the `translate` command. Instead, just pass `globals()` and `__file__` into the function, and leave the function argument blank. The module will know to translate a menu-based program.

Once the translation is complete, we get the TI-Basic back in a text file:
```
Lbl AE
Menu("MAIN MENU","ADD",AB,"SUBTRACT",AC,"QUIT",AD
Lbl AB
Prompt X
Goto AJ
Stop
Lbl AC
Prompt X
Goto AO
Stop
Lbl AD
Stop
Stop
Lbl AJ
Menu("ADD","ADD 1",AF,"ADD 3",AG,"ADD 5",AH,"BACK",AI
Lbl AF
X+1→X
Disp X
Stop
Lbl AG
X+3→X
Disp X
Stop
Lbl AH
X+5→X
Disp X
Stop
Lbl AI
Goto AE
Goto AE
Stop
Lbl AO
Menu("SUBTRACT","SUBTRACT 1",AK,"SUBTRACT 3",AL,"SUBTRACT 5",AM,"BACK",AN
Lbl AK
X-1→X
Disp X
Stop
Lbl AL
X-3→X
Disp X
Stop
Lbl AM
X-5→X
Disp X
Stop
Lbl AN
Goto AE
Stop
```
You can then copy-paste the TI-Basic into TI Connect or TI Connect CE to send it to your calculator. A more in-depth guide can be found [here](https://education.ti.com/en/customer-support/knowledge-base/sofware-apps/product-usage/11492).

## Conclusion
Menu-based programs are quite a bit more involved than their function-based counterparts. Hopefully, you now have a solid understanding of how menu-based programs work and can implement them into your own projects.

If you want some inspiration before you start on your own projects, check out the [examples page](./examples.md)!