import numpy as np

class VorlaxParser(object):
    def loadFile(self):
        for line in self.VorFile:
            self.VorInfo.append(line)
            self.lineNum += 1

    def findPanelLoc(self):
        self.lineNum = 0
        for i in range(0, len(self.VorInfo)):
            if self.VorInfo[i].find("PANEL NO.") != -1: # beginning of panel
                if self.lineNum == 0:
                    self.panelLoc[0]=[i,0]
                else:
                    self.panelLoc.append([i,0])
                # print(self.VorInfo[i])
                self.lineNum += 1
            elif self.VorInfo[i].find("ITRMAX") != -1 and self.lineNum > 0:
                self.panelLoc.append([i,1])
                self.lineNum += 1

    def __init__(self, filePath):
        self.filePath = filePath
        self.VorFile = open(self.filePath,"r")
        self.VorInfo=[]
        self.PanInfo = [] # holds info for all panels. Use as container for panel parsing
        self.lineNum = 0
        self.panelLoc = [[]]
        # initialize file
        self.loadFile()
        # initialize panel locations
        self.findPanelLoc()
        self.panel =  np.zeros(shape = (self.panelLoc[1][0]-self.panelLoc[0][0],17))
        self.temp = []
        self.rowIter = 0
        self. colIter = 0
        self.lBound = 0

    def setOutPanel(self, panelLoc):
        self.panel = np.zeros(shape = (self.panelLoc[panelLoc+1][0]-self.panelLoc[panelLoc][0]-1,17))

    def getPanelLoc(self):
        return self.panelLoc

    def rowParse(self, panLoc): # Creates an array with the numbers in a line
        num = []
        for k in range(0, len(self.VorInfo[panLoc])):  # goes through an entire line
            a = self.VorInfo[panLoc][k]
            if a != " " and k != len(self.VorInfo[panLoc]) - 1:
                self.temp.append(self.VorInfo[panLoc][k])  # store numbers in temp array
            elif len(self.temp) != 0:
                num.append(
                    ''.join(self.temp))  # once it gets back to spaces, join temp array into 1 str => store in num
                # print(num)
                self.temp.clear()
                # after k loop, num will have all values for a line WORKS
        return num

    # Expects line to have 17 members
    def longParse(self, panLoc, panNum):
        rowVect = np.zeros(shape = (1,17)) # create temporary vector for storing numbers
        num = self.rowParse(panLoc) # get all numbers in a specific line
        for col in range(0, len(num)):
            # self.panel[panNum][col] = (float(num[col]))
            rowVect[0][col] = (float(num[col]))
        return rowVect

    # Expects line to have 11 members
    def shortParse(self, panLoc, panNum):
        rowVect = np.zeros(shape=(1, 17))
        num = self.rowParse(panLoc)
        for col in range(0, len(num)):
            if(col < 10) :
               # self.panel[panNum][col] = (float(num[col]))
                rowVect[0][col] = float(num[col])
            elif(col == 10):
                # print(num[11])
                # self.panel[panNum][14] = float(num[11]);
                rowVect[0][14] = float(num[10])
            else:
                # self.panel[panNum][col] = float(0)
                rowVect[0][col] = float(0)
        return rowVect

    # Segment parse inside a panel
    def segParse(self, panel, startLoc, endLoc, type):
        iter = 0
        for j in range(self.panelLoc[panel][0]+startLoc, self.panelLoc[panel][0] + endLoc):
            if type == "long":
                self.panel[iter] = self.longParse(j, iter)
                iter += 1
            else:
                self.panel[iter] = self.shortParse(j, iter)
                # print(self.panel[iter])
                iter+=1
        return self.panel

    def panParse(self, panel):
        if(self.panelLoc[panel][1] != 1):
            self.setOutPanel(panel)
            iter = 0
            for j in range(self.panelLoc[panel][0]+1, self.panelLoc[panel+1][0]):
                self.panel[iter] = self.shortParse(j, iter)
                if iter == 0:
                   # print("Longparse\t", self.panel[iter], "\n")
                    self.panel[iter] = self.longParse(j, iter)
                elif self.panel[iter-1][1] > self.panel[iter][1]:
                    self.panel[iter] = self.longParse(j, iter)
                  #  print("Longparse\t",self.panel[iter],"\n")
                #print(self.panel[iter-1][1],"\t", self.panel[iter][1])
                iter+=1
            return self.panel
        else:
            print("ERROR: PANEL INDEX IS AN END POINT")
            return([0])

    def Parse(self):
        for i in range(0,len(self.panelLoc)):
            if(self.panelLoc[i][1] == 0):
                self.PanInfo.append(self.panParse(i))

