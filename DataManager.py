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
     list =[]
     workbook= load_workbook(path)
     sheet=workbook['Driver']
     for row in sheet.iter_rows():
         for cell in row:
             if cell.value =="YES":
                 list.append(cell.row)
     return list


 def get_data_sheet_name(path):
    list=[]
    worksheet=load_workbook(path)['Driver']
    for item in DataManager.get_execution_flag_rownum(path):
        list.append(worksheet.cell(row=item,column=7).value)
    print(list)










#print(DataManager.getcellData('/my_Stuff/python/sheet1.xlsx','Sheet1',4,3).value)

# DataManager.get_execution_flag_rownum('/my_Stuff/python/Untitled 1.xlsx')

# print(DataManager.get_execution_flag_rownum('C:/python/DataMgmt.xlsx'))
DataManager.get_data_sheet_name('C:/python/DataMgmt.xlsx')









