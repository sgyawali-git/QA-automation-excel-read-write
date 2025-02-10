import openpyxl
test_location = r"C:\Users\A C E R\PycharmProjects\Python Learning\swag_lab\read.xlsx"
def readexcel():
    wb = openpyxl.load_workbook(test_location)
    ws = wb["Sheet1"]

    for col in ws.iter_rows(min_row=2,values_only=True):
        sn,TS,xpath,action,value = col
        print(sn,TS,xpath,action,value)
readexcel()