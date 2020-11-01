import xlrd
import xlwt

rwb = xlrd.open_workbook("成绩表.xlsx")
rsheet = rwb.sheet_by_index(0)

# 求所有学生的成绩的总分
rsheet.put_cell(0,4,xlrd.XL_CELL_TEXT,"总分",None)
nrows = rsheet.nrows
for row in range(1,nrows):
    grades = rsheet.row_values(row,1,4)
    total = sum(grades)
    rsheet.put_cell(row,4,xlrd.XL_CELL_NUMBER,total,None)

# 求每个科目的平均分
nrows = rsheet.nrows
ncols = rsheet.ncols
for col in range(1,5):
    grades = rsheet.col_values(col,1,nrows)
    avg = sum(grades)/len(grades)
    rsheet.put_cell(nrows,col,xlrd.XL_CELL_NUMBER,avg,None)


wwb = xlwt.Workbook()
wsheet = wwb.add_sheet("sheet1")
nrows = rsheet.nrows
ncols = rsheet.ncols
for row in range(0,nrows):
    for col in range(0,ncols):
        wsheet.write(row,col,rsheet.cell_value(row,col))

wwb.save("abc.xls")
