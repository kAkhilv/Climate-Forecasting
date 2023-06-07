import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf 


#Read the dataset

df = pd.read_csv('jena_climate_2009_2016.csv')
df.head()