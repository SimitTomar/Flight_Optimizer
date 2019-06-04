import os
from sklearn import preprocessing
from sklearn.preprocessing import minmax_scale
import pandas as pd
import numpy as np
import logging
from datamanipulation.data_preprocessing import make_col_positive, log_transform
import matplotlib.pyplot as plt


# Increase the Number of Columns Pycharm can show
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',32)


# TODO: Initialise a simple logger and set the desired format to be: TIME LEVEL-module-function-line number-message

import logging
logger = logging.getLogger('root')
FORMAT = "[%(asctime)s:%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)



def transform_data(data):
    """
    Function to transform data according to some pre-defined steps.

    :param data: data to transform, dataframe format
    :return: transformed data
    """

    # TODO: drop column 'DAY_OF_WEEK'
    del data['DAY_OF_WEEK']

    # TODO: Rename column 'WHEELS_OFF' to 'HAS_WHEELS'
    data.rename(columns={'WHEELS_OFF': 'HAS_WHEELS'})

    # TODO: Fill blanks in column 'AIR_SYSTEM_DELAY' with the average of the values
    data.fillna(data['AIR_SYSTEM_DELAY'].mean(), inplace=True)

    # TODO: Scale values between 0 and 1 in 'DEPARTURE_DELAY' and put them in 'DEPARTURE_DELAY_NORMALISED'
    departure_delay_normalized_data = minmax_scale(np.array(data['DEPARTURE_DELAY']))
    data.insert(11, 'DEPARTURE_DELAY_NORMALISED', departure_delay_normalized_data, True)

    # TODO: Make 'ARRIVAL_DELAY' column positive using a function imported from data_preprocessing.py
    data['ARRIVAL_DELAY'] = make_col_positive(data['ARRIVAL_DELAY'])

    # TODO: take the log of the column DEPARTURE_DELAY
    data['DEPARTURE_DELAY'] = log_transform(data['DEPARTURE_DELAY'])

    return data


if __name__ == "__main__":
    '''
    HOMEWORK: Write a function that outputs insights into the data. I.e. aggregated data, plots etc. that will
    tell a compelling story to Heathrow aboDEPARTURE_TIMEut trends that we have discovered in the airline industry.

    The output should be the repository that helped produce the insight and a deck (.pdf, no longer that 5 slides)
    which would be used to present the insights to the client.

    Please do not spend more than 3 hours on this.
    '''
    flights_data = pd.read_csv("/Users/simtomar/Desktop/DataScience_Course/data-science-learning/espresso_python_hacking/data/flights_old.csv") # TODO: Import flight data
    logger.info(flights_data)
    transformed = transform_data(flights_data)
    transformed.plot(x='ARRIVAL_TIME', y='ARRIVAL_DELAY', style='o')
    transformed.plot(x='DEPARTURE_TIME', y='ARRIVAL_DELAY', style='o')
    transformed.plot(x='DEPARTURE_DELAY_NORMALISED', y='ARRIVAL_DELAY', style='o')
    plt.show()