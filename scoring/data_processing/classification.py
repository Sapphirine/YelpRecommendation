#!/usr/bin/env python
# ECBM E4040 Neural Networks and Deep Learning
# This is a utility function to help you download the dataset and preprocess the data we use for this homework.
# requires several modules: _pickle, tarfile, glob. If you don't have them, search the web on how to install them.
# You are free to change the code as you like.

# Import modules. If you don't have them, try `pip install xx` or `conda
# install xx` in your console.
import _pickle as pickle
import os
import tarfile
import glob
import urllib.request as url
import numpy as np
from scipy import misc



def load_data(mode='all'):
    """
    Unpack the CIFAR-10 dataset and load the datasets.
    :param mode: 'train', or 'test', or 'all'. Specify the training set or test set, or load all the data.
    :return: A tuple of data/labels, depending on the chosen mode. If 'train', return training data and labels;
    If 'test' ,return test data and labels; If 'all', return both training and test sets.
    """
    # If the data hasn't been downloaded yet, download it first.
    
    # Go to the location where the files are unpacked
    root_dir = os.getcwd()

    os.chdir('Ugly')
    train_data = []
    train_label = []
    test_data = []
    test_label = []
    try:
        for image_path in glob.glob("*"):
            image = misc.imread(image_path)
            #print(image.shape)
            

            test_data.append(image)
            test_label.append(0)
    except BaseException:
        print('Something went wrong...')
        return None
        # Turn the dataset into numpy compatible arrays.
    os.chdir(root_dir)
    os.chdir('Good')
    try:
        for image_path in glob.glob("*"):
            image = misc.imread(image_path)
            #print(image.shape)
            

            test_data.append(image)
            test_label.append(1)
    except BaseException:
        print('Something went wrong...')
        return None
    
    os.chdir(root_dir)
    os.chdir('classification/1')
    try:
        for image_path in glob.glob("*"):
            image = misc.imread(image_path)
            #print(image.shape)
            

            train_data.append(image)
            train_label.append(0)
    except BaseException:
        print('Something went wrong...')
        return None

    os.chdir(root_dir)
    os.chdir('classification/2')
    try:
        for image_path in glob.glob("*"):
            image = misc.imread(image_path)
            #print(image.shape)
            

            train_data.append(image)
            train_label.append(1)
    except BaseException:
        print('Something went wrong...')
        return None

    os.chdir(root_dir)
    os.chdir('classification/3')
    try:
        for image_path in glob.glob("*"):
            image = misc.imread(image_path)
            #print(image.shape)
            

            train_data.append(image)
            train_label.append(2)
    except BaseException:
        print('Something went wrong...')
        return None

    os.chdir(root_dir)
    os.chdir('classification/4')
    try:
        for image_path in glob.glob("*"):
            image = misc.imread(image_path)
            #print(image.shape)
            

            train_data.append(image)
            train_label.append(3)
    except BaseException:
        print('Something went wrong...')
        return None

    os.chdir(root_dir)
    os.chdir('classification/5')
    try:
        for image_path in glob.glob("*"):
            image = misc.imread(image_path)
            #print(image.shape)
            

            train_data.append(image)
            train_label.append(4)
    except BaseException:
        print('Something went wrong...')
        return None

    train_data = np.asarray(train_data)
    train_label = np.asarray(train_label)
    test_data = np.asarray(test_data)
    test_label = np.asarray(test_label)
    os.chdir(root_dir)
    if mode == 'train':
        return train_data, train_label
    elif mode == 'test':
        return test_data, test_label
    elif mode == 'all':
        return train_data, train_label, test_data, test_label
    else:
        raise ValueError('Mode should be \'train\' or \'test\' or \'all\'')
