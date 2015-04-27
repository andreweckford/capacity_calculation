import sys
import numpy as np

def parseCommandLineArguments():
    if len(sys.argv) < 7:
        print("Usage: python3 generateScript.py (channel) (time step) (simulation time) (iterations) (outputs) (off probability) [flags] [--cores=n] [--python=]")
        print("Parameters and flags have the same meaning as in capacity_calculation; -e and -d are ignored.")
        print("Any parameter, except channel, flags, and cores, can be specified with a step and range, in MATLAB notation.")
        print("However, range only (e.g., 0:1) is only valid with integers, and would normally be used only with outputs.")
        print("If cores is provided, then n scripts are generated, which may be executed simultaneously.")
        print("The script has the name script1.sh, or if n cores, script1.sh, ..., scriptn.sh")
        exit()
        
    whichChannel = sys.argv[1]
    if '-t' in sys.argv:
        simTimer = True
    else:
        simTimer = False
    
    if '-v' in sys.argv:
        varFlag = True
    else:
        varFlag = False
    
    numCores = 1
    if any(['--cores=' in t for t in sys.argv]):
        for t in sys.argv:
            if '--cores=' in t:
                numCores = int(t.split('=')[1])
    
    pythonCommand = 'python3'
    if any(['--python=' in t for t in sys.argv]):
        for t in sys.argv:
            if '--python=' in t:
                pythonCommand = t.split('=')[1]
                
    parsedParameters = []
    for i in range(2,7):
        parsedParameters.append(parseParameter(sys.argv[i]))
        
    return (whichChannel,simTimer,varFlag,numCores,parsedParameters,pythonCommand)

def parseParameter(p):
    # parses whether the parameter is scalar or a range
    # returns a list either way
    pSplit = p.split(':')
    if len(pSplit) == 1:
        return [float(pSplit[0])]
    
    if len(pSplit) == 2:
        return list(range(int(pSplit[0]),int(pSplit[1])+1))
    
    if len(pSplit) == 3:
        # use np.float_ for high precision 
        count = np.float64(pSplit[0])
        inc = np.float64(pSplit[1])
        term = np.float64(pSplit[2])
        if (term >= count):
            keepGoing = True
            result = [count]
            while keepGoing:
                count += inc
                if ((count-term) < inc*1e-12): # otherwise it seems to ignore the == case due to funny number handling
                    result.append(count)
                else:
                    keepGoing = False
        else:
            result = []
        return result
    
    raise ValueError('Invalid parameter')

def main():
    p = parseCommandLineArguments()
    #print(p)

    whichChannel = p[0]
    
    if p[1] is True:
        simTimerString = ' -t'
    else:
        simTimerString = ''
    
    if p[2] is True:
        varFlagString = ' -v'
    else:
        varFlagString = ''
      
    numCores = p[3]
    
    pythonCommand = p[5]

    commands = []

    for timeStep in p[4][0]:
        for simulationTime in p[4][1]:
            for iterations in p[4][2]:
                for outputs in p[4][3]:
                    for offProbability in p[4][4]:
                        commands.append(pythonCommand+' capacity_calculation.py '+whichChannel+' '+str(timeStep)+' '+str(simulationTime)
                                        +' '+str(int(iterations))+' '+str(outputs)+' '+str(offProbability)+simTimerString+varFlagString)
                        
    
    perCore = int(np.ceil(len(commands)/numCores))

    for i in range(1,numCores+1):
        scriptString = 'script'+str(i)+'.sh'
        outFileString = ' result-'+whichChannel+'-'+str(i)+'.csv'
        f = open(scriptString,'w')
        #print('---'+scriptString+'---')
        f.write('rm'+outFileString+' 2>/dev/null\n')
        #print('rm'+outFileString+' 2>/dev/null')
        f.write('touch'+outFileString+'\n')
        #print('touch'+outFileString)

        for j in range((i-1)*perCore,min([len(commands),i*perCore])):
            f.write(commands[j]+' >>'+outFileString+'\n')
            #print(commands[j]+' >>'+outFileString)
            
        f.close()
            
if __name__ == "__main__":
    main()