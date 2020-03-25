# -*- coding:utf-8 -*-
import pandas as pd # excel用
import numpy as np


def main():
    # csvファイルの読み込み
    df = pd.read_csv('loto6.csv'.encoding="cp932")
    # 当選数値だけを抽出
    df = df.iloc[:,2:8]

    #データセット作成
    dataset = pd.DataFrame(np.empty((df.shape[0],2), dtype = int))

    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if j == 0:
                dataset.loc[i,1] = str(df.iloc[i,j]) # excelから読み取ったやつの指定はiloc、自分で指定した配列はloc
            else:
                dataset.loc[i,1] = str(dataset.loc[i,1]) + str(df.iloc[i,j])

        dataset.loc[i,0] = i + 1

    # 名前を変えて保存
    dataset.to_csv("loto6_dataset.csv",header=None,index=False)


    # lstm用データセット作成
    num = 200 # 何個ごとに予測するか
    sub_dataset = pd.DataFrame(np.empty((num,2), dtype = int))

    #for i in range(0,df.shape[0],num):
    #    if i == 0:
    #        sub_dataset = dataset.shift(i * -num)
    #    else:
    #        sub_dataset.loc[:,1] = dataset.shift(-num)
    #    sub_dataset.to_csv("sub_dataset/loto6_sub_dataset" + str(i) + ".csv",header=None,index=False)

    #for i in range(num):
    #    sub_dataset.loc[i,0] = i

    dataset = dataset.shift(1)
    dataset.to_csv("sub_dataset/loto6_sub_dataset.csv",header= None,index=False)

if __name__ == '__main__':
    main()
