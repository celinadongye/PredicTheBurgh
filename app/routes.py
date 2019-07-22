from flask import render_template, flash, redirect
from app import app
from app.backend.fetch_currency_info import get_current_rate
from app.backend.fetch_currency_rates import get_currency_rates
from datetime import date, timedelta
from app.forms import NotificationForm
from app.backend.notifications import check_if_send_notification
from flask import request

date_start = date(2018,11,1)
date_end = date(2019,3,14)

currency_list_USD_EUR, dates_list, predicted_data_USD_EUR = get_currency_rates('USD', 'EUR', date_start, date_end)
currency_list_EUR_USD, dates_list, predicted_data_EUR_USD = get_currency_rates('EUR', 'USD', date_start, date_end)
currency_list_USD_GBP, dates_list, predicted_data_USD_GBP = get_currency_rates('USD', 'GBP', date_start, date_end)
currency_list_GBP_USD, dates_list, predicted_data_GBP_USD = get_currency_rates('GBP', 'USD', date_start, date_end)
currency_list_EUR_GBP, dates_list, predicted_data_EUR_GBP = get_currency_rates('EUR', 'GBP', date_start, date_end)
currency_list_GBP_EUR, dates_list, predicted_data_GBP_EUR = get_currency_rates('GBP', 'EUR', date_start, date_end)

rate_USD_EUR = get_current_rate('USD', 'EUR')
rate_EUR_USD = get_current_rate('EUR', 'USD')
rate_USD_GBP = get_current_rate('USD', 'GBP')
rate_GBP_USD = get_current_rate('GBP', 'USD')
rate_GBP_EUR = get_current_rate('GBP', 'EUR')
rate_EUR_GBP = get_current_rate('EUR', 'GBP')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = NotificationForm()
    if request.method == 'POST' and form.validate_on_submit():
        print('Validated')
        name = form.name.data
        phone = form.phone.data
        rate = form.rate.data
        choice = form.choice.data
        above_below = form.above_below.data
        pair = ""
        if choice == 'USD-EUR':
            pair = rate_USD_EUR
        elif choice == 'EUR-USD':
            pair = rate_EUR_USD
        elif choice == 'EUR-GBP':
            pair = rate_EUR_GBP
        elif choice == 'GBP-EUR':
            pair = rate_GBP_EUR
        elif choice == 'GBP-USD':
            pair = rate_GBP_USD
        elif choice == 'USD-GBP':
            pair = rate_USD_GBP
        check_if_send_notification(name, phone, rate, pair, choice, above_below)
        return redirect('/index')
    elif request.method == 'POST':
        return redirect('/index')
    return render_template('index.html',
        title='PredicTheBurgh',
        USD_EUR_data = currency_list_USD_EUR,
        USD_EUR_predicted = predicted_data_USD_EUR,
        EUR_USD_data = currency_list_EUR_USD,
        EUR_USD_predicted = predicted_data_EUR_USD,
        USD_GBP_data = currency_list_USD_GBP,
        USD_GBP_predicted = predicted_data_USD_GBP,
        GBP_USD_data = currency_list_GBP_USD,
        GBP_USD_predicted = predicted_data_GBP_USD,
        EUR_GBP_data = currency_list_EUR_GBP,
        EUR_GBP_predicted = predicted_data_EUR_GBP,
        GBP_EUR_data = currency_list_GBP_EUR,
        GBP_EUR_predicted = predicted_data_GBP_EUR,
        rate_USD_EUR = rate_USD_EUR,
        rate_EUR_USD = rate_EUR_USD,
        rate_USD_GBP = rate_USD_GBP,
        rate_GBP_USD = rate_GBP_USD,
        rate_GBP_EUR = rate_GBP_EUR,
        rate_EUR_GBP = rate_EUR_GBP,
        years=dates_list,
        form=form
    )
