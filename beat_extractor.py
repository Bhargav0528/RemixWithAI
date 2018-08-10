#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 23:06:46 2018

@author: bhargav-0528
"""

from scipy.io import wavfile
import numpy as np
from pydub import AudioSegment

def beat_extractor(n_beats):
    global i,j,k,beat_array
    while(j<n_beats):
        min_beats = np.ndarray(shape=(44100,1),dtype='int16')     
    
        for x in range(0,44100):
            min_beats[x] = wav[i]
            i = i+1
        
        mean = np.mean(min_beats)
        mean_array.append(mean)
        beat_array.append(min_beats)
        wavfile.write('Songs/output/att'+str(j)+'.wav',sr,beat_array[j])
        j=j+1
        
    
sound = AudioSegment.from_mp3("Songs/drums.mp3")
sound.export("test.wav", format="wav")
sound = sound.set_channels(1)
sound.export("test.wav", format="wav")
twe_sec = 20*1000
tew_song = sound[:twe_sec]
sound.export("test.wav", format="wav")



sr, wav = wavfile.read('test.wav')

beat_array, mean_array = [], []
i = sr;j=0;k=0;
beat_extractor(20)