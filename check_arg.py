#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

import sys
import os

def check_nb(mystr):
    try:
        mystr = int(mystr)
        return (mystr)
    except:
        pass
    try:
        mystr = float(mystr)
        return (mystr)
    except:
        pass
    return (mystr)

def check_x(val, p):
    if len(val) == 1:
        p.degree = 1
        return True
    if len(val) != 3:
        return False
    try:
        tmp = int(val[2])
    except:
        return False
    if (p.degree < tmp):
        p.degree = tmp
    if val[1] != '^':
        return False
    return True

def check_operator(op, egual):
    if op != "+" and op != "-" and \
        op != "*" and op != "=":
        return False
    if op == "=":
        egual[0] += 1
    return True

def check_format(cut, p):
    i = 0
    egual = [0]
    while i < len(cut):
        nb_len = len(cut[i])
        pt_pos = 0
        while pt_pos < len(cut[i]) and cut[i][pt_pos] != '.':
            pt_pos += 1
        cut[i] = check_nb(cut[i])
        if (type(cut[i]) == float and (pt_pos > 10 or nb_len > 20)) or \
            (type(cut[i]) == int and nb_len > 10):
            print(cut[i], ": \033[91mis a number to big or not well formated.\033[0m")
            sys.exit()
        elif type(cut[i]) == str and cut[i][0] != 'X':
            print(cut[i], ": \033[91mis NOT a number.\033[0m")
            sys.exit()
        elif type(cut[i]) == str and cut[i][0] == 'X' and check_x(cut[i], p) == False:
            print(cut[i], ": \033[91mX value not well formated.\033[0m")
            sys.exit()
        i += 1
        if i == len(cut):
            break
        if check_operator(cut[i], egual) == False:
            print(cut[i], " \033[91mis not good operator.\033[0m")
            sys.exit()
        i += 1
        if i == len(cut):
            print("\033[91mError: Equation end by operator.\033[0m")
            sys.exit()
        elif cut[i - 1] != "*":
            continue
        elif type(cut[i - 2]) == str and cut[i] == "*":
            print(cut[i - 2], ": \033[91mX can not be followed by *.\033[0m")
            sys.exit()
        if check_x(cut[i], p) == False:
            print(cut[i], ": \033[91mis NOT X value well formated.\033[0m")
            sys.exit()
        i += 1
        if i == len(cut):
            break
        if check_operator(cut[i], egual) == False or cut[i] == "*":
            print(cut[i], " \033[91mis not good operator.\033[0m")
            sys.exit()
        i += 1
    if egual[0] > 1:
        print("\033[91mError: Several operator '=' found.\033[0m")
    if egual[0] == 0:
        print("\033[91mError: Missing operator '='.\033[0m")

def check_argv(argv):
    tab = "1234567890X^*-+=. "
    i = 0
    while i < len(argv):
        tmp = 0
        j = 0
        while j < len(tab):
            if argv[i] == tab[j]:
                tmp = 1
            j += 1
        if tmp != 1:
            print("\033[91mError: Equation not well formated.\033[0m")
            sys.exit()
        i += 1

