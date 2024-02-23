# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:23:44 2021

@author: brend

Hello!
This program takes a paragraph provided by the user and finds its average sentence length, percent hard words,
average number of syllables, and readability using two seperate indices.
"""


import syllables as b

text=input('Enter a paragraph => ')
print(text)

stext=text.split('.')
stnum=len(stext)-1


wtnum = 0
hwnum = 0
syltnum = 0 
hwlist = []
#start

wtext=text.split()
wtnum=len(wtext) #finds the total number of words
j = 0 

while j < wtnum: #increments for each word in the sentence 
    syltnum_temp = b.find_num_syllables(wtext[j]) #finds the number of syllables in this word 
    
    if syltnum_temp >= 3 and wtext[j].find('-') == -1 and wtext[j].find('es',-2) == -1 and wtext[j].find('ed',-2) == -1:
        hwlist.append(wtext[j])
        hwnum += 1
        
    syltnum += syltnum_temp #finds the total number of syllables
    j+=1
    
       

ASL = wtnum/stnum
PHW = hwnum/wtnum*100
ASYL = syltnum/wtnum
GFRI = 0.4*(ASL + PHW)
FKRI = 206.835-1.015*ASL-86.4*ASYL



print('Here are the hard words in this paragraph: \n{}'.format(hwlist))
print('Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}'.format(ASL,PHW,ASYL))
print('Readability index (GFRI): {:.2f}'.format(GFRI))
print('Readability index (FKRI): {:.2f}'.format(FKRI))