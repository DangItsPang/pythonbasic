# Creating a function-based program

## What is a function-based program?
A *function-based program* is one of the two ways you can translate Python to TI-Basic using Python Basic. The other way is a [*menu-based program*](./menu_program.md). A function-based program is a python script containing one function that holds all the code to be translated to TI-Basic. These are generally simpler to work with than menu-based programs.

## Your first function-based program
If the above explanation doesn't make perfect sense, don't worry. This page will walk you through creating a function-based program, and you should hopefully see that it's not nearly as complicated as it sounds.

For simplicity's sake, we're going to be making a program that takes a specified number and adds 5 to it. To start, add in a function that will contain the code that is to be translated to TI-Basic.

```python
def add_five():
    # Python code to be translated to TI-Basic goes in here!
```

---
**NOTE**

The function name doesn't matter, and the function never takes an argument.

---

In this function, we first need to ask the user for a number, and then we need to add 5 to it before displaying the result back. This is achieved with the following:

```python
def add_five():
    pb.Prompt(N)
    N += 5
    pb.Disp(N)
```

Note that if you try to run the python file now, nothing will happen. This is because you must call the _translate()_ function, as shown below:

```python
pb.translate(globals(), __file__, add_five)
```

`globals()` and `__file__` remain unchanged. The last argument is the only one with any variability, as it will be set to the function whose code you want to translate. ***NOTE:*** If you are translating a script that uses a menu structure instead of a single function, you would leave

With the `translate()` function added, rerun the script. You should be prompted in the terminal to specify an output file name. Call it whatever you'd like, and hit enter. The translated code will be now be in a text file in the same directory as your script. Open that text file. For our example, it should look like this:

```
Prompt N
N+5→N
Disp N
```

Now, you can [send the program to your calculator](https://education.ti.com/en/customer-support/knowledge-base/sofware-apps/product-usage/11492) with the calculator's USB cable and the [TI Connect](https://education.ti.com/en/software/details/en/B59F6C83468C4574ABFEE93D2BC3F807/swticonnectsoftware) / [TI Connect CE](https://education.ti.com/en/software/details/en/CA9C74CAD02440A69FDC7189D7E1B6C2/swticonnectcesoftware) desktop apps. Once you have TI Connect (CE) open, you can copy-paste the translated code from the text file into the application and ship it to your calculator. After that, you can run the program on your calculator!

![Program ADDFIVE running on a TI-84 Plus CE](/pythonbasic/photos/add_five.png)

## Conclusion

You should now understand what function-based programs are. This is a obviously a simplified example, but all function-based programs resemble this one at their core. They `import pythonbasic`, declare one function that holds all the calculator's soon-to-be code, and then call the `translate()` function.

To explore the other type of Python Basic program, see [menu-based programs](./menu_program.md).