import tensorflow as tf
from sklearn.model_selection import train_test_split
import tensorflow as keras
import os

train_dir = 'C:/Users/User/MLproject/ML-Final_Project/Scalp_Image_Resize/Train_Resize/'
valid_dir = 'C:/Users/User/MLproject/ML-Final_Project/Scalp_Image_Resize/Valid_Resize/'

folders = ['10','11','12','13']

train_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
valid_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)


def load_images(image_dir):
    image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
    image_data = []
    for step in range(10, 14):
        step_dir = os.path.join(image_dir+ "{}".format(step))
        step_data = image_generator.flow_from_directory(
            directory=step_dir,
            target_size=(320,240),
            batch_size=32,
            class_mode='categorical',
            shuffle=True
        )
    image_data.append(step_data)
    return image_data

train_data = load_images(train_dir)
valid_data = load_images(valid_dir)


train_input = []
train_target = []
test_input = []
test_target = []

for step_data in train_data:
    input_data, target_data = next(iter(step_data))
    train_input.extend(input_data)
    train_target.extend(target_data)

for step_data in valid_data:
    input_data, target_data = next(iter(step_data))
    test_input.extend(input_data)
    test_target.extend(target_data)

train_input = tf.stack(train_input)
train_target = tf.stack(train_target)
test_input = tf.stack(test_input)
test_target = tf.stack(test_target)



train_input, valid_input, train_target, valid_target = train_test_split(
    input_data, target_data, test_size=0.2, random_state=42)

model = keras.Sequential()

model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu',padding='same', input_shape=(320,240,3)))
model.add(keras.layers.MaxPooling2D(2))
model.add(keras.layers.Conv2D(64, kernel_size=3, activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
metrics='accuracy')

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.h5')

early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
            restore_best_weights=True)

history = model.fit(train_input, train_target, epochs=5,
                    validation_data=(valid_input, valid_target),
                    callbacks=[checkpoint_cb, early_stopping_cb])

model.evaluate(valid_input,valid_target)
