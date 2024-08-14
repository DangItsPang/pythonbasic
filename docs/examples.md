# Example projects

* [Example One](#example-one)
* [Example Two](#example-two)
* [Example Three](#example-three)
* [Example Four](#example-four)

## Example One

### Overview
This program showcases the pythagorean theorem. It prompts the user for two numbers, _A_ and _B_, and finds the length of _C_ using the formula.

### Python Code
```python
import pythonbasic as pb
import math

def theorum():
    pb.Prompt(A)
    pb.Prompt(B)
    C = pb.power(A, 2) + pb.power(B, 2) 
    pb.Disp(math.sqrt(C))

pb.translate(globals(), __file__, theorum)
```

### TI-Basic Translation
```
Prompt A
Prompt B
A²+B²→C
Disp √(C)
```

## Example Two

### Overview
This program features a main menu. From this menu, the user can select one of five options: add, subtract, multiply, divide, or quit. If quit is selected, the program ends immediately. If any other option is selected, the program will prompt the user for two numbers, _A_ and _B_. It will then perform the selected option on the two numbers and display the result back to the user.

### Python Code
```python
import pythonbasic as pb

def main_menu_function(option):
    if option == "Add":
        pb.Prompt(A)
        pb.Prompt(B)
        S = A + B
        pb.Disp(S)
        pb.Pause()
        pb.ClrHome()
        pb.goto_menu(main_menu)
    if option == "Subtract":
        pb.Prompt(A)
        pb.Prompt(B)
        pb.Disp(A - B)
        pb.Pause()
        pb.ClrHome()
        pb.goto_menu(main_menu)
    if option == "Multiply":
        pb.Prompt(A)
        pb.Prompt(B)
        pb.Disp(A * B)
        pb.Pause()
        pb.ClrHome()
        pb.goto_menu(main_menu)
    if option == "Divide":
        pb.Prompt(A)
        pb.Prompt(B)
        pb.Disp(A / B)
        pb.Pause()
        pb.ClrHome()
        pb.goto_menu(main_menu)
    if option == "Quit":
        pb.Stop()

main_menu = pb.Menu("Main Menu", main_menu_function, [pb.MenuOption("Add"), pb.MenuOption("Subtract"), pb.MenuOption("Multiply"), pb.MenuOption("Divide"), pb.MenuOption("Quit")])

pb.translate(globals(), __file__)
```

### TI-Basic Translation
```
Lbl AG
Menu("MAIN MENU","ADD",AB,"SUBTRACT",AC,"MULTIPLY",AD,"DIVIDE",AE,"QUIT",AF
Lbl AB
Prompt A
Prompt B
A+B→S
Disp S
Pause 
ClrHome
Goto AG
Stop
Lbl AC
Prompt A
Prompt B
Disp A-B
Pause 
ClrHome
Goto AG
Stop
Lbl AD
Prompt A
Prompt B
Disp A*B
Pause 
ClrHome
Goto AG
Stop
Lbl AE
Prompt A
Prompt B
Disp A/B
Pause 
ClrHome
Goto AG
Stop
Lbl AF
Stop
Stop
```

## Example Three

### Overview
This program calculates the probability of a random number in a normal distribution of data falling between the specified upper and lower bounds. The user specifies the lower bound, upper bound, and the mean and standard deviation of the normal distribution, and the program returns the probability of a random number falling between the two specified bounds, given that the mean and standard deviation are true.

### Python Code
```python
import pythonbasic as pb

def normal_probability():
    pb.ClrHome()
    pb.Disp("Lower bound?")
    pb.Prompt(L)
    pb.Disp("Upper bound?")
    pb.Prompt(U)
    pb.Disp("Mean?")
    pb.Prompt(M)
    pb.Disp("Standard deviation?")
    pb.Prompt(S)
    P = pb.normalcdf(L, U, M, S)
    pb.Disp(P)

pb.translate(globals(), __file__, normal_probability)
```

### TI-Basic Translation
```
ClrHome
Disp "Lower bound?"
Prompt L
Disp "Upper bound?"
Prompt U
Disp "Mean?"
Prompt M
Disp "Standard deviation?"
Prompt S
normalcdf(L,U,M,S)→P
Disp P
```

## Example Four

### Overview
This program asks the user for an integer. When given, the program finds all positive and negative factoring pairs for that number. It does this by creating a variable _I_, which starts equal to 1 and is incremented in a while loop. It then divides the specified number, _N_, by I, and checks if the result is an integer. If it is, then both the divisor and the quotient are factors of _N_. They are appended to a list called _factors_ (known in the calculator as _⌊FTR_). _I_ is then incremented by 1, and _N_ is once again divided by _I_.

After the program finds all the factors of _N_, it then displays them to the user in a page format, where each page gets 16 pairs of factors. The user can scroll between these pages by using the up and down arrows on the calculator to see all of the factoring pairs.

### Python Code
```python
import pythonbasic as pb

factors = pb.List("FTR", "{0}")

N = 0
def get_factors():
    
    pb.Disp("Integer?")
    pb.Prompt(N)

    I = 1
    while I < pb.abs(N)/2:
        R = N/I

        if factors.contains_number(R):
            I = pb.abs(N)

        if pb.fPart(R) == 0 and pb.Not(factors.contains_number(R)):
            factors.append(R)
            factors.append(I)
            factors.append(R*-1)
            factors.append(I*-1)
        
        I += 1

    pb.ClrHome()
    factors.remove_index(1)

    M = pb.dim(factors.get_list())
    I = 1

    # P represents the "page" of factors being displayed to the user. Each page holds 32 factors, in 16 pairs of 2.
    # U represents the final page of factors. If we have 70 factors, U will be 2, as pages 0 and 1 will be filled
    # with the first 64 factors, and the remaining 6 will be on page 2.
    P = 0
    U = M/32
    if pb.fPart(U) == 0:
        U -= 1
    U = pb.floor(U)

    pb.Lbl("AA")
    pb.ClrHome()

    pb.Output(1, 1, "FACTORS OF")
    pb.Output(1, 12, N)
    pb.Output(10, 1, "ENTER TO CLOSE")
    if M > 32:
        if P != 0:
            pb.Output(1, 22, "PRV ^")
        if P != U:
            pb.Output(10, 22, "NXT v")

    if P < 0:
        P = 0
    if M < U:
        P = U
    
    I = P*32+1
    R = 2

    if M-I > 32:
        # This means more than 32 factors are still left to be displayed, so we will put 32 onto this page
        while I < P*32+32:
            # Display this page of factors
            pb.Output(R,1,"("+pb.toString(factors.get_index(I))+", "+pb.toString(factors.get_index(I+1))+")")
            I += 2

            if M-I >= 1:
                pb.Output(R,14,"("+pb.toString(factors.get_index(I))+", "+pb.toString(factors.get_index(I+1))+")")
                I += 2
                R += 1
            
        K = 0   
        while K == 0:
            Q = pb.getKey()
            if Q == 25 and P != 0:
                # 25 corresponds to the up arrow key
                P -= 1
                K = Q
                pb.goto_label("AA")
            if Q == 34 and P != U:
                # down arrow pressed
                P += 1
                K = Q
                pb.goto_label("AA")
            if Q == 105:
                # enter key pressed
                K = Q
                pb.ClrHome()
                pb.Stop()
    else:
        while I < M:
            pb.Output(R,1,"("+pb.toString(factors.get_index(I))+", "+pb.toString(factors.get_index(I+1))+")")
            I += 2

            if M - I >= 1:
                pb.Output(R,14,"("+pb.toString(factors.get_index(I))+", "+pb.toString(factors.get_index(I+1))+")")
                I += 2
                R += 1
        
        if P != 0:
            K = 0   
            while K == 0:
                Q = pb.getKey()
                if Q == 25 and P != 0:
                    # 25 corresponds to the up arrow key
                    P -= 1
                    K = Q
                    pb.goto_label("AA")
                if Q == 34 and P != U:
                    # down arrow pressed
                    P += 1
                    K = Q
                    pb.goto_label("AA")
                if Q == 105:
                    # enter key pressed
                    K = Q
                    pb.ClrHome()
                    pb.Stop()
            
        pb.Pause()
        pb.ClrHome()
        pb.Stop()

pb.translate(globals(), __file__, get_factors)
```

### TI-Basic Translation
```
{0}→⌊FTR

Disp "Integer?"
Prompt N

1→I
While I<abs(N)/2
N/I→R

If max(not(⌊FTR-R)
Then
abs(N)→I

End
If fPart(R)=0 and not(max(not(⌊FTR-R))
Then

R→⌊FTR(1+dim(⌊FTR))
I→⌊FTR(1+dim(⌊FTR))
R*­1→⌊FTR(1+dim(⌊FTR))
I*­1→⌊FTR(1+dim(⌊FTR))

End
I+1→I

End
ClrHome
seq(⌊FTR(X+(X≥1)),X,1,dim(⌊FTR)+­1)→⌊FTR

dim(⌊FTR)→M
1→I




0→P
M/32→U
If fPart(U)=0
Then
U-1→U
End
int(U)→U

Lbl AA
ClrHome

Output(1,1,"FACTORS OF")
Output(1,12,N)
Output(10,1,"ENTER TO CLOSE")
If M>32
Then
If P≠0
Then
Output(1,22,"PRV ^")
End
If P≠U
Then
Output(10,22,"NXT v")

End
End
If P<0
Then
0→P
End
If M<U
Then
U→P

End
P*32+1→I
2→R

If M-I>32
Then

While I<P*32+32

Output(R,1,"("+toString(⌊FTR(I))+", "+toString(⌊FTR(I+1))+")")
I+2→I

If M-I≥1
Then
Output(R,14,"("+toString(⌊FTR(I))+", "+toString(⌊FTR(I+1))+")")
I+2→I
R+1→R

End
End
0→K
While K=0
getKey→Q
If Q=25 and P≠0
Then

P-1→P
Q→K
Goto AA
End
If Q=34 and P≠U
Then

P+1→P
Q→K
Goto AA
End
If Q=105
Then

Q→K
ClrHome
Stop
End
End
Else
While I<M
Output(R,1,"("+toString(⌊FTR(I))+", "+toString(⌊FTR(I+1))+")")
I+2→I

If M-I≥1
Then
Output(R,14,"("+toString(⌊FTR(I))+", "+toString(⌊FTR(I+1))+")")
I+2→I
R+1→R

End
End
If P≠0
Then
0→K
While K=0
getKey→Q
If Q=25 and P≠0
Then

P-1→P
Q→K
Goto AA
End
If Q=34 and P≠U
Then

P+1→P
Q→K
Goto AA
End
If Q=105
Then

Q→K
ClrHome
Stop

End
End
End
Pause 
ClrHome
Stop
```

### The Result

| ![The first page of the factors for -300](/pythonbasic/photos/example_four(1).png) | ![The second page of the factors for -300](/pythonbasic/photos/example_four(2).png)
|:--:|:--:|
| *The first page of factors for -300* | *The second page of factors for -300* |