# -*- coding: utf-8 -*-
"""
Created on Sun May  8 00:18:02 2022

@author: 
"""
from tkinter import *

fenetre=Tk()
#on lui donne un titre
fenetre.title("Mastermind")
historique=Canvas(fenetre, width=310, height=450, bg='orange')
for i in range(1,11):
    historique.create_text((10,i*40), text=i, fill="black")
#on l'affiche
historique.pack()

propo=Canvas(fenetre, width=300, height=100, bg='orange')
propo.create_text((130,10), text='Votre proposition', fill="white")
propo.pack()

#ce que l'utilisateur doit deviner
objectif = []
#ce que l'utilisateur est entrain de proposer
proposition = []
#compteur de proposition
cmp=0
def validation():
    global objectif,proposition,cmp
    if len(proposition)==4:
        if len(objectif)==0:
            objectif=proposition
        else:
            if cmp<10:
                test(cmp)
            cmp+=1
    proposition=[]
    afficherpropo()
def test(i):
    global historique,objectif, proposition
    color=['blue','yellow','black','purple','white']
    for j in range(0,4):
        historique.create_rectangle((j+1)*40,(i+0.5)*40, (j+2)*40,(i+1.5)*40, fill=color[proposition[j]])
    if objectif==proposition:
        historique.create_rectangle(210,(i+0.5)*40,220,(i+1.5)*40, fill='green')
        historique.create_rectangle(230,(i+0.5)*40,240,(i+1.5)*40, fill='green')
        historique.create_rectangle(250,(i+0.5)*40,260,(i+1.5)*40, fill='green')
        historique.create_rectangle(270,(i+0.5)*40,280,(i+1.5)*40, fill='green')
    else:
        #pour ne pas perturber l'analyse on crée des copies
        nobj=objectif.copy()
        nprop=proposition.copy()
        #nombre de bonne position des couleurs
        nbcouleur=0
        for j in range(0,4):
            if objectif[3-j]==proposition[3-j]:
                nbcouleur+=1
                nobj.pop(3-j)
                nprop.pop(3-j)
        #nombre de bonne couleur mais dans le mauvais ordre
        nbordre=0
        nobj.sort()
        nprop.sort()
        for j in range(0,len(nobj)):
            if nobj[j] in nprop:
                nprop.remove(nobj[j])
                nbordre+=1
        for j in range(0,nbcouleur):
            historique.create_rectangle(210+j*20,(i+0.5)*40,220+j*20,(i+1.5)*40, fill='green')
        for j in range(0,nbordre):
            historique.create_rectangle(210+(nbcouleur+j)*20,(i+0.5)*40,220+(nbcouleur+j)*20,(i+1.5)*40, fill='grey')
                
def color0():
    global proposition
    if len(proposition)<4:
        proposition.append(0)
    afficherpropo()
def color1():
    global proposition
    if len(proposition)<4:
        proposition.append(1)
    afficherpropo()
def color2():
    global proposition
    if len(proposition)<4:
        proposition.append(2)
    afficherpropo()
def color3():
    global proposition
    if len(proposition)<4:
        proposition.append(3)
    afficherpropo()
def color4():
    global proposition
    if len(proposition)<4:
        proposition.append(4)
    afficherpropo()
def cancel():
    global proposition
    if len(proposition)>0:
        proposition.pop()
        afficherpropo()
def afficherpropo():
    global proposition,propo
    color=['blue','yellow','black','purple','white']
    #on efface les carrés précédents en les recouvrant
    for i in range(1,5):
        propo.create_rectangle(i*50,50, (i+1)*50,100, fill='orange')
    j=0
    for i in proposition:
        j+=1
        propo.create_rectangle(j*50,50, (j+1)*50,100, fill=color[i])
choix=Frame(fenetre)
B = Button(fenetre, bg='blue',width=5,command=color0).pack(side=LEFT)
Y = Button(fenetre, bg='yellow',width=5,command=color1).pack(side=LEFT)
BL = Button(fenetre, bg='black',width=5,command=color2).pack(side=LEFT)
R = Button(fenetre, bg='purple',width=5,command=color3).pack(side=LEFT)
R = Button(fenetre, bg='white',width=5,command=color4).pack(side=LEFT)
Supp= Button(fenetre,text='X', bg='red',width=5,command=cancel).pack(side=LEFT)
Supp= Button(fenetre,text='Valider', bg='green',width=5,command=validation).pack(side=LEFT)
choix.pack()
 
#on affiche la fenetre
fenetre.mainloop()