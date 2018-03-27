import numpy as np
import tensorflow as tf

num_classes = 20

def encode(X):

    with tf.name_scope("rectangle1"):
        with tf.name_scope("input_layer"):
            input_layer = tf.reshape(X, [-1, 224, 224, 3])
        with tf.name_scope("conv1"):
            rect1_conv1 = tf.layers.conv2d(
                input_layer,
                kernel_size=[3, 3],
                filters=64,
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )
        # with tf.name_scope("batch_normalization1"):
        #     mean, variance = tf.nn.moments(rect1_conv1, [0, 1, 2])
        #     normalized_conv1 = tf.nn.batch_normalization(rect1_conv1, mean, variance)
        with tf.name_scope("conv2"):
            rect1_conv2 = tf.layers.conv2d(
                rect1_conv1,
                kernel_size=[3, 3],
                strides=1,
                filters=64,
                padding="same",
                activation=tf.nn.relu
            )

    with tf.name_scope("rectangle2"):
        with tf.name_scope("down_sampling"):
            rect2_max_pool = tf.layers.max_pooling2d(
                rect1_conv2,
                pool_size=[2, 2],
                strides=2,
                padding="valid"
            )
        with tf.name_scope("conv1"):
            rect2_conv1 = tf.layers.conv2d(
                rect2_max_pool,
                kernel_size=[3, 3],
                filters=128,
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )
        with tf.name_scope("conv2"):
            rect2_conv2 = tf.layers.conv2d(
                rect2_conv1,
                kernel_size=[3, 3],
                filters=128,
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )

    with tf.name_scope("rectangle3"):
        with tf.name_scope("down_sampling"):
            rect3_max_pool = tf.layers.max_pooling2d(
                rect2_conv2,
                pool_size=[2, 2],
                strides=2,
                padding="valid"
            )
        with tf.name_scope("conv1"):
            rect3_conv1 = tf.layers.conv2d(
                rect3_max_pool,
                kernel_size=[3, 3],
                filters=256,
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )
        with tf.name_scope("conv2"):
            rect3_conv2 = tf.layers.conv2d(
                rect3_conv1,
                kernel_size=[3, 3],
                filters=256,
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )

    with tf.name_scope("rectangle4"):
        with tf.name_scope("down_sampling"):
            rect4_max_pool = tf.layers.max_pooling2d(
                rect3_conv2,
                pool_size=[2, 2],
                strides=2,
                padding="valid"
            )
        with tf.name_scope("conv1"):
            rect4_conv1 = tf.layers.conv2d(
                rect4_max_pool,
                kernel_size=[3, 3],
                filters=512,
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )
        with tf.name_scope("conv2"):
            rect4_conv2 = tf.layers.conv2d(
                rect4_conv1,
                kernel_size=[3, 3],
                filters=512,
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )

    with tf.name_scope("rectangle5"):
        with tf.name_scope("down_sampling"):
            rect5_max_pool = tf.layers.max_pooling2d(
                rect4_conv2,
                pool_size=[2, 2],
                strides=2,
                padding="valid"
            )
        with tf.name_scope("conv1"):
            rect5_conv1 = tf.layers.conv2d(
                rect5_max_pool,
                kernel_size=[3, 3],
                filters=1024,
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )
        with tf.name_scope("conv2"):
            rect5_conv2 = tf.layers.conv2d(
                rect5_conv1,
                kernel_size=[3, 3],
                filters=1024,
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )

    with tf.name_scope("rectangle6"):
        with tf.name_scope("upsampling"):
            rect6_transpose_conv = tf.layers.conv2d_transpose(
                rect5_conv2,
                filters=1024,
                kernel_size=[2, 2],
                strides=2,
                padding="valid"
            )
        with tf.name_scope("conv1"):
            rect6_conv1 = tf.layers.conv2d(
                rect6_transpose_conv,
                filters=512,
                kernel_size=[3, 3],
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )
        with tf.name_scope("conv2"):
            rect6_conv2 = tf.layers.conv2d(
                rect6_conv1,
                filters=512,
                kernel_size=[3, 3],
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )

    with tf.name_scope("rectangle7"):
        with tf.name_scope("upsampling"):
            rect7_transpose_conv = tf.layers.conv2d_transpose(
                rect6_conv2,
                filters=512,
                kernel_size=[2, 2],
                strides=2,
                padding="valid"
            )
        with tf.name_scope("conv1"):
            rect7_conv1 = tf.layers.conv2d(
                rect7_transpose_conv,
                filters=256,
                kernel_size=[3, 3],
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )
        with tf.name_scope("conv2"):
            rect7_conv2 = tf.layers.conv2d(
                rect7_conv1,
                filters=256,
                kernel_size=[3, 3],
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )

    with tf.name_scope("rectangle8"):
        with tf.name_scope("upsampling"):
            rect8_transpose_conv = tf.layers.conv2d_transpose(
                rect7_conv2,
                filters=256,
                kernel_size=[2, 2],
                strides=2,
                padding="valid"
            )
        with tf.name_scope("conv1"):
            rect8_conv1 = tf.layers.conv2d(
                rect8_transpose_conv,
                filters=128,
                kernel_size=[3, 3],
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )
        with tf.name_scope("conv2"):
            rect8_conv2 = tf.layers.conv2d(
                rect8_conv1,
                filters=128,
                kernel_size=[3, 3],
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )

    with tf.name_scope("rectangle9"):
        with tf.name_scope("upsampling"):
            rect9_transpose_conv = tf.layers.conv2d_transpose(
                rect8_conv2,
                filters=128,
                kernel_size=[2, 2],
                strides=2,
                padding="valid"
            )
        with tf.name_scope("conv1"):
            rect9_conv1 = tf.layers.conv2d(
                rect9_transpose_conv,
                filters=64,
                kernel_size=[3, 3],
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )
        with tf.name_scope("conv2"):
            rect9_conv2 = tf.layers.conv2d(
                rect9_conv1,
                filters=64,
                kernel_size=[3, 3],
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )
        with tf.name_scope("logits"):
            logits = tf.layers.conv2d(
                rect9_conv2,
                filters=num_classes,
                kernel_size=[1, 1],
                strides=1,
                padding="same",
                activation=tf.nn.relu
            )

    return logits
