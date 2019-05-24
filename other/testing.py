#!/usr/bin/env python3
# EEG to speech (non-invasive)
# Excerpt by John Melody Melissa Eskholazht
import os as M
import re
import time as T
import pygame as speech
import subprocess as sub

# Load the DATA:
userFileDir = input("Please Do Enter The File Directory:  ")
assert M.path.exists(userFileDir), "Try Again, please. " +str(userFileDir)
# Data Clariffication:
newData = open(userFileDir, "r+")
existingData = open("/home/johnmelodyme/Documents/API/AI/Data/JMEOG_FWRD_3EB.txt", "r+")
# Data Matching:
for line1 in newData:
        for line2 in existingData:
                # Play the voice data if DATA Matched:
                if line1 == line2:
                        print()
                        print("RECEIVING.......")
                        player = sub.Popen(["mplayer", "/home/johnmelodyme/Documents/API/AI/Sounds/123_1.mp3", "-ss", "30"], stdin=sub.PIPE, stdout=sub.PIPE, stderr=sub.PIPE)
                        T.sleep(3)
                        player.stdin.write(q)