# -*- coding: utf_8 -*-
import os
import argparse
import shutil
import csv

import numpy as np
import pandas as pd


def generate_train_data(training_file, divide_value):
    dir_name = './training_data/'

    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.mkdir(dir_name)

    input_file = training_file

    df_stock = pd.read_csv(input_file, encoding="shift-jis", header=1)

    df_stock_2 = df_stock[['始値', '高値', '安値', '終値', '出来高', '終値調整値']].apply(np.log) / 100

    divide_value = divide_value
    loop_range = int(df_stock_2.shape[0] / divide_value)

    validate = int(loop_range * 0.1)

    files_name = []
    labels = []
    for i in range(loop_range):
        start = i * divide_value
        end = (i + 1) * divide_value
        write_file_name = dir_name + 'data_' + str(i) + '.csv'
        if ((end+1) < df_stock['終値'].shape[0]):
            df_stock_2[start:end].to_csv(write_file_name, header=None, index=None)
            files_name.append(write_file_name)
            labels.append(int(df_stock['終値'].iloc[(end+1)]) / 1000)

    # print (labels)
    # print (files_name)

    f_train = open('stock_train.csv', 'w')
    writer_train = csv.writer(f_train, lineterminator='\n')

    f_validation = open('stock_validation.csv', 'w')
    writer_validation = csv.writer(f_validation, lineterminator='\n')

    header = ['x:data', 'y:label']
    writer_train.writerow(header)
    writer_validation.writerow(header)

    for i, (file, label) in enumerate(zip(files_name, labels)):
    #         print (i, file, label)
        if (i < (len(files_name) - validate)):
            writer_train.writerow((file, label))
        if (i >= (len(files_name) - validate)):
            writer_validation.writerow((file, label))

    f_train.close()
    f_validation.close()

    print("Complete !")


def gererate_evaluation_data(evaluation_file, divide_value):
    dir_name = './evaluation_data/'

    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.mkdir(dir_name)

    input_file = evaluation_file

    df_stock = pd.read_csv(input_file, encoding="shift-jis", header=1)

    df_stock_2 = df_stock[['始値', '高値', '安値', '終値', '出来高', '終値調整値']].apply(np.log) / 100

    divide_value = divide_value
    loop_range = int(df_stock_2.shape[0])

    files_name = []
    labels = []
    for i in range(loop_range):
        start = i * divide_value
        end = (i + 1) * divide_value
        write_file_name = dir_name + 'data_' + str(i) + '.csv'
        if ((end+1) < df_stock['終値'].shape[0]):
            df_stock_2[start:end].to_csv(write_file_name, header=None, index=None)
            files_name.append(write_file_name)
            labels.append(int(df_stock['終値'].iloc[(end+1)]) / 1000)

    # print (labels)
    # print (files_name)

    f_evaluation = open('stock_evaluation.csv', 'w')
    writer_evaluation = csv.writer(f_evaluation, lineterminator='\n')

    header = ['x:data', 'y:label']
    writer_evaluation.writerow(header)

    for i, (file, label) in enumerate(zip(files_name, labels)):
        writer_evaluation.writerow((file, label))

    f_evaluation.close()

    print("Complete !")


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--training_file', '-t', type=str)
    parser.add_argument('--evaluation_file', '-e', type=str)
    parser.add_argument('--divide_value', '-d', type=int)
    args = parser.parse_args()

    if args.training_file is None:
        training_file = '6502_2016.csv'
    if args.evaluation_file is None:
        evaluation_file = '6502_2017.csv'
    if args.divide_value is None:
        divide_value = 5

    generate_train_data(training_file, divide_value)
    gererate_evaluation_data(evaluation_file, divide_value)


if __name__ == '__main__':
    main()