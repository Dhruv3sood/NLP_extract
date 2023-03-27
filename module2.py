import pandas as pd
import tensorflow as tf
import keras
from pandas import read_csv
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

data = pd.read_csv("/content/Data_Regression.csv")
data.head()
data.shape
