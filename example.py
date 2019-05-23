#!/usr/bin/env python3
# EEG to speech (non-invasive)
# Excerpt by John Melody Melissa Eskholazht
import os as M
import re
import time as T

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
                        M.system("xdg-open /home/johnmelodyme/Documents/API/AI/Sounds/123.mp3")
                        break
                else:
                        print()
                        print("Please try again!")
                        M.system("xdg-open /home/johnmelodyme/Documents/API/AI/Sounds/false.mp3")   
                        break
                break
        break
