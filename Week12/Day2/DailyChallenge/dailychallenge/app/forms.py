import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    user_firstname = wtforms.StringField("First Name", [wtforms.validators.DataRequired()])
    user_lastname = wtforms.StringField("Last Name", [wtforms.validators.DataRequired()])
    age = wtforms.IntegerField("Age", [wtforms.validators.DataRequired()])
    exp = wtforms.StringField("Experience", [wtforms.validators.DataRequired()])
    country = wtforms.StringField("Country", [wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Submit")
