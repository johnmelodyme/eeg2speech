#!/usr/bin/env python3
# EEG to speech (non ivasive)
# Excerpt by John Melody 

import os as z
import matplotlib 
# from pygame import mixer # sudo apt-get install python-pygame
import time as y
import scipy.io as sc
from playsound import playsound

def inputedEEG():
    #mat = sc.loadmat('JMEOG_FWRD_3EB.m')
    f = open("JMEOG_FWRD_3EB.brt" ,"r")  # replace data.matlab with matlab data file
    if f.mode == 'r':
        f.read()
        f.close()

    newData = "JMEOG_FWRD_3EB.brt" # the input Data
    oldData = "JMEOG_RISING_2EB.brt" #Existing Data

    if newData == oldData:

        '''
        pygame.mixer.init()
        pygame.mixer.music.load('/home/johnmelodyme/Documents/API/AI/123.mp3')
        pygame.mixer.music.play()
        X.system('xdg-open /home/johnmelodyme/Documents/API/AI/123.mp3')
        X.system('clear')
        X.system('exit && exit')
        Y.sleep(2)
        pygame.mixer.music.istop()
        playsound('/home/johnmelodyme/Documents/API/AI/123.py')
        Y.sleep(2)
        '''

        z.system('xdg-open  \'/home/johnmelodyme/Documents/API/AI/123.mp3\'')
        y.sleep(3)
    else:
        z.system('xdg-open  \'/home/johnmelodyme/Documents/API/AI/321.mp3\'')
        y.sleep(2)
        return