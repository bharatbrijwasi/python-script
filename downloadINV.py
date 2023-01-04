import pandas as pd
import openpyxl
import wget


def writeStatus(fileName, index):
    wb = openpyxl.Workbook()
    sheet = wb.active
    c1 = sheet.cell(row = index, column = 5)
    c1.value = fileName
    wb.save("rr123.xlsx")
    
def downloadFile(url, fileName, index):
    response = wget.download(url, fileName)
    if response == fileName:
        print("Done")
        writeStatus(fileName, index)
    else :
        print("Error")

df = pd.read_excel('rr.xlsx', sheet_name = 'sheet')



for index in df.index:
    downloadFile(df['Doc URL'][index], df['File'][index], index)


