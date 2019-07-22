from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, SelectField
from wtforms.validators import DataRequired

class NotificationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Your name"})
    phone = StringField('Phone Number', validators=[DataRequired()], render_kw={"placeholder": "Your phone number"})
    rate = DecimalField('Rate', validators=[DataRequired()], render_kw={"placeholder": "Set rate"})
    choice = SelectField('Select currency pair', validators=[DataRequired()], choices=[('USD-EUR', 'USD-EUR'), ('EUR-USD', 'EUR-USD'), ('EUR-GBP', 'EUR-GBP'), ('GBP-EUR', 'GBP-EUR'), ('GBP-USD', 'GBP-USD'), ('USD-GBP', 'USD-GBP')])
    above_below = SelectField('Real time rate is', validators=[DataRequired()], choices=[('above', 'Above'), ('below', 'Below')])
    submit = SubmitField('Submit')
