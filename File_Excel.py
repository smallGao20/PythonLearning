import xlrd
import xlwt

def FileRead(name):
    data = xlrd.open_workbook(name)
    data.sheet_names()
    print("Sheets: ",data.sheet_names())

    table = data.sheet_by_name('Sheet1')
    print("行数：",table.nrows)
    print("列数：",table.ncols)

    for i in range (0,table.nrows):
        for j in range(0,table.ncols):
            cell = table.cell(i,j).value
            print(cell,"\t")
    # 通过行（左到右）-> 列（上到下）的方式遍历整个表格
    # 工作流程总结：
    # 1. 获取文件路劲
    # 2. 获取读取文件的”指针“
    # 3. 获取文件中的某表的表名
    # 4. 依靠表名得到表的行列数获取数据

def FileWrite(name,sum,work):
    data = xlwt.Workbook(encoding='utf-8')
    tablename = input("请输入文件名称")
    table = data.add_sheet(tablename)

    for i in range (0,sum):
        table.write(0,i,work[i])
    # 此处为创建的表名
    data.save(name)

    # 工作流程总结：
    # 1. 使用xlwt.Workbook()创建文件“指针“
    # 2. 使用add_sheet()添加工作表
    # 3. 依靠write（a,b,str）在表中表格插入数据
    # 4. 使用save(路径+文件名+文件类型)保存到指定路

def Create_Excel():
    str = (input("请输入第一列的各行的名称，各行名称使用#隔开"))
    data = str.split("#")
    # 各列内容读取
    length = len(data)
    # 列数获取
    filename1 = "D:\Py Work\Testing2.xls"
    FileWrite(filename1,length,data)



def FileUpdat(name):
    from xlutils.copy import copy
    from xlrd import open_workbook
    from xlwt import easyxf
    import os

    excel = filename
    rb = open_workbook(excel)
    x = rb.sheet_by_name("Sheet1")
    wb = copy(rb)

    table = wb.get_sheet("Sheet1")

    for i in range (0,x.nrows):
        for j in range (0,x.ncols):
            if j == 0 and i >= 1:
                table.write(i,j,i)

    os.remove(excel)
    wb.save(excel)

    # 工作例程说明：
    # 1. xlwt 只能创建并写入空表
    # 2. xlrd 只能读取已存在表
    # 3. 使用copy技术将已读取表全复制到新的写入表
    # 4. 利用修改指针修改复制得到的新表
    # 5. 删除被复制表，保存复制修改表
    # 6. 行列好读取 依赖于 xlrd
    # 7. 数据修改依赖于 xlwt
    # 8. 删除依赖于os.remove()
    # 9. 复制则依赖于from xlutils.copy import copy


# 测试用数据及函数调用（选择性使用）
filename = "D:\Py Work\工作簿1.xls"
# FileRead(filename)
# FileWrite(filename1)
#Create_Excel()
FileUpdat(filename)