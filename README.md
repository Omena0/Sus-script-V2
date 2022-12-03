# Scripter
 Some sussy script lang

# Info reading tips:
\<value\> = Argument

(value) = Comment

var = list of all variables

var 0 = latest set variable


# How it works:

## Variables: 
They are just in a list, so you need know the variables index if you want to access it.
You can do so using GET, which will just replace it with the value of the var, or the command might get the var from an argument.
BTW, The variable at index 0 is ALWAYS the most recently defined variable (highest index)

To set a variable use SET. With set you create a new variable and set it to a value, or format strings.
Since SET supports infinite arguments which any of can be other variables.
This is usefull when a command doesent support infinite arguments like PRINT.
(Also set is the most used command)

## Functions:
No native functions, you need to use GOTO to loop and stuff.

## Conditions:
With conditions you can check if a variable matches some value.

Basically the syntax is:
```sus-script 2 - Color edition
IF <VAR> (==) <VALUE>
DO <COMMAND>
ELSE <COMMAND>
```

You can add as many DO or ELSE commands as you want to run multiple commands, or just use GOTO.

## I/O:

You can get input by using either ASK, or INPUT.
ASK will add a prefix of "[ASK]: \> - "
INPUT will not add any prefix
They take 1 argument both, which is the prompt. (use GET for longer prompts)

You can send output with either LOG, or PRINT.
LOG will add a time, and color based on the logtype. The prefix is: "\<COLOR(s)\> [\<type\>]: \<time\> \> - "
PRINT will add a prefix of "[OUT]: \> - " unless argument 4 is set to NOPREFIX (use prints native get option to print longer values)

Syntax:
```sus-script 2 - Color edition
LOG <log level | GET> <msg | var> <msg>
```

## MATH:
With the MATH command you can calculate things really easily!
Syntax:
```sus-script 2 - Color edition
MATH <operator> <var1> <var2>
```
MATH will append the result to var.

## COLOR:
Using the COLOR command you can add color to a variable easily
Syntax:
```sus-script 2 - Color edition
COLOR <color> <var>
```

The only valid colors are BLUE, RED, YELLOW, and GREEN

## COMMENTS:
To start a comment begin a line with # and it wil be ignored.
Example:
```sus-script 2 - Color edition
# This is a comment!
```

## DEBUG:
By adding #!/DEBUG-A or #!/DEBUG-B the program will print extra debug info.

DEBUG A Displays:
```
COMMAND: <command>
```

DEBUG B Displays:
```
----------DEBUG----------
Command: <command>
Full args: <arguments>
Var: <all variables>
-------------------------
```

I personally like to toggle the debug options of by adding some symbol behind them.

## Timers:
You can create times by using the SLEEP command to sleep a number of seconds

Syntax:
```sus-script 2 - Color edition
SLEEP <GET | .1's of a second> <variable>
```

# Ask me if you want some more info about how to do something.

###### There is secret easter egg, if u want to find it read the code :)


