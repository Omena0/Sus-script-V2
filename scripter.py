#############################
# Made By Omena0.           #
# Do Not claim as your own! #
#############################

Commands = ['help','print','log','set','echo','input','get','ask','if','do','else','goto','sleep','math','color']

import string
import random as r
import sys
import os
import traceback
import time as t
import colorama
from colorama import *
colorama.init(autoreset=True)
from termcolor import colored

for i in range(20): print('\n')

true = True
false = False

def log(type,msg):
    time = t.strftime('%H:%m:%S')
    if type == 'SUCCESS':
        print(Fore.GREEN + Style.BRIGHT + f'[{type}]: {time} > - {msg}',end='\n')
    elif type == 'WARN':
        print(Fore.YELLOW + Style.BRIGHT + f'[{type}]: {time} > - {msg}',end='\n')
    elif type == 'ERROR':
        #print(Fore.RED + Style.BRIGHT + Back.LIGHTWHITE_EX + f'[{type}]: {time} > - {msg}')
        print(colored(f'[{type}]: {time} > - {msg}','red',attrs=['underline','bold']),end='\n')
    else: print(Style.BRIGHT + Fore.WHITE + f'[{type}]: {time} > - {msg}',end='\n')

version = 'V0.23 COLOR EDITION'
prefix = '[OUT]: > - '
ask_prefix = '[ASK]: > - '


log('INFO',f'Sus script {version}, Made by Omena0!\n')
log('INFO','[PROGRAM START]\n\n')
global var
var = ['']

def execute(content,line):
    content = content + ' '
    if debug == True: 
        print(Style.BRIGHT + Fore.WHITE + 'COMMAND: ' + content)
    args = content.split(" ",100)
    command = args[0]
    if '#' in args[0]:
        return None
    if command == '\n':
        return None
    var[0] = var[len(var)-1]
    index = 0
    if debugb == True:
        if command == '#!/DEBUGB\n' or command == '#!/DEBUG\n': return None
        print(Fore.WHITE + Style.BRIGHT + '\n----------DEBUG----------')
        print(Fore.WHITE + Style.BRIGHT + f'Command: {command}')
        print(Fore.WHITE + Style.BRIGHT + f'Full args: {args}')
        print(Fore.WHITE + Style.BRIGHT + f'Var: {var}')
        print(Fore.WHITE + Style.BRIGHT + '-------------------------\n')

    if command == 'help':
        print('Commands: ')
        for i in commands: print(i)
    
    if command == 'print':
        if args[1] == 'GET':
            args[1] = var[int(args[2])]
            args[2] = ''
        try: 
            if args[4] == 'NOPREFIX': print(Fore.WHITE + Style.BRIGHT + f'{args[1]} {args[2]} {args[3]}',end='')
            else: print(Fore.WHITE + Style.BRIGHT + f'{prefix} {args[1]} {args[2]} {args[3]} ',end='')
        
        except:
            log('WARN','Print Failed: Expected at least 3 arguments.')

            
    if command == 'log':
        if args[2] == 'GET':
            args[2] = var[int(args[3])]
            args[3] == ''
        try: log(f'{args[1]}',f' {args[2]} {args[3]} ')
        except: log('ERROR',f'[{line}] Log failed: Expected at least 3 arguments')

        
    if command == 'set': 
        allargs = ''
        index = 0
        for i in args:
            if index == 0: pass
            else:
                if args[index] == 'GET':
                    args[index] = var[int(args[index+1])]
                    args[index+1] = ''
                allargs = allargs + args[index] + ' '
            index += 1
        var.append(allargs)
            
    if command == 'echo':
            print(Style.BRIGHT + Fore.WHITE + input(args[1]),end='')
            
            
    if command == 'input':
        var.append(input(args[1]))
        
    if command == 'get':
        if args[1] == 'GET':
            args[1] = var[int(args[2])]
            args[2] = ''
        print(Fore.WHITE + Style.BRIGHT + var[int(args[1])])
        
        
    if command == 'ask':
        allargs = ''
        index = 0
        for i in args:
            if index == 0: pass
            else: 
                if '\n' in args[index]: pass
                else: allargs = allargs + args[index] + ' '
            index += 1
        answ = input(Fore.WHITE + Style.BRIGHT + f'{ask_prefix} {allargs} ')
        var.append(answ)
        
    if command == 'if':
        global condition
        condition = False
        if var[int(args[1])] + '\n'== args[2]:
            condition = True
        
    if command == 'do':
        if condition == True:
            allargs = ''
            index = 0
            for i in args:
                if index == 0: pass
                else: allargs = allargs + args[index] + ' '
                index += 1
            execute(allargs,line)
            
    if command == 'else':
       if condition == False:
            allargs = ''
            index = 0
            for i in args:
                if index == 0: pass
                else: allargs = allargs + args[index] + ' '
                index += 1
            execute(allargs,line)
        
    if command == 'goto':
        return args[1]
        
    if command == 'sleep':
        if args[1] == 'GET':
            args[1] = var[int(args[2])]
            args[2] = ''
        t.sleep(int(args[1])/10)
        
    
    if command == 'math':
        if args[1] == '+':
            result = int(var[int(args[2])]) + int(var[int(args[3])])
        elif args[1] == '-':
            result = int(var[int(args[2])]) - int(var[int(args[3])])
        elif args[1] == '*':
            result = int(var[int(args[2])]) * int(var[int(args[3])])
        elif args[1] == '/':
            result = int(var[int(args[2])]) / int(var[int(args[3])])
        else:
            raise SyntaxError(f'Invalid math operator ({args[1]})\nValid options are [+, -, *, /]')
        var.append(str(result))
    
    
    if command == 'color':
        args[1].lower()
        if args[1] == 'blue':
            var.append(Fore.BLUE + var[args[2]])
        elif args[1] == 'red':
            var.append(Fore.RED + var[args[2]])
        elif args[1] == 'yellow':
            var.append(Fore.YELLOW + var[args[2]])
        elif args[1] == 'green':
            var.append(Fore.GREEN + var[args[2]])
        else: raise SyntaxError(f'Invalid color: [{args[1]}]\nValid options are [RED,BLUE,YELLOW]')
    
    
    
    
