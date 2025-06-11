from numpy import ndarray
from PIL.Image import Image
from tensorflow import expand_dims
from keras.src.utils import img_to_array, load_img
from tensorflow.keras.models import Model

IMAGE_SIZE = (300, 300)

classes = {0: "paper", 1: "rock", 2: "scissors"}


def preprocess_image(image: Image) -> ndarray:
    image_array = img_to_array(image)
    image_array = expand_dims(image_array, 0)

    return image_array


def load_image_and_preprocess(image_path: str) -> ndarray:
    image = load_img(image_path, target_size=IMAGE_SIZE)

    return preprocess_image(image)


def predict_image(model: Model, image_path: str) -> dict[str, float]:
    image = load_image_and_preprocess(image_path)

    prediction = model.predict(image)

    confidence_score = prediction.max()
    class_index = prediction.argmax(axis=1)[0]
    return {classes[class_index]: float(confidence_score)}
