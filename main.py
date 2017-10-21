from bokeh.plotting import figure, output_file, show
import datashader as ds
import base64
import datashader.utils as utils
import datashader.transfer_functions as tf
import pandas as pd

df = pd.read_csv('Trees.csv')
print(df)
cvs = ds.Canvas(plot_width=2000, plot_height=1000)
agg = cvs.points(df, 'X','Y')
img = tf.shade(agg,cmap=["green","green"], how='log')
print(img)
print(type(img))

utils.export_image(img,'output')
