import pandas as pd
import openpyxl
import wget
import xlsxwriter
import requests
from requests.auth import HTTPBasicAuth
def downloadFile(url, fileName, basic):
    try:
        response = requests.get(url, stream = True, allow_redirects=True, auth=basic) #add auth=basic for authorization
        if response.status_code == 200:
            print(fileName)
            print("File downloading status: ",response.status_code)
            with open(fileName, "wb") as pdf:
                pdf.write(response.content)
                return fileName
        else :
            print(response.status_code)
            print("error")
            return response.status_code
    except:
        return 401


def readFile(basic):
    
    print("Enter Name of File:")
    sourceFile =  input()
    print("Enter sheet name:")
    sheet_name = input()
    df = pd.read_excel(sourceFile, sheet_name = sheet_name)
    Status = ''
    successCount = 0
    errorCount = 0
    df['Status'] = Status
    df['successCount'] = successCount
    df['errorCount'] = errorCount

    for index in df.index:
        fileName = downloadFile(df['Doc URL'][index], str(df['File'][index])+str(df['Airtel Reference Number'][index])+str('.pdf'), basic)
        if fileName == str(df['File'][index])+str(df['Airtel Reference Number'][index])+str('.pdf'):
            df['Status'][index] = fileName
            successCount +=1
            print("Error Count...............................................................................", errorCount)
            print("Total File Downloaded.....................................................................", successCount)
            print()
        else :
            print("Error while downloadind file...")
            print()
            df['Status'][index] = 'Error'
            errorCount +=1
            print("Error Count...............................................................................", errorCount)
            print("Total File Downloaded.....................................................................", successCount)
            print()
    df['successCount'] = successCount
    df['errorCount'] = errorCount
    return df


print("Enter Username:")
username = input()
print("password")
password = input()
basic = HTTPBasicAuth(username, password)
logsDF = readFile(basic)
logsDF.to_excel('logs.xlsx', sheet_name='summary')
