import csv
import pandas as pd
import argparse


# 配置.sh脚本文件输入内容
def parse_args():
    global script_path, proj_ios_path
    parser = argparse.ArgumentParser(description='获取git提交记录工具\n')
    parser.add_argument('--fileName', dest='fileName', type=str, required=False, help='文件名')
    parser.add_argument('--text', dest='text', type=str, required=False, help='屏蔽关键字组合')
    args = parser.parse_args()
    return args


def readCSV(path, fileName, masks):
    contentDic = {"日期": "内容"}
    with open(path, 'r') as f:
        contentReader = csv.reader(f)
        for row in contentReader:
            if any(x in row[1] for x in masks):
                continue
            time = pd.to_datetime(row[0]).strftime('%Y-%m-%d')
            if time in contentDic:
                contentDic.update({time: contentDic.get(time) + ";" + row[1]})
            else:
                contentDic.update({time: row[1]})
    f.close()
    with open(fileName, 'w') as fw:
        writer = csv.writer(fw)
        for key in contentDic.keys():
            writer.writerow([key, contentDic.get(key)])
    fw.close()


if __name__ == '__main__':
    global fileName
    app_args = parse_args()
    fileName = app_args.fileName
    maskText = app_args.text
    masks = maskText.split(',')
    readCSV('commit.csv', fileName, masks)
