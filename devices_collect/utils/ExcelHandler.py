import pandas as pd
import MySQLdb
import csv
from matplotlib import pyplot as plt
import numpy as np
import os
from devices_collect.utils import app_setting

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def insert2category():
    db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='my_system', charset='utf8')
    sql_cmd = '''insert into story_analysis_category(c_id, name) values (%s, '%s')'''
    cursor = db.cursor()
    files = ['../excels/category/' + i for i in ['个人直播_结合版_category.csv', '个人直播_category.csv', '花样直播_category.csv']]
    for file_path in files:
        csv_file = open(file_path, 'r', encoding='utf8')
        data = csv.reader(csv_file)
        for item in data:
            row = item[0]
            name, c_id = tuple(row.split('	'))
            cursor.execute(sql_cmd % (int(c_id), name))
        csv_file.close()
    db.commit()
    cursor.close()

def analysis_manufactor(file_name, target_rate=90.0, focus_col=r'机型', task_id=0):
    plt.figure(figsize=(10.0, 10.0))
    data = pd.read_excel(file_name)
    df = data[[focus_col, r'联网占比']].to_dict(orient='dict')
    rate = 0.0
    rates = []
    labels = []
    row, _ = data.shape
    for i in df[focus_col]:
        tmp_rate = df[r'联网占比'][i]
        labels.append(df[focus_col][i])
        rates.append(tmp_rate)
        rate += tmp_rate
        if rate >= target_rate:
            break
    # explode = (0, 0, 0.02, 0)
    colors = (plt.cm.prism(np.linspace(0.0, 1.0, len(rates))))
    patches, text1, text2 = plt.pie(rates,
                                    labels=labels,
                                    colors=colors,
                                    autopct='%3.2f%%',  # 数值保留固定小数位
                                    shadow=False,  # 无阴影设置
                                    startangle=90,  # 逆时针起始角度设置
                                    pctdistance=0.6)  # 数值距圆心半径倍数的距离
    name = file_name.split('\\')[-1].split('.')[0]
    plt.title(name)
    plt.savefig('../static/pictures/%s.png' % name)
    plt.close()

def mkdir(path):
    path=path.strip()
    is_exist = os.path.exists(path)
    if not is_exist:
        os.makedirs(path)
        return True
    else:
        return False

def handle_upload_file(f, task_name='0'):
    """

    :param f: 文件
    :param task_name: 任务路径名
    :return:
    """
    dir_path = app_setting.LANTERNS_PATH + task_name
    mkdir(dir_path)
    path = dir_path + '\\' + f.name
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


if __name__ == '__main__':
    files = ['NOW安卓品牌（2018-06-10 至 2018-07-09）.xls', 'NOW安卓机型（2018-06-10 至 2018-07-09）.xls',
             'NOW安卓系统（2018-06-10 至 2018-07-09）.xls', 'NOW苹果机型（2018-06-10 至 2018-07-09）.xls',
             'NOW苹果系统（2018-06-10 至 2018-07-09）.xls']
    for file in files:
        file_path = r'E:\papersoftware\mysite\devices_collect\excels\lanterns\\' + file
        analysis_manufactor(file_path)

