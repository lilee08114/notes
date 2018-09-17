from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, PasswordField,
                     TextAreaField, FileField, ValidationError)
from wtforms.validators import DataRequired, Length, regexp
from . import app

class PostPic(FlaskForm):
    image = FileField('上传图片', validators=[DataRequired(),
                                          regexp(u'^[^/\\]\.%s'%app.config['ALLOWED_IMAGE_EXTENSION'],
                                                 message="允许的文件格式有%s"%app.config['ALLOWED_IMAGE_EXTENSION'])])
    title = StringField('标题', validators=[DataRequired(),Length(6, 30)])
    description = TextAreaField('图片描述', validators=[DataRequired()])
    submit = SubmitField('提交')

    def validate_image(form, field):
        max_size = app.config['MAX_IMAGE_SIZE']
        print ('图片内容长度为%s'%len(field.data))
        if len(field.data) > max_size:
            raise ValidationError('图片最大尺寸不超过 %sM'%(max_size/1024/1024))