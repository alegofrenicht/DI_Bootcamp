import flask
from DI_Bootcamp.Week12.Day2.DailyChallenge.dailychallenge.app import app
from DI_Bootcamp.Week12.Day2.DailyChallenge.dailychallenge.app.forms import Form


@app.route('/', methods=("GET", "POST"))
def main():
    form = Form()
    if form.validate_on_submit():
        print('Inside')
        retr_data = {
            'firstname': form.user_firstname.data,
            'lastname': form.user_lastname.data,
            'age': form.age.data,
            'country': form.country.data,
            'exp': form.exp.data
        }
        return flask.render_template('CV.html', data=retr_data)
    return flask.render_template('main.html', form=form)
