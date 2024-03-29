#!/usr/bin/env/ python
# ECBM E4040 Fall 2017 Assignment 2
# This Python script contains various functions for layer construction.

import numpy as np


def affine_forward(x, w, b):
    """
    Computes the forward pass for an affine (fully-connected) layer.

    The input x has shape (N, d_1, ..., d_k) and contains a minibatch of N
    examples, where each example x[i] has shape (d_1, ..., d_k). We will
    reshape each input into a vector of dimension D = d_1 * ... * d_k, and
    then transform it to an output vector of dimension M.

    Inputs:
    :param x: A numpy array containing input data, of shape (N, d_1, ..., d_k)
    :param w: A numpy array of weights, of shape (D, M)
    :param b: A numpy array of biases, of shape (M,)

    :return:
    - out: output, of shape (N, M)
    - cache: x, w, b for back-propagation
    """
    num_train = x.shape[0]
    x_flatten = x.reshape((num_train, -1))
    out = np.dot(x_flatten, w) + b
    cache = (x, w, b)
    return out, cache


def affine_backward(dout, cache):
    """
    Computes the backward pass for an affine layer.
    :param dout: Upstream derivative, of shape (N, M)
    :param cache: Tuple of:
                    x: Input data, of shape (N, d_1, ... d_k)
                    w: Weights, of shape (D, M)

    :return: a tuple of:
    - dx: Gradient with respect to x, of shape (N, d1, ..., d_k)
    - dw: Gradient with respect to w, of shape (D, M)
    - db: Gradient with respect to b, of shape (M,)
    """
    x, w, b = cache

    N = x.shape[0]
    x_flatten = x.reshape((N, -1))

    dx = np.reshape(np.dot(dout, w.T), x.shape)
    dw = np.dot(x_flatten.T, dout)
    db = np.dot(np.ones((N,)), dout)

    return dx, dw, db


def relu_forward(x):
    """
    Computes the forward pass for a layer of rectified linear units (ReLUs).

    :param x: Inputs, of any shape
    :return: A tuple of:
    - out: Output, of the same shape as x
    - cache: x for back-propagation
    """
    out = np.zeros_like(x)
    out[np.where(x > 0)] = x[np.where(x > 0)]

    cache = x

    return out, cache


def relu_backward(dout, cache):
    """
    Computes the backward pass for a layer of rectified linear units (ReLUs).

    :param dout: Upstream derivatives, of any shape
    :param cache: Input x, of same shape as dout

    :return: dx - Gradient with respect to x
    """
    x = cache

    dx = np.zeros_like(x)
    dx[np.where(x > 0)] = dout[np.where(x > 0)]

    return dx


def softmax_loss(x, y):
    """
    Softmax loss function, vectorized version.
    y_prediction = argmax(softmax(x))

    :param x: (float) a tensor of shape (N, #classes)
    :param y: (int) ground truth label, a array of length N

    :return: loss - the loss function
             dx - the gradient wrt x
    """
    loss = 0.0
    num_train = x.shape[0]

    x = x - np.max(x, axis=1, keepdims=True)
    x_exp = np.exp(x)
    loss -= np.sum(x[range(num_train), y])
    loss += np.sum(np.log(np.sum(x_exp, axis=1)))

    loss /= num_train

    neg = np.zeros_like(x)
    neg[range(num_train), y] = -1

    pos = (x_exp.T / np.sum(x_exp, axis=1)).T

    dx = (neg + pos) / num_train

    return loss, dx


