import mysql.connector
import numpy as np
from scipy.stats import norm

mydb = mysql.connector.connect(
    host="localhost",
    user="myuser",
    password="mypassword",
    database="mydatabase"
)


def weighted_mean(data):

    # Calculate the mean and standard deviation of the data
    mean = np.mean(data)
    std_dev = np.std(data)

    # Check if the standard deviation is zero
    if std_dev == 0:
        return mean  # Return the mean directly if all values are the same

    # Calculate the weights from the normal distribution
    weights = norm.pdf(data, mean, std_dev)

    # Normalize the weights
    weights /= np.sum(weights)

    # Calculate the weighted average
    weighted_avg = np.sum(data * weights)
    return weighted_avg
