python ExcelToVorlax.py
set /p inFile= "Enter input file: "
set /p outFile= "Enter output file: "
vorlax.exe < %inFile% > %outFile%