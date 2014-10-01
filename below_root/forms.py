from flask_wtf import Form 
from wtforms import TextField
from wtforms.validators import DataRequired, Length

class InputForm(Form):
    x_or_o = TextField('Username', validators=[DataRequired(), Length(min=1, max=1, message="input must be 'x' or 'o'")])