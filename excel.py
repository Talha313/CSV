from  xlrd import open_workbook
import xlrd

def read():
    wb = xlrd.open_workbook('input.xlsx')
    #print(wb)

    for s in wb.sheets():
        values = []
        for row in range(s.nrows):
            col_value = []
            for col in range(s.ncols):
                value  = (s.cell(row,col).value)
                try: value = str(int(value))

                except : pass
                col_value.append(value)
           # print(col_value)
            values.append(col_value)

    #print (values[1][4])
    print(values)
if __name__ == '__main__':
    read()