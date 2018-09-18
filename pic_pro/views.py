
'''
a web project mainly to record and show pictures
'''
import os
import os.path
from uuid import uuid1
from datetime import datetime
from flask import request, render_template, current_app, redirect, url_for
from .extension import db
from .form import PostPic
from .model import Image
from . import app

@app.route('/')
def home():
    form = PostPic()
    latest_ten_images = Image.query.filter_by().order_by(Image.id).limit(10)
    return render_template('home.html', form=form,
                           images=latest_ten_images )

@app.route('/upload/', methods=['POST'])
def upload_file():
    image_file = request.files['image']
    if image_file:
        path = _get_image_storage_path()
        image_file.save(path)
        image = Image(image_path=path,
                      title=request.form['title'],
                      description=request.form['description'])
        db.session.add(image)
        db.session.commit()
    return redirect(url_for('home'))

def _get_image_storage_path():
    """get the image storage path, it will be generate by combining storage
       path plus date folder plus a unique id,
       images will be store in different directory base on upload date
    """
    image_folder = current_app.config['IMAGE_UPLOADED_FILE']
    today = datetime.now().strftime("%Y-%m-%d")
    image_folder_for_today = os.path.join(image_folder, today)
    if not os.path.exists(image_folder_for_today):
        os.makedirs(image_folder_for_today)
    unique_id = str(uuid1())
    unique_name = os.path.join(image_folder_for_today, unique_id)
    return unique_name + '.jpg'
