# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

#
import stock_history_aggregate as trainer

print(tf.__version__)


(train_inputs, train_outputs) = trainer.create()


# our model
model = keras.Sequential([
    keras.layers.Dense(256, activation=tf.nn.leaky_relu, input_shape=(305,)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(3, activation=tf.nn.relu)
])

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

model.fit(train_inputs, train_outputs, epochs=100, callbacks=[checkpoint_callback])

