import tensorflow as tf
from tensorflow.python.client import device_lib
print(tf.__version__)
print(device_lib.list_local_devices())
tf.test.gpu_device_name()
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
