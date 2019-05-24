#!/usr/bin/env BASH
# EEG to speech (non-invasive) -- $RUN file 
# Excerpt by John Melody Melissa Eskholazht
###########################################################################
#
# Update And Upgrade:
# sudo apt-get update && sudo apt-get upgrade
#
###########################################################################
#
# Start The EEG programme: 
# Install WINE first :
#sudo apt-get install winetricks 
cd /home/johnmelodyme/Documents/API/AI/APPS/
wine 'STARLABS EEG Analysis.exe'
#
############################################################################
#
#
# Run the python - script:
cd /home/johnmelodyme/Documents/API/AI/
ls
python3 script.py
#
############################################################################

