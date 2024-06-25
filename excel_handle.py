import pandas as pd


def handle():
    # 读取用户上传的文件
    file_path = '/Users/tomato/Desktop/日常项目进项统计2.xlsx'
    df = pd.read_excel(file_path, header=0)

    # 显示文件的前几行以了解其结构和内容
    # head = df.head()

    # 获取excel的列标题名称
    columns = df.columns
    print(columns)

    # 获取某列数据df_obj[col_idx] 或df_obj.col_idx
    colData = df['菜品']
    print(colData)


def handle2(file_name, sheet_name):
    # 读取Excel文件
    df = pd.read_excel(file_name, sheet_name=sheet_name, skiprows=1)

    # 获取列标题
    # column_titles = df.columns

    # 输出列标题
    # print(column_titles)

    # 对"A"列进行分组，并对数量合计列进行求和
    # df_sum = df.groupby('菜品')['总计'].sum().reset_index()

    df_sum = df.groupby('    日期\n品名').sum().reset_index()

    # 输出结果
    # print(df_sum)

    # 创建一个ExcelWriter对象，并写入结果到新的Sheet
    with pd.ExcelWriter(file_name, mode='a', if_sheet_exists='replace') as writer:
        newSheetName = sheet_name + '_合计'
        df_sum.to_excel(writer, sheet_name=newSheetName, index=False)


def batchExcel(file_path):
    # 读取Excel文件
    sheets = pd.read_excel(file_path, sheet_name=None)

    # 获取所有的sheet名
    # sheets.items()
    for sheet_name, sheet_data in sheets.items():
        print(sheet_name)
        # 处理每个sheet
        handle2(file_path, sheet_name)


if __name__ == '__main__':
    handle()
    # handle2('/Users/tomato/Desktop/2023学年第二学期食物统计表_副本.xlsx', '新 5月')

    # batchExcel('/Users/tomato/Desktop/副本2023学年第二学期食物统计表.xlsx')
