# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

#
import generator
import os

print(tf.__version__)


(x, y) = generator.create()

train_inputs = np.asarray(x)
train_outputs = np.asarray(y)

# our model
model = keras.Sequential([
    keras.layers.Dense(256, input_shape=(303,)),
    keras.layers.Dense(256),
    keras.layers.Dense(128),
    keras.layers.Dense(128),
    keras.layers.Dense(3)
])

# Directory where the checkpoints will be saved
checkpoint_dir = 'E:\\Hackathon\\training_checkpoints'
# Name of the checkpoint files
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)

model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))

model.compile(optimizer=tf.train.AdamOptimizer(.00002), 
              loss=tf.keras.losses.MeanSquaredError(),
              metrics=['accuracy'])

##model.fit(train_inputs, train_outputs, epochs=800, callbacks=[checkpoint_callback])
tf.keras.models.save_model(model, 'model.h5', include_optimizer=False)

seshh = tf.keras.backend.get_session()

grappy = seshh.graph
inno = grappy.get_tensor_by_name("dense_input:0")
outo = grappy.get_tensor_by_name("dense_4/BiasAdd:0")

tf.saved_model.simple_save(seshh, "E:\\SavedModel", inputs={"x": inno}, outputs={"y": outo})
#with tf.keras.backend.get_session() as sess:
	# `sess.graph` provides access to the graph used in a <a href="./../api_docs/python/tf/Session"><code>tf.Session</code></a>.
#	writer = tf.summary.FileWriter("/tmp/log/thang.txt", sess.graph)
#	model.fit(train_inputs, train_outputs, epochs=10, callbacks=[checkpoint_callback])
#	writer.close()




#tf.print(tf.keras.backend.get_session())