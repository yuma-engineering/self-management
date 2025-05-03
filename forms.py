from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,ValidationError,FloatField
from wtforms.validators import DataRequired, Length, EqualTo,ValidationError,NumberRange
from backend.models import User
import string

class DoForm(FlaskForm):
    todo=StringField(validators=[DataRequired()])
    time=FloatField(validators=[DataRequired(),NumberRange(min=0.1,max=24)])
    submit=SubmitField('追加')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')


        

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password')
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_password(self,password):
        '''
        - 未入力 禁止
        - 文字数４文字以上８文字以下
        - 「-」を入れる
        '''
        if password.data == '':
            raise ValidationError('値を入力してください。')
        if not(4 <= len(password.data) <= 8):
            raise ValidationError('値を4文字以上8文字以下で入力してください。')
        
        if not any(char in string.punctuation for char in password.data):
            raise ValidationError('少なくとも1つ特殊文字を含めてください。')

        if not any(char.isdigit() for char in password.data):
            raise ValidationError('少なくとも1つ数字を含めてください。')
        

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
