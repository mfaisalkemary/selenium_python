import openpyxl
from openpyxl import load_workbook
from openpyxl import worksheet

class DataManager:
 def getRowCount(path,sheetName):
    Workbook = load_workbook(path, use_iterators=True)
    return Workbook[sheetName].max_row


 def getColumnCount(self,path,sheetname):
     Workbook= load_workbook(path,sheetname)
     return Workbook[sheetname].max_column

 def getcellData(path,sheet,col,row):
     Workbook= load_workbook(path,sheet)
     return Workbook[sheet].cell(col,row)

 def get_execution_flag_rownum(path):
     workbook= load_workbook(path)
     sheet=workbook['Sheet1']
     for row in sheet.iter_rows():
         for cell in row:
             if cell.value =="y":
                 return (cell.row)







#print(DataManager.getcellData('/my_Stuff/python/sheet1.xlsx','Sheet1',4,3).value)

DataManager.get_execution_flag_rownum('/my_Stuff/python/Untitled 1.xlsx')











