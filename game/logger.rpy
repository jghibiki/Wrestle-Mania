init python:
    import os
    import datetime
    from inspect import currentframe, getframeinfo
    
    class Logger(store.object):
        
        instances = []
        
        
        def __init__(self, fileLoc, verbosity=True, failQuietly=False, allowGameDir=False):
            self.fileLoc = fileLoc
            self.failQueitly = failQuietly
            self.allow_game_dir = allowGameDir

            fw = self.openFile(self.fileLoc, "w")
            
            fw.write("File initialization completed...")
            fw.close()
            self.psp()
            
            self.tags = {}
            self.tags["__main__"] = verbosity
            
            self.indentSize = 0
            #add instance to instance list
            Logger.instances.append(self)
                            
                            
        def writeTo(self, textString, indent=0, verbose=True, shift=None, tag=None):
            if tag != None:
                try:
                    tagValue = self.tags[tag]
                except:
                    tagValue = True
            else:
                tagValue = True
            
            if self.tags["__main__"] and tagValue:
                fa = self.openFile(self.fileLoc, "a")
                                
                indentSize = ""
                if indent != 0:
                    for i in xrange(indent):
                        indentSize += "\t"
                else:
                    for i in xrange(self.indentSize):
                        indentSize += "\t"
                if shift == "up":
                    indentSize += "\t"
                elif shift == "down":
                    if indentSize > 0:
                        indentSize = indentSize[:-1]
                
                fa.write("[" + unicode(datetime.datetime.now()) + "] " + indentSize + str(textString) + "\n")
                fa.close()
            else:
                if not verbose:
                    fa = self.openFile(self.fileLoc, "a")
                    
                    indentSize = ""
                    if indent != 0:
                        for i in xrange(indent):
                            indentSize += "\t"
                    else:
                        for i in xrange(self.indentSize):
                            indentSize += "\t"
                    if shift == "up":
                        indentSize += "\t"
                    elif shift == "down":
                        if indentSize > 0:
                            indentSize = indentSize[:-1]
                    
                    self.fa.write("[" + unicode(datetime.datetime.now()) + "] " + indentSize + str(textString) + "\n")
                    self.fa.close()
                    
        def up(self):
            self.indentSize += 1
                
        def down(self):
            if self.indentSize > 0:
                self.indentSize -= 1
        
        def setVerbosity(self, newValue):
            self.verbosity = newValue
            
        def getVerbosity(self):
            return self.verbosity

        def mute(self):
            self.setVerbosity(False)
        
        def unmute(self):
            self.setVerbosity(True)
            
        def newTag(self, tag, value=False):
            if not self.tags.has_key("tag"):
                try:
                    self.tags[tag] = value
                except NameError:
                    self.tags[tag] = False
        
        def setTag(self, tag, value):
            if self.tags.has_key(tag):
                self.tags[tag] = value

        #format macros
     
        def insertLabel(self, label):
            #new in V2.0, the function must open the file in append mode and close it when done
            
            fa = self.openFile(self.fileLoc, "a")
            
            splatLen = len(label) + 4 #+4 is for a space on either side and an asterisk on both sides of the string
            
            for x in xrange(splatLen):
                fa.write("*")
                
            fa.write("\n")
            
            fa.write("* " + label + " *\n")
            
            for x in xrange(splatLen):
                fa.write("*")
            fa.write("\n")
            fa.close()
            
            
        
        def pump(self):
            fa = self.openFile(self.fileLoc, 'a')
            fa.write("\n")
            fa.close()
        
        def dpump(self):
            self.pump()
            self.pump()
        
        def splat(self):
            fa = self.openFile(self.fileLoc, "a")
            fa.write("************************************************************************************\n")
            fa.close()
        
        def dsplat(self):
            self.splat()
            self.splat()

        def psp(self):
            self.pump()
            self.splat()
            self.pump()
        
        def pdsp(self):
            self.pump()
            self.dsplat()
            self.pump()
                
        def repeat(self, input): #takes string or char and repeats it until the output string is 84 characters long, set to match the splat length
            fa = self.openFile(self.fileLoc, "a")
            inputSize = len(input)
            defaultWidth = 84
            printfull = 84/inputSize
            printLeftOver = 84%inputSize
            outputString = ""
            for x in xrange(printfull):
                outputString += input
            for x in xrange(printLeftOver-1):
                outputString += input[x]
            fa.write(outputString)
            fa.close()
            
        
        def failQuietly(self):
            self.failQuetly = True
            
        def failLoudly(self):
            self.failQuietly = False
            
        
        def openFile(self, fileLoc, mode):
            try:
                f = open(store._config.gamedir + "/logs/" + self.fileLoc, mode)
            except IOError:
                if self.allow_game_dir:
                    try:
                        f = open(store._config.gamedir + self.fileLoc, mode)
                    except IOError:
                        if not failQuietly:
                            self.error("Logger file was not found at:\n" + self.fileLoc + "\nor\n" + store._config.gamedir + self.fileLoc)
                        else:
                            return
                else:
                    if not self.failQuietly:
                        self.error("Logger file was not found at:\n" + self.fileLoc + "\nor\n" + store._config.gamedir + self.fileLoc)
                    else:
                        return            
            return f
                    

            
                            
                            
    ##################################################################################
    ## Error Logging


    #Syntax for getting the frame info :

    #        from inspect import currentframe, getframeinfo
    #        frameinfo = getframeinfo(currentframe())
    #        msg = "For whatever reason, no file was loaded."
    #        myLogger.error(msg, frameinfo, True)

    def postError(msg, log=True, frameinfo=None):
        if log:
            logError(msg, frameinfo)
        renpy.error(str(msg))
                
                

    def logError(msg, frameinfo):
        if frameinfo != None:
            for x in xrange(len(Logger.instances)):
                        Logger.instances[x].pump()
                        Logger.instances[x].dsplat()
                        Logger.instances[x].writeTo("\n\n************\nError!\nAt line: " + str(frameinfo.lineno) + 
                                                           "\nin file: " + str(frameinfo.filename) + 
                                                           "\nError message: " + msg)
        else:
            for x in xrange(len(Logger.instances)):
                        Logger.instances[x].pump()
                        Logger.instances[x].dsplat()
                        Logger.instances[x].writeTo("\n\n************\nError!\n" +
                                                           "Error message: " + str(msg))   
        
