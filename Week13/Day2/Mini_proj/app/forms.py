import flask_wtf
import wtforms


class LoginForm(flask_wtf.FlaskForm):
    name = wtforms.StringField("Your name", [wtforms.validators.DataRequired()])
    address_city = wtforms.StringField("Your address", [wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Submit")
