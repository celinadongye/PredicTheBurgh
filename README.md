# PredicTheBurgh

Devpost submission: https://devpost.com/software/predictheburgh

## Inspiration
For many international students, including us, there is a need to exchange the home currency. Do you have to pay the rent in the upcoming month? Are you buying something expensive in the next two weeks? Wouldn’t it be nice if some website would tell you when is the best time to exchange the currency and remind you via the message...

## What It Does
PredicTheBurgh.com makes predictions of exchange rates between the three main currencies (EUR, GBP, USD) and provides the optimal time to convert their money to minimize the loss during conversion and reminds you to exchange the currency via a phone message.

## How We Built It
We trained a Long-Short Term Memory Recurrent Neural Network (Keras) on a datahub.io dataset of the currency rate history for the last 40 years. The neural net takes 60 previous days as an input to predict the price of the next 14 days.
We used foreign exchange rate API by European Central Bank to retrieve the currency rate of the previous 60 days.
The nexmo API was used to send SMS reminder.
Python, CSS, JavaScript, HTML, Flask were used to create a website which integrates all bits of the application.

## Challenges We Ran Into
Training LSTM takes much longer than expected, so it was hard to tune the parameters.

## What’s Next For ‘PredicTheBurgh’
We would like to improve LSTM model and provide user with an option to choose the timeframe of interest.