def conv2d_forward(x, w, b, pad, stride):
    """
    A Numpy implementation of 2-D image convolution.
    By 'convolution', simple element-wise multiplication and summation will suffice.
    The border mode is 'valid' - Your convolution only happens when your input and your filter fully overlap.
    Another thing to remember is that in TensorFlow, 'padding' means border mode (VALID or SAME). For this practice,
    'pad' means the number rows/columns of zeroes to to concatenate before/after the edge of input.

    Inputs:
    :param x: Input data. Should have size (batch, height, width, channels).
    :param w: Filter. Should have size (num_of_filters, filter_height, filter_width, channels).
    :param b: Bias term. Should have size (num_of_filters, ).
    :param pad: Integer. The number of zeroes to pad along the height and width axis.
    :param stride: Integer. The number of pixels to move between 2 neighboring receptive fields.

    :return: A 4-D array. Should have size (batch, new_height, new_width, num_of_filters).

    Note:
    To calculate the output shape of your convolution, you need the following equations:
    new_height = ((height - filter_height + 2 * pad) // stride) + 1
    new_width = ((width - filter_width + 2 * pad) // stride) + 1
    For reference, visit this website:
    https://adeshpande3.github.io/A-Beginner%27s-Guide-To-Understanding-Convolutional-Neural-Networks-Part-2/
    """
    #######################################################################
    #                                                                     #
    #                                                                     #
    #                         TODO: YOUR CODE HERE                        #
    #                                                                     #
    #                                                                     #
    #######################################################################
    N, H, W, C = x.shape
    F, HH, WW, C = w.shape

    Hprime = (H - HH + 2 * pad) / stride + 1
    Wprime = (W - WW + 2 * pad) / stride + 1

    Hprime = int(Hprime)
    Wprime = int(Wprime)

    out = np.empty((N, Hprime, Wprime, F))

  # for each image
    for i in range(N):
    # get the current image and pad it with 0's
        X = np.pad(x[i], ((pad, pad), (pad, pad), (0, 0)), 'constant')

    # X is of shape (C, H + 2pad, W + 2pad)

    # for each filter
        for f in range(F):
            W = w[f]
            b_curr = b[f]

      # W is of shape (C, HH, WW)
      # b_curr is a constant

            result = np.empty((Hprime, Wprime))

            for r in range(Hprime):
                for c in range(Wprime):
                    r_start = r * stride
                    r_end = r_start + HH

                    c_start = c * stride
                    c_end = c_start + WW

                    x_curr = X[r_start:r_end, c_start:c_end, :]

          # x_curr is of shape (C, HH, WW)

                    result[r, c] = np.sum(np.multiply(x_curr, W)) + b_curr

      # result is of shape (Hprime, Wprime)

            out[i, :, :, f] = result

  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################

    return out



def conv2d_backward(d_top, x, w, b, pad, stride):
    """
    (Optional, but if you solve it correctly, we give you +10 points for this assignment.)
    A lite Numpy implementation of 2-D image convolution back-propagation.

    Inputs:
    :param d_top: The derivatives of pre-activation values from the previous layer
                       with shape (batch, height_new, width_new, num_of_filters).
    :param x: Input data. Should have size (batch, height, width, channels).
    :param w: Filter. Should have size (num_of_filters, filter_height, filter_width, channels).
    :param b: Bias term. Should have size (num_of_filters, ).
    :param pad: Integer. The number of zeroes to pad along the height and width axis.
    :param stride: Integer. The number of pixels to move between 2 neighboring receptive fields.

    :return: (d_w, d_b), i.e. the derivative with respect to w and b. For example, d_w means how a change of each value
     of weight w would affect the final loss function.

    Note:
    Normally we also need to compute d_x in order to pass the gradients down to lower layers, so this is merely a
    simplified version where we don't need to back-propagate.
    For reference, visit this website:
    http://www.jefkine.com/general/2016/09/05/backpropagation-in-convolutional-neural-networks/
    """
    #######################################################################
    #                                                                     #
    #                                                                     #
    #                         TODO: YOUR CODE HERE                        #
    #                                                                     #
    #                                                                     #
    #######################################################################
    N, H, W, C = x.shape
    F, HH, WW, C = w.shape

    Hprime = (H - HH + 2 * pad) / stride + 1
    Wprime = (W - WW + 2 * pad) / stride + 1

    Hprime = int(Hprime)
    Wprime = int(Wprime)
    
    x_padded = np.pad(x, ((0, 0), (pad, pad), (pad, pad), (0, 0)), 'constant')
    dx_padded = np.zeros(x_padded.shape)
    dw = np.zeros(w.shape)
    db = np.zeros(b.shape)
    
    for i in range(N):
        for c in range(C):
          # X is shape (H, W)
            X = x_padded[i, :, :, c]

            for f in range(F):
            # W is shape (HH, WW)
                W = w[f, :, :, c]

            # indices in the output volume
                for r1 in range(Hprime):
              # indices in the input X
                    r1_start = r1 * stride
                    r1_end = r1_start + HH

                    for r2 in range(Wprime):
                # indices in the input X
                        r2_start = r2 * stride
                        r2_end = r2_start + WW

                        x_curr = X[r1_start:r1_end, r2_start:r2_end].copy()

                        dx_padded[i, r1_start:r1_end, r2_start:r2_end, c] += W * d_top[i, r1, r2, f]

                        dw[f, 0:HH, 0:WW, c] += x_curr * d_top[i, r1, r2, f]

                        db[f] += d_top[i, r1, r2, f] # doing this C too many times

    dx = dx_padded[:, pad:-pad, pad:-pad, :]

    db /= C
    
    return dw, db

