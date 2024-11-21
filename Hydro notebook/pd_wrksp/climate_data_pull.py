import ulmo
import pandas as pd
import numpy as np
import datetime as dt
from dateutil.relativedelta import relativedelta
import pdb
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import figure
from climata.snotel import StationDailyDataIO
import os

def ImportSnotel(stationid,start_date='2021-05-1',end_date='2022-7-18'): 
    '''wrapper for climata.  returns a date indexed dataframe of snow water equivalent'''
    print ('downloading snotel station swe data.')
    params = StationDailyDataIO(station=stationid,start_date='2021-05-1',end_date='2022-7-18')   
    print ('snotel swe download done.')
    df = params.as_dataframe()
    swe = df.data[df.index[df.element_name=='SNOW WATER EQUIVALENT'].values[0]].as_dataframe()
    swe['date']=pd.to_datetime(swe.date)
    swe.set_index('date',inplace=True)
    swe=swe.dropna()
    return swe
swe = ImportSnotel('760:MT:SNTL',start_date='2021-05-1',end_date='2022-7-18')

def ImportSnotel(stationid,start_date='2021-05-1',end_date='2022-7-18'): 
    '''wrapper for climata.  returns a date indexed dataframe of snow water equivalent'''
    print ('downloading snotel station depth data.')
    params = StationDailyDataIO(station=stationid,start_date='2021-05-1',end_date='2022-7-18')   
    print ('snotel depth download done.')
    df = params.as_dataframe()
    depth = df.data[df.index[df.element_name=='SNOW DEPTH'].values[0]].as_dataframe()
    depth['date']=pd.to_datetime(depth.date)
    depth.set_index('date',inplace=True)
    depth=depth.dropna()
    return depth
depth = ImportSnotel('760:MT:SNTL',start_date='2021-05-1',end_date='2022-7-18')

swe.to_csv('skalkaho_swe.csv')
depth.to_csv('skalkaho_depth.csv')
