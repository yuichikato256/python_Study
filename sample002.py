import pandas as pd
import pandas_datareader.data as web

# stooqから指定された証券コードの株価データを取得
def get_stock_data(code):
    code_data = str(code) + '.JP'
    data = web.DataReader(code_data, 'stooq').dropna()
    data = data.sort_index() # 最新データがトップに出るので日付でソート
    return data

# 指定された株価データをcsvとして出力
def save_csv(code, data):
    filename = './data/dir' + str(code) + '.csv'
    data.to_csv(filename, sep=',')

data = get_stock_data(7272)
save_csv(7272,data)
print(data)


# stooqから指定された証券コードの株価データを取得
def get_stock_data(code):
    code_data = str(code) + '.JP'
    data = web.DataReader(code_data, 'stooq').dropna()
    data = data.sort_index() # 最新データがトップに出るので日付でソート
    return data

# 指定された株価データをcsvとして出力
def save_csv(code, data):
    filename = './data/csv/' + str(code) + '.csv'
    data.to_csv(filename, sep=',')

data = get_stock_data(7272)
print(data)
