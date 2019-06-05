import os
from sklearn import preprocessing
import pandas as pd
import logging
import seaborn as sns
import matplotlib.pyplot as plt


# from src.datamanipulation.data_preprocessing import make_col_positive

# TODO: Initialise a simple logger and set the desired format to be: TIME LEVEL-module-function-line number-message

# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')


def transform_data(data):
    """
    Function to transform data according to some pre-defined steps.

    :param data: data to transform, dataframe format
    :return: transformed data
    """
    # import logging
    # logger = logging.getLogger('root')
    # FORMAT = "[%(asctime)s:%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    # logging.basicConfig(format=FORMAT)
    # logger.setLevel(logging.DEBUG)
    # logger.debug('Your Custom Message')
    columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name']
    df = pd.read_fwf("../../data/auto-mpg-data.txt", names = columns)
    # print(df)
    sns.boxplot(x=df['mpg'])
    # sns.distplot(df['mpg'], kde=True, rug=False)
    plt.show()



    return data


if __name__ == "__main__":
    '''
    HOMEWORK: Write a function that outputs insights into the data. I.e. aggregated data, plots etc. that will
    tell a compelling story to Heathrow about trends that we have discovered in the airline industry.

    The output should be the repository that helped produce the insight and a deck (.pdf, no longer that 5 slides)
    which would be used to present the insights to the client. 

    Please do not spend more than 3 hours on this.
    '''
    flights_data = None  # TODO: Import flight data
    transformed = transform_data(flights_data)