in_file = open('input.txt')


index = 0
content = in_file.readlines()
in_file.close()


if '#!/DEBUG-A\n' in content:
    debug = True
    print(' DEBUG A ON')
else:
    debug = False

if '#!/DEBUG-B\n' in content:
    debugb = True
    print(' DEBUG B ON')
else:
    debugb = False




index = 0
for i in content:
    index = index + 1
lines = index - 1
index = 0
while True:
    if index > lines: break
    try: 
        returned = None
        returned = execute(content[index],index)
        if returned == '': pass
        elif returned == None: pass
        else:
            index = int(returned) - 1
    except: 
        error = traceback.format_exc()
        print(Fore.RED + '----ERROR----')
        print(Fore.RED + error,end='')
        print(Fore.RED + '-------------')
    index +=1
    
    
    
print(Style.DIM + Fore.WHITE + '\n\n[PROGRAM END]')          
while True:
    answ = input('')
    execute(answ,0)
    try: exec(answ)
    except: pass
    try: execute(answ,0)
    except: pass
    if answ == 'Secret code!': print(Fore.WHITE + ':D you found an easter egg!')
    elif answ == ':D': print(Fore.WHITE + 'Lets be happy together! \n:D')
    elif 'egg' in answ: print(Fore.WHITE + answ)
    elif 'sus' in answ: print(Fore.WHITE + 'Ur sus!')
    elif answ == 'ok': print(Fore.WHITE + 'sus')
    elif answ == 'echo!': print(Fore.WHITE + 'echhhooooo!!!')
    elif 'among' in answ: print(Fore.WHITE + 'Among is among your message')
    elif 'E' in answ: print(Fore.WHITE + 'sussy message!!!')
    elif answ == 'restart': print(Fore.WHITE + 'restartting...')
