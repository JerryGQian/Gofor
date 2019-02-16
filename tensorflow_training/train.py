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
    keras.layers.Dense(256, input_shape=(306,)),
    keras.layers.Dense(128),
    keras.layers.Dense(128),
    keras.layers.Dense(3)
])

#model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))

model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss=tf.keras.losses.MeanSquaredError(),
              metrics=['accuracy'])

# Directory where the checkpoints will be saved
checkpoint_dir = 'E:\\Hackathon\\training_checkpoints'
# Name of the checkpoint files
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)

model.fit(train_inputs, train_outputs, epochs=1000, callbacks=[checkpoint_callback])

predictions = model.predict(train_inputs)

print(train_outputs)
print(predictions)

test_loss, test_acc = model.evaluate(train_inputs, train_outputs)

print('\nTest accuracy:', test_acc)