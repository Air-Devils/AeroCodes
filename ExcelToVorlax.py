from Lib import VorlaxParser
from Lib import ExcelParser
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import subprocess
import shlex
import os

Tk().withdraw()
eParseFile = askopenfilename()
#outDir = askdirectory()
outFileName = input("Please input vorlax file name: ")
#vorOutFileName = input("please input output file name: ")
#outFileLoc = outDir + "/" + outFileName
outFileLoc = outFileName
#print(outFileLoc)

excelParser = ExcelParser.ExcelParser(eParseFile, outFileLoc)
excelParser.parseMain()
for i in range(1,excelParser.numOfPans):
    excelParser.parsePanel(i)
excelParser.parseEnd()

#command1 = "cmd.exe /K cd " + outDir + "\n"
#command1 = "vorlax.exe < " + outFileName + " > " + vorOutFileName + "\n\r"
#print(command1)

#print (command2)
#p = subprocess.Popen("cmd.exe dir", stdout=subprocess.PIPE, stderr = subprocess.PIPE)
#os.system(command1)
#subprocess.call(command1)
#subprocess.call(command2)
#args = shlex.split(command)
#print(args)
#p = subprocess.Popen(args, stdout=subprocess.PIPE)
#p = subprocess.Popen(command, stdout=subprocess.PIPE)

#print(p.communicate())

#p = subprocess.Popen("cmd.exe", stdin = subprocess.PIPE, stdout = subprocess.PIPE)
#stdout, stderr = p.communicate(command)
#print(stdout)
#print(p.communicate())
#vorParse = VorlaxParser.VorlaxParser(os.getcwd()+"/vorlax.LOG")

#vorParse.Parse()
#print(vorParse.PanInfo[1]) #get info for panel index 1
#for i in range(0,len(vorParse.panelLoc)):
  #  print(i, "\t", vorParse.panelLoc[i])
 #   vorParse.panParse(i)
#for i in range(0,len(vorInfo)):
#    print(vorInfo[i])