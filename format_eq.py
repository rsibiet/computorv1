#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

import sys
import os

def remove_stars(tab):
    for elt in tab:
        if elt == "*":
            tab.remove("*")

def remove_sign(tab):
    i = 1
    while i < len(tab):
        if tab[i - 1] == "-":
            if type(tab[i]) != str:
                tab[i] *= -1
            else:
                tab[i] = "-" + tab[i]
            tab[i - 1] = "+"
        i += 1

def put_to_left(tab):
    i = 1
    side = 1
    while i < len(tab):
        if tab[i] == "=":
            side = -1
            tab[i] = "+"
        if side == -1 and tab[i - 1] == "+":
            if type(tab[i]) != str:
                tab[i] *= -1
            elif tab[i][0] == 'X':
                tab[i] = "-" + tab[i]
            else:
                tab[i] = tab[i][1::]
        i += 1

def reduce_me(tab):
    i = 0
    while i < len(tab):
        if tab[i] == "X^0":
            tab[i] = 1
        elif tab[i] == "-X^0":
            tab[i] = -1
        if i > 0 and type(tab[i]) != str and type(tab[i - 1]) != str:
            tab[i] = tab[i] * tab[i - 1]
            del tab[i - 1]
        elif tab[i] == "X":
            tab[i] = "X^1"
        elif tab[i] == "-X":
            tab[i] = "-X^1"
        i += 1

def sort_me(tab, p):
    i = 0
    while i < p.degree:
        p.res.append(0)
        i += 1
    i = 0
    while i < len(tab):
        if (i + 1) == len(tab) or tab[i + 1] == "+":
            if type(tab[i]) != str:
                p.res[0] += tab[i]
            elif i > 0 and type(tab[i - 1]) != str:
                p.res[int(tab[i][2])] += tab[i - 1]
            elif i == 0 or tab[i - 1] == "+":
                if tab[i][0] == '-':
                    p.res[int(tab[i][3])] -= 1
                else:
                    p.res[int(tab[i][2])] += 1            
        i += 1
    nb_neg = 0
    i = 0
    for elt in p.res:
        if elt < 0:
            nb_neg += 1
    if nb_neg > (len(p.res) / 2):
        while i < len(p.res):
            p.res[i] *= -1
            i += 1

def format_reduced_form(p):
    i = 0
    tmp = 1
    while i < len(p.res):
        if p.res[i] != 0:
            if i > 0 and p.res[i] > 0 and p.reduc != "":
                p.reduc += " + "
            elif i > 0 and p.reduc != "":
                p.reduc += " - "
                tmp *= -1
            p.reduc += str(p.res[i] * tmp)
            tmp = 1
            if i == 1:
                p.reduc += " * X"
            if i > 1:
                p.reduc += " * X^" + str(i)
        i += 1
    tmp = 0
    i = 0
    p.degree = 0
    while i < len(p.res):
        if p.res[i] != 0:
            tmp += 1
            p.degree = i
        i += 1
    if tmp == 0:
        p.reduc = "0"
    else:
        p.reduc += " = 0"












