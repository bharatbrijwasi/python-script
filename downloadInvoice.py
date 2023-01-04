import pandas as pd
import openpyxl
import wget

def writeDownloadedFile(wfileName, ind):
    test = excelSheet.active
    c1 = test.cell(ind, 2)
    c1.value = wfileName
    

def downloadFile(URL, fileName, ind):
  response = wget.download(URL, fileName)
  if response == fileName:
      writeDownloadedFile(fileName, ind)
  else :
      print(response)

excelSheet = openpyxl.load_workbook("rr.xlsx")
dataFile = pd.read_excel('rr.xlsx', sheet_name='sheet')
for ind in dataFile.index:
	downloadFile(dataFile['Doc URL'][ind], dataFile['File'][ind], ind)

excelSheet.save("rr.xlsx")