import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf import FlaskForm, CSRFProtect
from flask_wtf.file import FileField, FileRequired
from tensorflow.keras.models import load_model

from classifier import predict_image

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

csrf = CSRFProtect(app)

STATIC_FOLDER = "static/"
UPLOAD_FOLDER = STATIC_FOLDER + "uploads/"

model = load_model("static/models/rock-paper-scissors.keras")


class ImageForm(FlaskForm):
    image = FileField(validators=[FileRequired()])


@app.route("/", methods=["GET", "POST"])
@csrf.exempt
def root() -> str:
    form = ImageForm()

    if form.validate_on_submit():
        img = form.image.data
        img_path = os.path.join(UPLOAD_FOLDER, img.filename)
        img.save(img_path)
        prediction = predict_image(model, img_path)
        return render_template(
            "index.html",
            form=form,
            image_path=img_path,
            prediction=prediction
        )

    return render_template("index.html", form=form)
