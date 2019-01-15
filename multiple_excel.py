import xlrd

#for name, sheet_name in zip('multiple.xlsx', 0):
def read(sheet_name):
    book = xlrd.open_workbook('multiple.xlsx')
    sheet = book.sheet_by_name(sheet_name)
    values = []
    for row in range(sheet.nrows):
        col_value = []
        for col in range(sheet.ncols):
            value  = (sheet.cell(row,col).value)
            try: value = str(int(value))
            except : pass
            col_value.append(value)
           # print(col_value)
        values.append(col_value)

    print (values[1][2])
    print(values[1][1])
    print(values)
if __name__ == '__main__':
    read('Salas')