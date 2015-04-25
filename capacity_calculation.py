'''
Created on Jan 5, 2015

@author: andreweckford
'''

import genMarkov
import sequence_probability as seq
import channelrhodopsin
import acetylcholine
import calmodulin
import numpy as np
import sys
from time import time

#test

def parseCommandLineArguments():
    if ((len(sys.argv) < 7) and ('-d' not in sys.argv)):
        print("Usage: python3 capacity_calculation.py (channel) (time step) (simulation time) (iterations) (outputs) (off probability) [flags]")
        print("channel - which transduction channel to use, valid choices are ChR2, ACh, and CaM")
        print("time step - discretization interval (in ms)")
        print("simulation time - total amount of time for each run of the simulation (in ms)")
        print("iterations - number of simulation runs to average over (integer greater than 0)")
        print("outputs - 0 if the channel outputs are equal to the receptor state, 1 if the channel outputs are equal to the ion channel state")
        print("off probability - the iid probability that the illumination source is off in each discrete time interval")
        print("Flags:")
        print('-d - debug, ignores other command line arguments, use at your own risk')
        print("-e - estimate the running time using these parameters, do not return a result")
        print('-t - append the running time to the result vector (has no effect if used with -e)')
        print('-v - append a variance estimate to the result vector (has no effect if used with -e)')
        exit()   
    
    if '-d' in sys.argv:
        debugFlag = True
        whichChannel = None
        bigDelta = None
        simTime = None
        itr = None
        whichMap = None
        p_off = None
    else:
        debugFlag = False
        whichChannel = sys.argv[1]
        bigDelta = float(sys.argv[2])
        simTime = int(sys.argv[3])
        itr = int(sys.argv[4])
        whichMap = int(sys.argv[5])
        p_off = float(sys.argv[6])
    
    estimate = False
    simTimer = False
    varFlag = False
    if '-e' in sys.argv:
        estimate = True
    if '-t' in sys.argv:
        simTimer = True
    if '-v' in sys.argv:
        varFlag = True
    
    return [bigDelta,simTime,itr,whichMap,p_off,estimate,simTimer,varFlag,debugFlag,whichChannel]

def getEstimate(n,itr,nOld,itrOld,startTime,endTime):
    timeEstimate = (endTime - startTime)*(nOld*itrOld)/(n*itr)
    result = ''
    sigDig = 0
    days = np.floor(timeEstimate / 86400)
    if (days > 0):
        result += str(int(days))
        result += ' days '
        if (days > 10):
            sigDig += 2
        else:
            sigDig += 1
        timeEstimate -= days*86400
    hours = np.floor(timeEstimate / 3600)
    if ((hours > 0) and (sigDig < 2)):
        result += str(int(hours))
        result += ' hours '
        if (hours > 10):
            sigDig += 2
        else:
            sigDig += 1
        timeEstimate -= hours*3600
    minutes = np.floor(timeEstimate / 60)
    if ((minutes > 0) and (sigDig < 2)):
        result += str(int(minutes))
        result += ' minutes '
        if (minutes > 10):
            sigDig += 2
        else:
            sigDig += 1
        timeEstimate -= minutes*60
    if (sigDig < 2):
        seconds = np.floor(timeEstimate)
        result += str(int(seconds))
        result += ' seconds'
    print(result)

def main():

    startTime = time()
    [bigDelta,simTime,itr,whichMap,p_off,estimate,simTimer,varFlag,debugFlag,whichChannel] = parseCommandLineArguments()
            
    # give some default arguments for testing
    if (debugFlag is True):
        whichChannel = 'ACh'
        n = 5000
        itr = 10
        bigDelta = 0.02
        whichMap = 0
        p_off = 0.9
    else:
        n = int(simTime/bigDelta)
        
    if (estimate is True):
        nOld = n
        itrOld = itr
        n = 5000
        itr = 10
                
    if whichChannel is 'CaM':
        [P,Px,maps] = calmodulin.genP(bigDelta, bigDelta/p_off, bigDelta/(1-p_off))
    elif whichChannel is 'ACh':
        [P,Px,maps] = acetylcholine.genP(bigDelta, bigDelta/p_off, bigDelta/(1-p_off))
    elif whichChannel is 'ChR2':
        [P,Px,maps] = channelrhodopsin.genP(bigDelta, bigDelta/p_off, bigDelta/(1-p_off))
    else:
        raise ValueError('Invalid channel choice')
    
    mymap = maps[whichMap]
    allResults = []

    for _ in range(0,itr):

        x = genMarkov.generateMarkov(Px,n)
    
        z = genMarkov.getNonStationarySteadyStateDist(P,Px)

        y = genMarkov.generateNonStationaryHiddenMarkov(P, x, n, z[1], mymap)
        qqq = seq.log2NonStationaryConditionalProbability(P, y, x, z[1],mymap)/(-1*n)
        rrr = seq.log2NonStationaryOutputProbability(P, y, Px,mymap)/(-1*n)
        allResults.append((rrr-qqq)/bigDelta * 1000)
        #result += (rrr-qqq)/bigDelta * 1000

    
    endTime = time()
    result = np.mean(allResults)
    varEstimate = np.var(allResults)
    
    if (estimate is True):
        getEstimate(n,itr,nOld,itrOld,startTime,endTime)
    else:
        printOut = str(bigDelta)+","+str(simTime)+","+str(itr)+","+str(whichMap)+","+str(p_off)+","+str(result)
        if (simTimer is True):
            printOut += ","+str(endTime-startTime)
        if (varFlag is True):
            printOut += ","+str(varEstimate)
        print(printOut)
            
    
    
if __name__=="__main__":
    main()

