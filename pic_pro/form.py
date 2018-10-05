from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, PasswordField,
                     TextAreaField, FileField, ValidationError)
from wtforms.validators import DataRequired, Length, regexp
from . import app
from flask import request

class PostPic(FlaskForm):
    image = FileField('上传图片', validators=[DataRequired()])
    title = StringField('标题', validators=[DataRequired(), Length(6, 30, "wasdasdasdas！")])
    description = TextAreaField('图片描述', validators=[DataRequired()])
    submit = SubmitField('提交')

    def validate_image(form, field):
        max_size = app.config['MAX_IMAGE_SIZE']
        # if len(field.data.content_length) > max_size:
        #     raise ValidationError('图片最大尺寸不超过 %sM'%(max_size/1024/1024))
        if not field.data.filename.lower().endswith(tuple(app.config['ALLOWED_IMAGE_EXTENSION'])):
            raise ValidationError("允许的文件格式有%s"%app.config['ALLOWED_IMAGE_EXTENSION'])
