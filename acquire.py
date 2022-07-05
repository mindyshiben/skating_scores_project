import pandas as pd
import numpy as np
import requests
import os

def get_gp_usa():

    b0304 = pd.read_html('https://skatingscores.com/0304/gpusa/sr/women/short/quicklook/')
    b0405 = pd.read_html('https://skatingscores.com/0405/gpusa/sr/women/short/quicklook/')
    b0506 = pd.read_html('https://skatingscores.com/0506/gpusa/sr/women/short/quicklook/')
    b0607 = pd.read_html('https://skatingscores.com/0607/gpusa/sr/women/short/quicklook/')
    b0708 = pd.read_html('https://skatingscores.com/0708/gpusa/sr/women/short/quicklook/')
    b0809 = pd.read_html('https://skatingscores.com/0809/gpusa/sr/women/short/quicklook/')
    b0910 = pd.read_html('https://skatingscores.com/0910/gpusa/sr/women/short/quicklook/')
    b1011 = pd.read_html('https://skatingscores.com/1011/gpusa/sr/women/short/quicklook/')
    b1112 = pd.read_html('https://skatingscores.com/1112/gpusa/sr/women/short/quicklook/')
    b1213 = pd.read_html('https://skatingscores.com/1213/gpusa/sr/women/short/quicklook/')
    b1314 = pd.read_html('https://skatingscores.com/1314/gpusa/sr/women/short/quicklook/')
    b1415 = pd.read_html('https://skatingscores.com/1415/gpusa/sr/women/short/quicklook/')
    b1516 = pd.read_html('https://skatingscores.com/1516/gpusa/sr/women/short/quicklook/')
    b1617 = pd.read_html('https://skatingscores.com/1617/gpusa/sr/women/short/quicklook/')
    b1718 = pd.read_html('https://skatingscores.com/1718/gpusa/sr/women/short/quicklook/')
    b1819 = pd.read_html('https://skatingscores.com/1819/gpusa/sr/women/short/quicklook/')
    b1920 = pd.read_html('https://skatingscores.com/1920/gpusa/sr/women/short/quicklook/')
    b2021 = pd.read_html('https://skatingscores.com/2021/gpusa/sr/women/short/quicklook/')
    b2122 = pd.read_html('https://skatingscores.com/2122/gpusa/sr/women/short/quicklook/')
    c0304 = pd.read_html('https://skatingscores.com/0304/gpusa/sr/women/long/quicklook/')
    c0405 = pd.read_html('https://skatingscores.com/0405/gpusa/sr/women/long/quicklook/')
    c0506 = pd.read_html('https://skatingscores.com/0506/gpusa/sr/women/long/quicklook/')
    c0607 = pd.read_html('https://skatingscores.com/0607/gpusa/sr/women/long/quicklook/')
    c0708 = pd.read_html('https://skatingscores.com/0708/gpusa/sr/women/long/quicklook/')
    c0809 = pd.read_html('https://skatingscores.com/0809/gpusa/sr/women/long/quicklook/')
    c0910 = pd.read_html('https://skatingscores.com/0910/gpusa/sr/women/long/quicklook/')
    c1011 = pd.read_html('https://skatingscores.com/1011/gpusa/sr/women/long/quicklook/')
    c1112 = pd.read_html('https://skatingscores.com/1112/gpusa/sr/women/long/quicklook/')
    c1213 = pd.read_html('https://skatingscores.com/1213/gpusa/sr/women/long/quicklook/')
    c1314 = pd.read_html('https://skatingscores.com/1314/gpusa/sr/women/long/quicklook/')
    c1415 = pd.read_html('https://skatingscores.com/1415/gpusa/sr/women/long/quicklook/')
    c1516 = pd.read_html('https://skatingscores.com/1516/gpusa/sr/women/long/quicklook/')
    c1617 = pd.read_html('https://skatingscores.com/1617/gpusa/sr/women/long/quicklook/')
    c1718 = pd.read_html('https://skatingscores.com/1718/gpusa/sr/women/long/quicklook/')
    c1819 = pd.read_html('https://skatingscores.com/1819/gpusa/sr/women/long/quicklook/')
    c1920 = pd.read_html('https://skatingscores.com/1920/gpusa/sr/women/long/quicklook/')
    c2021 = pd.read_html('https://skatingscores.com/2021/gpusa/sr/women/long/quicklook/')
    c2122 = pd.read_html('https://skatingscores.com/2122/gpusa/sr/women/long/quicklook/')
    f0304 = pd.read_html('https://skatingscores.com/0304/gpusa/sr/women/results/')
    f0405 = pd.read_html('https://skatingscores.com/0405/gpusa/sr/women/results/')
    f0506 = pd.read_html('https://skatingscores.com/0506/gpusa/sr/women/results/')
    f0607 = pd.read_html('https://skatingscores.com/0607/gpusa/sr/women/results/')
    f0708 = pd.read_html('https://skatingscores.com/0708/gpusa/sr/women/results/')
    f0809 = pd.read_html('https://skatingscores.com/0809/gpusa/sr/women/results/')
    f0910 = pd.read_html('https://skatingscores.com/0910/gpusa/sr/women/results/')
    f1011 = pd.read_html('https://skatingscores.com/1011/gpusa/sr/women/results/')
    f1112 = pd.read_html('https://skatingscores.com/1112/gpusa/sr/women/results/')
    f1213 = pd.read_html('https://skatingscores.com/1213/gpusa/sr/women/results/')
    f1314 = pd.read_html('https://skatingscores.com/1314/gpusa/sr/women/results/')
    f1415 = pd.read_html('https://skatingscores.com/1415/gpusa/sr/women/results/')
    f1516 = pd.read_html('https://skatingscores.com/1516/gpusa/sr/women/results/')
    f1617 = pd.read_html('https://skatingscores.com/1617/gpusa/sr/women/results/')
    f1718 = pd.read_html('https://skatingscores.com/1718/gpusa/sr/women/results/')
    f1819 = pd.read_html('https://skatingscores.com/1819/gpusa/sr/women/results/')
    f1920 = pd.read_html('https://skatingscores.com/1920/gpusa/sr/women/results/')
    f2021 = pd.read_html('https://skatingscores.com/2021/gpusa/sr/women/results/')
    f2122 = pd.read_html('https://skatingscores.com/2122/gpusa/sr/women/results/')
    b0304 = b0304[1]
    b0405 = b0405[1]
    b0506 = b0506[1]
    b0607 = b0607[1]
    b0708 = b0708[1]
    b0809 = b0809[1]
    b0910 = b0910[1]
    b1011 = b1011[1]
    b1112 = b1112[1]
    b1213 = b1213[1]
    b1314 = b1314[1]
    b1415 = b1415[1]
    b1516 = b1516[1]
    b1617 = b1617[1]
    b1718 = b1718[1]
    b1819 = b1819[1]
    b1920 = b1920[1]
    b2021 = b2021[1]
    b2122 = b2122[1]
    b0304['season'] = 2004
    b0405['season'] = 2005
    b0506['season'] = 2006
    b0607['season'] = 2007
    b0708['season'] = 2008
    b0809['season'] = 2009
    b0910['season'] = 2010
    b1011['season'] = 2011
    b1112['season'] = 2012
    b1213['season'] = 2013
    b1314['season'] = 2014
    b1415['season'] = 2015
    b1516['season'] = 2016
    b1617['season'] = 2017
    b1718['season'] = 2018
    b1819['season'] = 2019
    b1920['season'] = 2020
    b2021['season'] = 2021
    b2122['season'] = 2022
    c0304 = c0304[1]
    c0405 = c0405[1]
    c0506 = c0506[1]
    c0607 = c0607[1]
    c0708 = c0708[1]
    c0809 = c0809[1]
    c0910 = c0910[1]
    c1011 = c1011[1]
    c1112 = c1112[1]
    c1213 = c1213[1]
    c1314 = c1314[1]
    c1415 = c1415[1]
    c1516 = c1516[1]
    c1617 = c1617[1]
    c1718 = c1718[1]
    c1819 = c1819[1]
    c1920 = c1920[1]
    c2021 = c2021[1]
    c2122 = c2122[1]
    c0304['season'] = 2004
    c0405['season'] = 2005
    c0506['season'] = 2006
    c0607['season'] = 2007
    c0708['season'] = 2008
    c0809['season'] = 2009
    c0910['season'] = 2010
    c1011['season'] = 2011
    c1112['season'] = 2012
    c1213['season'] = 2013
    c1314['season'] = 2014
    c1415['season'] = 2015
    c1516['season'] = 2016
    c1617['season'] = 2017
    c1718['season'] = 2018
    c1819['season'] = 2019
    c1920['season'] = 2020
    c2021['season'] = 2021
    c2122['season'] = 2022
    f0304 = f0304[1]
    f0405 = f0405[1]
    f0506 = f0506[1]
    f0607 = f0607[1]
    f0708 = f0708[1]
    f0809 = f0809[1]
    f0910 = f0910[1]
    f1011 = f1011[1]
    f1112 = f1112[1]
    f1213 = f1213[1]
    f1314 = f1314[1]
    f1415 = f1415[1]
    f1516 = f1516[1]
    f1617 = f1617[1]
    f1718 = f1718[1]
    f1819 = f1819[1]
    f1920 = f1920[1]
    f2021 = f2021[1]
    f2122 = f2122[1]
    f0304['season'] = 2004
    f0405['season'] = 2005
    f0506['season'] = 2006
    f0607['season'] = 2007
    f0708['season'] = 2008
    f0809['season'] = 2009
    f0910['season'] = 2010
    f1011['season'] = 2011
    f1112['season'] = 2012
    f1213['season'] = 2013
    f1314['season'] = 2014
    f1415['season'] = 2015
    f1516['season'] = 2016
    f1617['season'] = 2017
    f1718['season'] = 2018
    f1819['season'] = 2019
    f1920['season'] = 2020
    f2021['season'] = 2021
    f2122['season'] = 2022
    f0304['skater_name'] = f0304['Skater']
    f0405['skater_name'] = f0405['Skater']
    f0506['skater_name'] = f0506['Skater']
    f0607['skater_name'] = f0607['Skater']
    f0708['skater_name'] = f0708['Skater']
    f0809['skater_name'] = f0809['Skater']
    f0910['skater_name'] = f0910['Skater']
    f1011['skater_name'] = f1011['Skater']
    f1112['skater_name'] = f1112['Skater']
    f1213['skater_name'] = f1213['Skater']
    f1314['skater_name'] = f1314['Skater']
    f1415['skater_name'] = f1415['Skater']
    f1516['skater_name'] = f1516['Skater']
    f1617['skater_name'] = f1617['Skater']
    f1718['skater_name'] = f1718['Skater']
    f1819['skater_name'] = f1819['Skater']
    f1920['skater_name'] = f1920['Skater']
    f2021['skater_name'] = f2021['Skater']
    f2122['skater_name'] = f2122['Skater']
    f0304[['first_name','Skater']] = f0304['Skater'].loc[f0304['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0405[['first_name','Skater']] = f0405['Skater'].loc[f0405['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0506[['first_name','Skater']] = f0506['Skater'].loc[f0506['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0607[['first_name','Skater']] = f0607['Skater'].loc[f0607['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0708[['first_name','Skater']] = f0708['Skater'].loc[f0708['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0809[['first_name','Skater']] = f0809['Skater'].loc[f0809['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0910[['first_name','Skater']] = f0910['Skater'].loc[f0910['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1011[['first_name','Skater']] = f1011['Skater'].loc[f1011['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1112[['first_name','Skater']] = f1112['Skater'].loc[f1112['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1213[['first_name','Skater']] = f1213['Skater'].loc[f1213['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1314[['first_name','Skater']] = f1314['Skater'].loc[f1314['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1415[['first_name','Skater']] = f1415['Skater'].loc[f1415['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1516[['first_name','Skater']] = f1516['Skater'].loc[f1516['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1617[['first_name','Skater']] = f1617['Skater'].loc[f1617['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1718[['first_name','Skater']] = f1718['Skater'].loc[f1718['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1819[['first_name','Skater']] = f1819['Skater'].loc[f1819['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1920[['first_name','Skater']] = f1920['Skater'].loc[f1920['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f2021[['first_name','Skater']] = f2021['Skater'].loc[f2021['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f2122[['first_name','Skater']] = f2122['Skater'].loc[f2122['Skater'].str.split().str.len() == 2].str.split(expand=True)
    s2004 = f0304.merge(b0304,on='Skater').merge(c0304, on='Skater')
    s2005 = f0405.merge(b0405,on='Skater').merge(c0405, on='Skater')
    s2006 = f0506.merge(b0506,on='Skater').merge(c0506, on='Skater')
    s2007 = f0607.merge(b0607,on='Skater').merge(c0607, on='Skater')
    s2008 = f0708.merge(b0708,on='Skater').merge(c0708, on='Skater')
    s2009 = f0809.merge(b0809,on='Skater').merge(c0809, on='Skater')
    s2010 = f0910.merge(b0910,on='Skater').merge(c0910, on='Skater')
    s2011 = f1011.merge(b1011,on='Skater').merge(c1011, on='Skater')
    s2012 = f1112.merge(b1112,on='Skater').merge(c1112, on='Skater')
    s2013 = f1213.merge(b1213,on='Skater').merge(c1213, on='Skater')
    s2014 = f1314.merge(b1314,on='Skater').merge(c1314, on='Skater')
    s2015 = f1415.merge(b1415,on='Skater').merge(c1415, on='Skater')
    s2016 = f1516.merge(b1516,on='Skater').merge(c1516, on='Skater')
    s2017 = f1617.merge(b1617,on='Skater').merge(c1617, on='Skater')
    s2018 = f1718.merge(b1718,on='Skater').merge(c1718, on='Skater')
    s2019 = f1819.merge(b1819,on='Skater').merge(c1819, on='Skater')
    s2020 = f1920.merge(b1920,on='Skater').merge(c1920, on='Skater')
    s2021 = f2021.merge(b2021,on='Skater').merge(c2021, on='Skater')
    s2022 = f2122.merge(b2122,on='Skater').merge(c2122, on='Skater')
    gp_usa = pd.concat([s2004, s2005, s2006, s2007, s2008, s2009, s2010, s2011, s2012, s2013, s2014, 
                            s2015, s2016, s2017, s2018, s2019, s2020, s2021, s2022], axis=0)
    gp_usa['event'] = 'gp_usa'
    return gp_usa



def get_gp_canada():

    b0304 = pd.read_html('https://skatingscores.com/0304/gpcan/sr/women/short/quicklook/')
    b0405 = pd.read_html('https://skatingscores.com/0405/gpcan/sr/women/short/quicklook/')
    b0506 = pd.read_html('https://skatingscores.com/0506/gpcan/sr/women/short/quicklook/')
    b0607 = pd.read_html('https://skatingscores.com/0607/gpcan/sr/women/short/quicklook/')
    b0708 = pd.read_html('https://skatingscores.com/0708/gpcan/sr/women/short/quicklook/')
    b0809 = pd.read_html('https://skatingscores.com/0809/gpcan/sr/women/short/quicklook/')
    b0910 = pd.read_html('https://skatingscores.com/0910/gpcan/sr/women/short/quicklook/')
    b1011 = pd.read_html('https://skatingscores.com/1011/gpcan/sr/women/short/quicklook/')
    b1112 = pd.read_html('https://skatingscores.com/1112/gpcan/sr/women/short/quicklook/')
    b1213 = pd.read_html('https://skatingscores.com/1213/gpcan/sr/women/short/quicklook/')
    b1314 = pd.read_html('https://skatingscores.com/1314/gpcan/sr/women/short/quicklook/')
    b1415 = pd.read_html('https://skatingscores.com/1415/gpcan/sr/women/short/quicklook/')
    b1516 = pd.read_html('https://skatingscores.com/1516/gpcan/sr/women/short/quicklook/')
    b1617 = pd.read_html('https://skatingscores.com/1617/gpcan/sr/women/short/quicklook/')
    b1718 = pd.read_html('https://skatingscores.com/1718/gpcan/sr/women/short/quicklook/')
    b1819 = pd.read_html('https://skatingscores.com/1819/gpcan/sr/women/short/quicklook/')
    b1920 = pd.read_html('https://skatingscores.com/1920/gpcan/sr/women/short/quicklook/')
    b2122 = pd.read_html('https://skatingscores.com/2122/gpcan/sr/women/short/quicklook/')
    c0304 = pd.read_html('https://skatingscores.com/0304/gpcan/sr/women/long/quicklook/')
    c0405 = pd.read_html('https://skatingscores.com/0405/gpcan/sr/women/long/quicklook/')
    c0506 = pd.read_html('https://skatingscores.com/0506/gpcan/sr/women/long/quicklook/')
    c0607 = pd.read_html('https://skatingscores.com/0607/gpcan/sr/women/long/quicklook/')
    c0708 = pd.read_html('https://skatingscores.com/0708/gpcan/sr/women/long/quicklook/')
    c0809 = pd.read_html('https://skatingscores.com/0809/gpcan/sr/women/long/quicklook/')
    c0910 = pd.read_html('https://skatingscores.com/0910/gpcan/sr/women/long/quicklook/')
    c1011 = pd.read_html('https://skatingscores.com/1011/gpcan/sr/women/long/quicklook/')
    c1112 = pd.read_html('https://skatingscores.com/1112/gpcan/sr/women/long/quicklook/')
    c1213 = pd.read_html('https://skatingscores.com/1213/gpcan/sr/women/long/quicklook/')
    c1314 = pd.read_html('https://skatingscores.com/1314/gpcan/sr/women/long/quicklook/')
    c1415 = pd.read_html('https://skatingscores.com/1415/gpcan/sr/women/long/quicklook/')
    c1516 = pd.read_html('https://skatingscores.com/1516/gpcan/sr/women/long/quicklook/')
    c1617 = pd.read_html('https://skatingscores.com/1617/gpcan/sr/women/long/quicklook/')
    c1718 = pd.read_html('https://skatingscores.com/1718/gpcan/sr/women/long/quicklook/')
    c1819 = pd.read_html('https://skatingscores.com/1819/gpcan/sr/women/long/quicklook/')
    c1920 = pd.read_html('https://skatingscores.com/1920/gpcan/sr/women/long/quicklook/')
    c2122 = pd.read_html('https://skatingscores.com/2122/gpcan/sr/women/long/quicklook/')
    f0304 = pd.read_html('https://skatingscores.com/0304/gpcan/sr/women/results/')
    f0405 = pd.read_html('https://skatingscores.com/0405/gpcan/sr/women/results/')
    f0506 = pd.read_html('https://skatingscores.com/0506/gpcan/sr/women/results/')
    f0607 = pd.read_html('https://skatingscores.com/0607/gpcan/sr/women/results/')
    f0708 = pd.read_html('https://skatingscores.com/0708/gpcan/sr/women/results/')
    f0809 = pd.read_html('https://skatingscores.com/0809/gpcan/sr/women/results/')
    f0910 = pd.read_html('https://skatingscores.com/0910/gpcan/sr/women/results/')
    f1011 = pd.read_html('https://skatingscores.com/1011/gpcan/sr/women/results/')
    f1112 = pd.read_html('https://skatingscores.com/1112/gpcan/sr/women/results/')
    f1213 = pd.read_html('https://skatingscores.com/1213/gpcan/sr/women/results/')
    f1314 = pd.read_html('https://skatingscores.com/1314/gpcan/sr/women/results/')
    f1415 = pd.read_html('https://skatingscores.com/1415/gpcan/sr/women/results/')
    f1516 = pd.read_html('https://skatingscores.com/1516/gpcan/sr/women/results/')
    f1617 = pd.read_html('https://skatingscores.com/1617/gpcan/sr/women/results/')
    f1718 = pd.read_html('https://skatingscores.com/1718/gpcan/sr/women/results/')
    f1819 = pd.read_html('https://skatingscores.com/1819/gpcan/sr/women/results/')
    f1920 = pd.read_html('https://skatingscores.com/1920/gpcan/sr/women/results/')
    f2122 = pd.read_html('https://skatingscores.com/2122/gpcan/sr/women/results/')
    b0304 = b0304[1]
    b0405 = b0405[1]
    b0506 = b0506[1]
    b0607 = b0607[1]
    b0708 = b0708[1]
    b0809 = b0809[1]
    b0910 = b0910[1]
    b1011 = b1011[1]
    b1112 = b1112[1]
    b1213 = b1213[1]
    b1314 = b1314[1]
    b1415 = b1415[1]
    b1516 = b1516[1]
    b1617 = b1617[1]
    b1718 = b1718[1]
    b1819 = b1819[1]
    b1920 = b1920[1]
    b2122 = b2122[1]
    b0304['season'] = 2004
    b0405['season'] = 2005
    b0506['season'] = 2006
    b0607['season'] = 2007
    b0708['season'] = 2008
    b0809['season'] = 2009
    b0910['season'] = 2010
    b1011['season'] = 2011
    b1112['season'] = 2012
    b1213['season'] = 2013
    b1314['season'] = 2014
    b1415['season'] = 2015
    b1516['season'] = 2016
    b1617['season'] = 2017
    b1718['season'] = 2018
    b1819['season'] = 2019
    b1920['season'] = 2020
    b2122['season'] = 2022
    c0304 = c0304[1]
    c0405 = c0405[1]
    c0506 = c0506[1]
    c0607 = c0607[1]
    c0708 = c0708[1]
    c0809 = c0809[1]
    c0910 = c0910[1]
    c1011 = c1011[1]
    c1112 = c1112[1]
    c1213 = c1213[1]
    c1314 = c1314[1]
    c1415 = c1415[1]
    c1516 = c1516[1]
    c1617 = c1617[1]
    c1718 = c1718[1]
    c1819 = c1819[1]
    c1920 = c1920[1]
    c2122 = c2122[1]
    c0304['season'] = 2004
    c0405['season'] = 2005
    c0506['season'] = 2006
    c0607['season'] = 2007
    c0708['season'] = 2008
    c0809['season'] = 2009
    c0910['season'] = 2010
    c1011['season'] = 2011
    c1112['season'] = 2012
    c1213['season'] = 2013
    c1314['season'] = 2014
    c1415['season'] = 2015
    c1516['season'] = 2016
    c1617['season'] = 2017
    c1718['season'] = 2018
    c1819['season'] = 2019
    c1920['season'] = 2020
    c2122['season'] = 2022
    f0304 = f0304[1]
    f0405 = f0405[1]
    f0506 = f0506[1]
    f0607 = f0607[1]
    f0708 = f0708[1]
    f0809 = f0809[1]
    f0910 = f0910[1]
    f1011 = f1011[1]
    f1112 = f1112[1]
    f1213 = f1213[1]
    f1314 = f1314[1]
    f1415 = f1415[1]
    f1516 = f1516[1]
    f1617 = f1617[1]
    f1718 = f1718[1]
    f1819 = f1819[1]
    f1920 = f1920[1]
    f2122 = f2122[1]
    f0304['season'] = 2004
    f0405['season'] = 2005
    f0506['season'] = 2006
    f0607['season'] = 2007
    f0708['season'] = 2008
    f0809['season'] = 2009
    f0910['season'] = 2010
    f1011['season'] = 2011
    f1112['season'] = 2012
    f1213['season'] = 2013
    f1314['season'] = 2014
    f1415['season'] = 2015
    f1516['season'] = 2016
    f1617['season'] = 2017
    f1718['season'] = 2018
    f1819['season'] = 2019
    f1920['season'] = 2020
    f2122['season'] = 2022
    f0304['skater_name'] = f0304['Skater']
    f0405['skater_name'] = f0405['Skater']
    f0506['skater_name'] = f0506['Skater']
    f0607['skater_name'] = f0607['Skater']
    f0708['skater_name'] = f0708['Skater']
    f0809['skater_name'] = f0809['Skater']
    f0910['skater_name'] = f0910['Skater']
    f1011['skater_name'] = f1011['Skater']
    f1112['skater_name'] = f1112['Skater']
    f1213['skater_name'] = f1213['Skater']
    f1314['skater_name'] = f1314['Skater']
    f1415['skater_name'] = f1415['Skater']
    f1516['skater_name'] = f1516['Skater']
    f1617['skater_name'] = f1617['Skater']
    f1718['skater_name'] = f1718['Skater']
    f1819['skater_name'] = f1819['Skater']
    f1920['skater_name'] = f1920['Skater']
    f2122['skater_name'] = f2122['Skater']
    f0304[['first_name','Skater']] = f0304['Skater'].loc[f0304['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0405[['first_name','Skater']] = f0405['Skater'].loc[f0405['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0506[['first_name','Skater']] = f0506['Skater'].loc[f0506['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0607[['first_name','Skater']] = f0607['Skater'].loc[f0607['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0708[['first_name','Skater']] = f0708['Skater'].loc[f0708['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0809[['first_name','Skater']] = f0809['Skater'].loc[f0809['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0910[['first_name','Skater']] = f0910['Skater'].loc[f0910['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1011[['first_name','Skater']] = f1011['Skater'].loc[f1011['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1112[['first_name','Skater']] = f1112['Skater'].loc[f1112['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1213[['first_name','Skater']] = f1213['Skater'].loc[f1213['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1314[['first_name','Skater']] = f1314['Skater'].loc[f1314['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1415[['first_name','Skater']] = f1415['Skater'].loc[f1415['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1516[['first_name','Skater']] = f1516['Skater'].loc[f1516['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1617[['first_name','Skater']] = f1617['Skater'].loc[f1617['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1718[['first_name','Skater']] = f1718['Skater'].loc[f1718['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1819[['first_name','Skater']] = f1819['Skater'].loc[f1819['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1920[['first_name','Skater']] = f1920['Skater'].loc[f1920['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f2122[['first_name','Skater']] = f2122['Skater'].loc[f2122['Skater'].str.split().str.len() == 2].str.split(expand=True)
    s2004 = f0304.merge(b0304,on='Skater').merge(c0304, on='Skater')
    s2005 = f0405.merge(b0405,on='Skater').merge(c0405, on='Skater')
    s2006 = f0506.merge(b0506,on='Skater').merge(c0506, on='Skater')
    s2007 = f0607.merge(b0607,on='Skater').merge(c0607, on='Skater')
    s2008 = f0708.merge(b0708,on='Skater').merge(c0708, on='Skater')
    s2009 = f0809.merge(b0809,on='Skater').merge(c0809, on='Skater')
    s2010 = f0910.merge(b0910,on='Skater').merge(c0910, on='Skater')
    s2011 = f1011.merge(b1011,on='Skater').merge(c1011, on='Skater')
    s2012 = f1112.merge(b1112,on='Skater').merge(c1112, on='Skater')
    s2013 = f1213.merge(b1213,on='Skater').merge(c1213, on='Skater')
    s2014 = f1314.merge(b1314,on='Skater').merge(c1314, on='Skater')
    s2015 = f1415.merge(b1415,on='Skater').merge(c1415, on='Skater')
    s2016 = f1516.merge(b1516,on='Skater').merge(c1516, on='Skater')
    s2017 = f1617.merge(b1617,on='Skater').merge(c1617, on='Skater')
    s2018 = f1718.merge(b1718,on='Skater').merge(c1718, on='Skater')
    s2019 = f1819.merge(b1819,on='Skater').merge(c1819, on='Skater')
    s2020 = f1920.merge(b1920,on='Skater').merge(c1920, on='Skater')
    s2022 = f2122.merge(b2122,on='Skater').merge(c2122, on='Skater')
    gp_canada = pd.concat([s2004, s2005, s2006, s2007, s2008, s2009, s2010, s2011, s2012, s2013, s2014, 
                            s2015, s2016, s2017, s2018, s2019, s2020, s2022], axis=0)
    gp_canada['event'] = 'gp_canada'
    return gp_canada



def get_gp_france():
    
    b0304 = pd.read_html('https://skatingscores.com/0304/gpfra/sr/women/short/quicklook/')
    b0405 = pd.read_html('https://skatingscores.com/0405/gpfra/sr/women/short/quicklook/')
    b0506 = pd.read_html('https://skatingscores.com/0506/gpfra/sr/women/short/quicklook/')
    b0607 = pd.read_html('https://skatingscores.com/0607/gpfra/sr/women/short/quicklook/')
    b0708 = pd.read_html('https://skatingscores.com/0708/gpfra/sr/women/short/quicklook/')
    b0809 = pd.read_html('https://skatingscores.com/0809/gpfra/sr/women/short/quicklook/')
    b0910 = pd.read_html('https://skatingscores.com/0910/gpfra/sr/women/short/quicklook/')
    b1011 = pd.read_html('https://skatingscores.com/1011/gpfra/sr/women/short/quicklook/')
    b1112 = pd.read_html('https://skatingscores.com/1112/gpfra/sr/women/short/quicklook/')
    b1213 = pd.read_html('https://skatingscores.com/1213/gpfra/sr/women/short/quicklook/')
    b1314 = pd.read_html('https://skatingscores.com/1314/gpfra/sr/women/short/quicklook/')
    b1415 = pd.read_html('https://skatingscores.com/1415/gpfra/sr/women/short/quicklook/')
    b1617 = pd.read_html('https://skatingscores.com/1617/gpfra/sr/women/short/quicklook/')
    b1718 = pd.read_html('https://skatingscores.com/1718/gpfra/sr/women/short/quicklook/')
    b1819 = pd.read_html('https://skatingscores.com/1819/gpfra/sr/women/short/quicklook/')
    b1920 = pd.read_html('https://skatingscores.com/1920/gpfra/sr/women/short/quicklook/')
    b2122 = pd.read_html('https://skatingscores.com/2122/gpfra/sr/women/short/quicklook/')
    c0304 = pd.read_html('https://skatingscores.com/0304/gpfra/sr/women/long/quicklook/')
    c0405 = pd.read_html('https://skatingscores.com/0405/gpfra/sr/women/long/quicklook/')
    c0506 = pd.read_html('https://skatingscores.com/0506/gpfra/sr/women/long/quicklook/')
    c0607 = pd.read_html('https://skatingscores.com/0607/gpfra/sr/women/long/quicklook/')
    c0708 = pd.read_html('https://skatingscores.com/0708/gpfra/sr/women/long/quicklook/')
    c0809 = pd.read_html('https://skatingscores.com/0809/gpfra/sr/women/long/quicklook/')
    c0910 = pd.read_html('https://skatingscores.com/0910/gpfra/sr/women/long/quicklook/')
    c1011 = pd.read_html('https://skatingscores.com/1011/gpfra/sr/women/long/quicklook/')
    c1112 = pd.read_html('https://skatingscores.com/1112/gpfra/sr/women/long/quicklook/')
    c1213 = pd.read_html('https://skatingscores.com/1213/gpfra/sr/women/long/quicklook/')
    c1314 = pd.read_html('https://skatingscores.com/1314/gpfra/sr/women/long/quicklook/')
    c1415 = pd.read_html('https://skatingscores.com/1415/gpfra/sr/women/long/quicklook/')
    c1617 = pd.read_html('https://skatingscores.com/1617/gpfra/sr/women/long/quicklook/')
    c1718 = pd.read_html('https://skatingscores.com/1718/gpfra/sr/women/long/quicklook/')
    c1819 = pd.read_html('https://skatingscores.com/1819/gpfra/sr/women/long/quicklook/')
    c1920 = pd.read_html('https://skatingscores.com/1920/gpfra/sr/women/long/quicklook/')
    c2122 = pd.read_html('https://skatingscores.com/2122/gpfra/sr/women/long/quicklook/')
    f0304 = pd.read_html('https://skatingscores.com/0304/gpfra/sr/women/results/')
    f0405 = pd.read_html('https://skatingscores.com/0405/gpfra/sr/women/results/')
    f0506 = pd.read_html('https://skatingscores.com/0506/gpfra/sr/women/results/')
    f0607 = pd.read_html('https://skatingscores.com/0607/gpfra/sr/women/results/')
    f0708 = pd.read_html('https://skatingscores.com/0708/gpfra/sr/women/results/')
    f0809 = pd.read_html('https://skatingscores.com/0809/gpfra/sr/women/results/')
    f0910 = pd.read_html('https://skatingscores.com/0910/gpfra/sr/women/results/')
    f1011 = pd.read_html('https://skatingscores.com/1011/gpfra/sr/women/results/')
    f1112 = pd.read_html('https://skatingscores.com/1112/gpfra/sr/women/results/')
    f1213 = pd.read_html('https://skatingscores.com/1213/gpfra/sr/women/results/')
    f1314 = pd.read_html('https://skatingscores.com/1314/gpfra/sr/women/results/')
    f1415 = pd.read_html('https://skatingscores.com/1415/gpfra/sr/women/results/')
    f1617 = pd.read_html('https://skatingscores.com/1617/gpfra/sr/women/results/')
    f1718 = pd.read_html('https://skatingscores.com/1718/gpfra/sr/women/results/')
    f1819 = pd.read_html('https://skatingscores.com/1819/gpfra/sr/women/results/')
    f1920 = pd.read_html('https://skatingscores.com/1920/gpfra/sr/women/results/')
    f2122 = pd.read_html('https://skatingscores.com/2122/gpfra/sr/women/results/')
    b0304 = b0304[1]
    b0405 = b0405[1]
    b0506 = b0506[1]
    b0607 = b0607[1]
    b0708 = b0708[1]
    b0809 = b0809[1]
    b0910 = b0910[1]
    b1011 = b1011[1]
    b1112 = b1112[1]
    b1213 = b1213[1]
    b1314 = b1314[1]
    b1415 = b1415[1]
    b1617 = b1617[1]
    b1718 = b1718[1]
    b1819 = b1819[1]
    b1920 = b1920[1]
    b2122 = b2122[1]
    b0304['season'] = 2004
    b0405['season'] = 2005
    b0506['season'] = 2006
    b0607['season'] = 2007
    b0708['season'] = 2008
    b0809['season'] = 2009
    b0910['season'] = 2010
    b1011['season'] = 2011
    b1112['season'] = 2012
    b1213['season'] = 2013
    b1314['season'] = 2014
    b1415['season'] = 2015
    b1617['season'] = 2017
    b1718['season'] = 2018
    b1819['season'] = 2019
    b1920['season'] = 2020
    b2122['season'] = 2022
    c0304 = c0304[1]
    c0405 = c0405[1]
    c0506 = c0506[1]
    c0607 = c0607[1]
    c0708 = c0708[1]
    c0809 = c0809[1]
    c0910 = c0910[1]
    c1011 = c1011[1]
    c1112 = c1112[1]
    c1213 = c1213[1]
    c1314 = c1314[1]
    c1415 = c1415[1]
    c1617 = c1617[1]
    c1718 = c1718[1]
    c1819 = c1819[1]
    c1920 = c1920[1]
    c2122 = c2122[1]
    c0304['season'] = 2004
    c0405['season'] = 2005
    c0506['season'] = 2006
    c0607['season'] = 2007
    c0708['season'] = 2008
    c0809['season'] = 2009
    c0910['season'] = 2010
    c1011['season'] = 2011
    c1112['season'] = 2012
    c1213['season'] = 2013
    c1314['season'] = 2014
    c1415['season'] = 2015
    c1617['season'] = 2017
    c1718['season'] = 2018
    c1819['season'] = 2019
    c1920['season'] = 2020
    c2122['season'] = 2022
    f0304 = f0304[1]
    f0405 = f0405[1]
    f0506 = f0506[1]
    f0607 = f0607[1]
    f0708 = f0708[1]
    f0809 = f0809[1]
    f0910 = f0910[1]
    f1011 = f1011[1]
    f1112 = f1112[1]
    f1213 = f1213[1]
    f1314 = f1314[1]
    f1415 = f1415[1]
    f1617 = f1617[1]
    f1718 = f1718[1]
    f1819 = f1819[1]
    f1920 = f1920[1]
    f2122 = f2122[1]
    f0304['season'] = 2004
    f0405['season'] = 2005
    f0506['season'] = 2006
    f0607['season'] = 2007
    f0708['season'] = 2008
    f0809['season'] = 2009
    f0910['season'] = 2010
    f1011['season'] = 2011
    f1112['season'] = 2012
    f1213['season'] = 2013
    f1314['season'] = 2014
    f1415['season'] = 2015
    f1617['season'] = 2017
    f1718['season'] = 2018
    f1819['season'] = 2019
    f1920['season'] = 2020
    f2122['season'] = 2022
    f0304['skater_name'] = f0304['Skater']
    f0405['skater_name'] = f0405['Skater']
    f0506['skater_name'] = f0506['Skater']
    f0607['skater_name'] = f0607['Skater']
    f0708['skater_name'] = f0708['Skater']
    f0809['skater_name'] = f0809['Skater']
    f0910['skater_name'] = f0910['Skater']
    f1011['skater_name'] = f1011['Skater']
    f1112['skater_name'] = f1112['Skater']
    f1213['skater_name'] = f1213['Skater']
    f1314['skater_name'] = f1314['Skater']
    f1415['skater_name'] = f1415['Skater']
    f1617['skater_name'] = f1617['Skater']
    f1718['skater_name'] = f1718['Skater']
    f1819['skater_name'] = f1819['Skater']
    f1920['skater_name'] = f1920['Skater']
    f2122['skater_name'] = f2122['Skater']
    f0304[['first_name','Skater']] = f0304['Skater'].loc[f0304['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0405[['first_name','Skater']] = f0405['Skater'].loc[f0405['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0506[['first_name','Skater']] = f0506['Skater'].loc[f0506['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0607[['first_name','Skater']] = f0607['Skater'].loc[f0607['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0708[['first_name','Skater']] = f0708['Skater'].loc[f0708['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0809[['first_name','Skater']] = f0809['Skater'].loc[f0809['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0910[['first_name','Skater']] = f0910['Skater'].loc[f0910['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1011[['first_name','Skater']] = f1011['Skater'].loc[f1011['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1112[['first_name','Skater']] = f1112['Skater'].loc[f1112['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1213[['first_name','Skater']] = f1213['Skater'].loc[f1213['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1314[['first_name','Skater']] = f1314['Skater'].loc[f1314['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1415[['first_name','Skater']] = f1415['Skater'].loc[f1415['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1617[['first_name','Skater']] = f1617['Skater'].loc[f1617['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1718[['first_name','Skater']] = f1718['Skater'].loc[f1718['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1819[['first_name','Skater']] = f1819['Skater'].loc[f1819['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1920[['first_name','Skater']] = f1920['Skater'].loc[f1920['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f2122[['first_name','Skater']] = f2122['Skater'].loc[f2122['Skater'].str.split().str.len() == 2].str.split(expand=True)
    s2004 = f0304.merge(b0304,on='Skater').merge(c0304, on='Skater')
    s2005 = f0405.merge(b0405,on='Skater').merge(c0405, on='Skater')
    s2006 = f0506.merge(b0506,on='Skater').merge(c0506, on='Skater')
    s2007 = f0607.merge(b0607,on='Skater').merge(c0607, on='Skater')
    s2008 = f0708.merge(b0708,on='Skater').merge(c0708, on='Skater')
    s2009 = f0809.merge(b0809,on='Skater').merge(c0809, on='Skater')
    s2010 = f0910.merge(b0910,on='Skater').merge(c0910, on='Skater')
    s2011 = f1011.merge(b1011,on='Skater').merge(c1011, on='Skater')
    s2012 = f1112.merge(b1112,on='Skater').merge(c1112, on='Skater')
    s2013 = f1213.merge(b1213,on='Skater').merge(c1213, on='Skater')
    s2014 = f1314.merge(b1314,on='Skater').merge(c1314, on='Skater')
    s2015 = f1415.merge(b1415,on='Skater').merge(c1415, on='Skater')
    s2017 = f1617.merge(b1617,on='Skater').merge(c1617, on='Skater')
    s2018 = f1718.merge(b1718,on='Skater').merge(c1718, on='Skater')
    s2019 = f1819.merge(b1819,on='Skater').merge(c1819, on='Skater')
    s2020 = f1920.merge(b1920,on='Skater').merge(c1920, on='Skater')
    s2022 = f2122.merge(b2122,on='Skater').merge(c2122, on='Skater')
    gp_france = pd.concat([s2004, s2005, s2006, s2007, s2008, s2009, s2010, s2011, s2012, s2013, s2014, 
                            s2015, s2017, s2018, s2019, s2020, s2022], axis=0)
    gp_france['event'] = 'gp_france'
    return gp_france



def get_gp_china():
    b0304 = pd.read_html('https://skatingscores.com/0304/gpchn/sr/women/short/quicklook/')
    b0405 = pd.read_html('https://skatingscores.com/0405/gpchn/sr/women/short/quicklook/')
    b0506 = pd.read_html('https://skatingscores.com/0506/gpchn/sr/women/short/quicklook/')
    b0607 = pd.read_html('https://skatingscores.com/0607/gpchn/sr/women/short/quicklook/')
    b0708 = pd.read_html('https://skatingscores.com/0708/gpchn/sr/women/short/quicklook/')
    b0809 = pd.read_html('https://skatingscores.com/0809/gpchn/sr/women/short/quicklook/')
    b0910 = pd.read_html('https://skatingscores.com/0910/gpchn/sr/women/short/quicklook/')
    b1011 = pd.read_html('https://skatingscores.com/1011/gpchn/sr/women/short/quicklook/')
    b1112 = pd.read_html('https://skatingscores.com/1112/gpchn/sr/women/short/quicklook/')
    b1213 = pd.read_html('https://skatingscores.com/1213/gpchn/sr/women/short/quicklook/')
    b1314 = pd.read_html('https://skatingscores.com/1314/gpchn/sr/women/short/quicklook/')
    b1415 = pd.read_html('https://skatingscores.com/1415/gpchn/sr/women/short/quicklook/')
    b1516 = pd.read_html('https://skatingscores.com/1516/gpchn/sr/women/short/quicklook/')
    b1617 = pd.read_html('https://skatingscores.com/1617/gpchn/sr/women/short/quicklook/')
    b1718 = pd.read_html('https://skatingscores.com/1718/gpchn/sr/women/short/quicklook/')
    b1920 = pd.read_html('https://skatingscores.com/1920/gpchn/sr/women/short/quicklook/')
    b2021 = pd.read_html('https://skatingscores.com/2021/gpchn/sr/women/short/quicklook/')
    c0304 = pd.read_html('https://skatingscores.com/0304/gpchn/sr/women/long/quicklook/')
    c0405 = pd.read_html('https://skatingscores.com/0405/gpchn/sr/women/long/quicklook/')
    c0506 = pd.read_html('https://skatingscores.com/0506/gpchn/sr/women/long/quicklook/')
    c0607 = pd.read_html('https://skatingscores.com/0607/gpchn/sr/women/long/quicklook/')
    c0708 = pd.read_html('https://skatingscores.com/0708/gpchn/sr/women/long/quicklook/')
    c0809 = pd.read_html('https://skatingscores.com/0809/gpchn/sr/women/long/quicklook/')
    c0910 = pd.read_html('https://skatingscores.com/0910/gpchn/sr/women/long/quicklook/')
    c1011 = pd.read_html('https://skatingscores.com/1011/gpchn/sr/women/long/quicklook/')
    c1112 = pd.read_html('https://skatingscores.com/1112/gpchn/sr/women/long/quicklook/')
    c1213 = pd.read_html('https://skatingscores.com/1213/gpchn/sr/women/long/quicklook/')
    c1314 = pd.read_html('https://skatingscores.com/1314/gpchn/sr/women/long/quicklook/')
    c1415 = pd.read_html('https://skatingscores.com/1415/gpchn/sr/women/long/quicklook/')
    c1516 = pd.read_html('https://skatingscores.com/1516/gpchn/sr/women/long/quicklook/')
    c1617 = pd.read_html('https://skatingscores.com/1617/gpchn/sr/women/long/quicklook/')
    c1718 = pd.read_html('https://skatingscores.com/1718/gpchn/sr/women/long/quicklook/')
    c1920 = pd.read_html('https://skatingscores.com/1920/gpchn/sr/women/long/quicklook/')
    c2021 = pd.read_html('https://skatingscores.com/2021/gpchn/sr/women/long/quicklook/')
    f0304 = pd.read_html('https://skatingscores.com/0304/gpchn/sr/women/results/')
    f0405 = pd.read_html('https://skatingscores.com/0405/gpchn/sr/women/results/')
    f0506 = pd.read_html('https://skatingscores.com/0506/gpchn/sr/women/results/')
    f0607 = pd.read_html('https://skatingscores.com/0607/gpchn/sr/women/results/')
    f0708 = pd.read_html('https://skatingscores.com/0708/gpchn/sr/women/results/')
    f0809 = pd.read_html('https://skatingscores.com/0809/gpchn/sr/women/results/')
    f0910 = pd.read_html('https://skatingscores.com/0910/gpchn/sr/women/results/')
    f1011 = pd.read_html('https://skatingscores.com/1011/gpchn/sr/women/results/')
    f1112 = pd.read_html('https://skatingscores.com/1112/gpchn/sr/women/results/')
    f1213 = pd.read_html('https://skatingscores.com/1213/gpchn/sr/women/results/')
    f1314 = pd.read_html('https://skatingscores.com/1314/gpchn/sr/women/results/')
    f1415 = pd.read_html('https://skatingscores.com/1415/gpchn/sr/women/results/')
    f1516 = pd.read_html('https://skatingscores.com/1516/gpchn/sr/women/results/')
    f1617 = pd.read_html('https://skatingscores.com/1617/gpchn/sr/women/results/')
    f1718 = pd.read_html('https://skatingscores.com/1718/gpchn/sr/women/results/')
    f1920 = pd.read_html('https://skatingscores.com/1920/gpchn/sr/women/results/')
    f2021 = pd.read_html('https://skatingscores.com/2021/gpchn/sr/women/results/')
    b0304 = b0304[1]
    b0405 = b0405[1]
    b0506 = b0506[1]
    b0607 = b0607[1]
    b0708 = b0708[1]
    b0809 = b0809[1]
    b0910 = b0910[1]
    b1011 = b1011[1]
    b1112 = b1112[1]
    b1213 = b1213[1]
    b1314 = b1314[1]
    b1415 = b1415[1]
    b1516 = b1516[1]
    b1617 = b1617[1]
    b1718 = b1718[1]
    b1920 = b1920[1]
    b2021 = b2021[1]
    b0304['season'] = 2004
    b0405['season'] = 2005
    b0506['season'] = 2006
    b0607['season'] = 2007
    b0708['season'] = 2008
    b0809['season'] = 2009
    b0910['season'] = 2010
    b1011['season'] = 2011
    b1112['season'] = 2012
    b1213['season'] = 2013
    b1314['season'] = 2014
    b1415['season'] = 2015
    b1516['season'] = 2016
    b1617['season'] = 2017
    b1718['season'] = 2018
    b1920['season'] = 2020
    b2021['season'] = 2021
    c0304 = c0304[1]
    c0405 = c0405[1]
    c0506 = c0506[1]
    c0607 = c0607[1]
    c0708 = c0708[1]
    c0809 = c0809[1]
    c0910 = c0910[1]
    c1011 = c1011[1]
    c1112 = c1112[1]
    c1213 = c1213[1]
    c1314 = c1314[1]
    c1415 = c1415[1]
    c1516 = c1516[1]
    c1617 = c1617[1]
    c1718 = c1718[1]
    c1920 = c1920[1]
    c2021 = c2021[1]
    c0304['season'] = 2004
    c0405['season'] = 2005
    c0506['season'] = 2006
    c0607['season'] = 2007
    c0708['season'] = 2008
    c0809['season'] = 2009
    c0910['season'] = 2010
    c1011['season'] = 2011
    c1112['season'] = 2012
    c1213['season'] = 2013
    c1314['season'] = 2014
    c1415['season'] = 2015
    c1516['season'] = 2016
    c1617['season'] = 2017
    c1718['season'] = 2018
    c1920['season'] = 2020
    c2021['season'] = 2021
    f0304 = f0304[1]
    f0405 = f0405[1]
    f0506 = f0506[1]
    f0607 = f0607[1]
    f0708 = f0708[1]
    f0809 = f0809[1]
    f0910 = f0910[1]
    f1011 = f1011[1]
    f1112 = f1112[1]
    f1213 = f1213[1]
    f1314 = f1314[1]
    f1415 = f1415[1]
    f1516 = f1516[1]
    f1617 = f1617[1]
    f1718 = f1718[1]
    f1920 = f1920[1]
    f2021 = f2021[1]
    f0304['season'] = 2004
    f0405['season'] = 2005
    f0506['season'] = 2006
    f0607['season'] = 2007
    f0708['season'] = 2008
    f0809['season'] = 2009
    f0910['season'] = 2010
    f1011['season'] = 2011
    f1112['season'] = 2012
    f1213['season'] = 2013
    f1314['season'] = 2014
    f1415['season'] = 2015
    f1516['season'] = 2016
    f1617['season'] = 2017
    f1718['season'] = 2018
    f1920['season'] = 2020
    f2021['season'] = 2021
    f0304['skater_name'] = f0304['Skater']
    f0405['skater_name'] = f0405['Skater']
    f0506['skater_name'] = f0506['Skater']
    f0607['skater_name'] = f0607['Skater']
    f0708['skater_name'] = f0708['Skater']
    f0809['skater_name'] = f0809['Skater']
    f0910['skater_name'] = f0910['Skater']
    f1011['skater_name'] = f1011['Skater']
    f1112['skater_name'] = f1112['Skater']
    f1213['skater_name'] = f1213['Skater']
    f1314['skater_name'] = f1314['Skater']
    f1415['skater_name'] = f1415['Skater']
    f1516['skater_name'] = f1516['Skater']
    f1617['skater_name'] = f1617['Skater']
    f1718['skater_name'] = f1718['Skater']
    f1920['skater_name'] = f1920['Skater']
    f2021['skater_name'] = f2021['Skater']
    f0304[['first_name','Skater']] = f0304['Skater'].loc[f0304['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0405[['first_name','Skater']] = f0405['Skater'].loc[f0405['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0506[['first_name','Skater']] = f0506['Skater'].loc[f0506['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0607[['first_name','Skater']] = f0607['Skater'].loc[f0607['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0708[['first_name','Skater']] = f0708['Skater'].loc[f0708['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0809[['first_name','Skater']] = f0809['Skater'].loc[f0809['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0910[['first_name','Skater']] = f0910['Skater'].loc[f0910['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1011[['first_name','Skater']] = f1011['Skater'].loc[f1011['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1112[['first_name','Skater']] = f1112['Skater'].loc[f1112['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1213[['first_name','Skater']] = f1213['Skater'].loc[f1213['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1314[['first_name','Skater']] = f1314['Skater'].loc[f1314['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1415[['first_name','Skater']] = f1415['Skater'].loc[f1415['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1516[['first_name','Skater']] = f1516['Skater'].loc[f1516['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1617[['first_name','Skater']] = f1617['Skater'].loc[f1617['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1718[['first_name','Skater']] = f1718['Skater'].loc[f1718['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1920[['first_name','Skater']] = f1920['Skater'].loc[f1920['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f2021[['first_name','Skater']] = f2021['Skater'].loc[f2021['Skater'].str.split().str.len() == 2].str.split(expand=True)
    s2004 = f0304.merge(b0304,on='Skater').merge(c0304, on='Skater')
    s2005 = f0405.merge(b0405,on='Skater').merge(c0405, on='Skater')
    s2006 = f0506.merge(b0506,on='Skater').merge(c0506, on='Skater')
    s2007 = f0607.merge(b0607,on='Skater').merge(c0607, on='Skater')
    s2008 = f0708.merge(b0708,on='Skater').merge(c0708, on='Skater')
    s2009 = f0809.merge(b0809,on='Skater').merge(c0809, on='Skater')
    s2010 = f0910.merge(b0910,on='Skater').merge(c0910, on='Skater')
    s2011 = f1011.merge(b1011,on='Skater').merge(c1011, on='Skater')
    s2012 = f1112.merge(b1112,on='Skater').merge(c1112, on='Skater')
    s2013 = f1213.merge(b1213,on='Skater').merge(c1213, on='Skater')
    s2014 = f1314.merge(b1314,on='Skater').merge(c1314, on='Skater')
    s2015 = f1415.merge(b1415,on='Skater').merge(c1415, on='Skater')
    s2016 = f1516.merge(b1516,on='Skater').merge(c1516, on='Skater')
    s2017 = f1617.merge(b1617,on='Skater').merge(c1617, on='Skater')
    s2018 = f1718.merge(b1718,on='Skater').merge(c1718, on='Skater')
    s2020 = f1920.merge(b1920,on='Skater').merge(c1920, on='Skater')
    s2021 = f2021.merge(b2021,on='Skater').merge(c2021, on='Skater')
    gp_china = pd.concat([s2004, s2005, s2006, s2007, s2008, s2009, s2010, s2011, s2012, s2013, s2014, 
                            s2015, s2016, s2017, s2018, s2020, s2021], axis=0)
    gp_china['event'] = 'gp_china'
    return gp_china



def get_gp_russia():

    b0304 = pd.read_html('https://skatingscores.com/0304/gprus/sr/women/short/quicklook/')
    b0405 = pd.read_html('https://skatingscores.com/0405/gprus/sr/women/short/quicklook/')
    b0506 = pd.read_html('https://skatingscores.com/0506/gprus/sr/women/short/quicklook/')
    b0607 = pd.read_html('https://skatingscores.com/0607/gprus/sr/women/short/quicklook/')
    b0708 = pd.read_html('https://skatingscores.com/0708/gprus/sr/women/short/quicklook/')
    b0809 = pd.read_html('https://skatingscores.com/0809/gprus/sr/women/short/quicklook/')
    b0910 = pd.read_html('https://skatingscores.com/0910/gprus/sr/women/short/quicklook/')
    b1011 = pd.read_html('https://skatingscores.com/1011/gprus/sr/women/short/quicklook/')
    b1112 = pd.read_html('https://skatingscores.com/1112/gprus/sr/women/short/quicklook/')
    b1213 = pd.read_html('https://skatingscores.com/1213/gprus/sr/women/short/quicklook/')
    b1314 = pd.read_html('https://skatingscores.com/1314/gprus/sr/women/short/quicklook/')
    b1415 = pd.read_html('https://skatingscores.com/1415/gprus/sr/women/short/quicklook/')
    b1516 = pd.read_html('https://skatingscores.com/1516/gprus/sr/women/short/quicklook/')
    b1617 = pd.read_html('https://skatingscores.com/1617/gprus/sr/women/short/quicklook/')
    b1718 = pd.read_html('https://skatingscores.com/1718/gprus/sr/women/short/quicklook/')
    b1819 = pd.read_html('https://skatingscores.com/1819/gprus/sr/women/short/quicklook/')
    b1920 = pd.read_html('https://skatingscores.com/1920/gprus/sr/women/short/quicklook/')
    b2021 = pd.read_html('https://skatingscores.com/2021/gprus/sr/women/short/quicklook/')
    b2122 = pd.read_html('https://skatingscores.com/2122/gprus/sr/women/short/quicklook/')
    c0304 = pd.read_html('https://skatingscores.com/0304/gprus/sr/women/long/quicklook/')
    c0405 = pd.read_html('https://skatingscores.com/0405/gprus/sr/women/long/quicklook/')
    c0506 = pd.read_html('https://skatingscores.com/0506/gprus/sr/women/long/quicklook/')
    c0607 = pd.read_html('https://skatingscores.com/0607/gprus/sr/women/long/quicklook/')
    c0708 = pd.read_html('https://skatingscores.com/0708/gprus/sr/women/long/quicklook/')
    c0809 = pd.read_html('https://skatingscores.com/0809/gprus/sr/women/long/quicklook/')
    c0910 = pd.read_html('https://skatingscores.com/0910/gprus/sr/women/long/quicklook/')
    c1011 = pd.read_html('https://skatingscores.com/1011/gprus/sr/women/long/quicklook/')
    c1112 = pd.read_html('https://skatingscores.com/1112/gprus/sr/women/long/quicklook/')
    c1213 = pd.read_html('https://skatingscores.com/1213/gprus/sr/women/long/quicklook/')
    c1314 = pd.read_html('https://skatingscores.com/1314/gprus/sr/women/long/quicklook/')
    c1415 = pd.read_html('https://skatingscores.com/1415/gprus/sr/women/long/quicklook/')
    c1516 = pd.read_html('https://skatingscores.com/1516/gprus/sr/women/long/quicklook/')
    c1617 = pd.read_html('https://skatingscores.com/1617/gprus/sr/women/long/quicklook/')
    c1718 = pd.read_html('https://skatingscores.com/1718/gprus/sr/women/long/quicklook/')
    c1819 = pd.read_html('https://skatingscores.com/1819/gprus/sr/women/long/quicklook/')
    c1920 = pd.read_html('https://skatingscores.com/1920/gprus/sr/women/long/quicklook/')
    c2021 = pd.read_html('https://skatingscores.com/2021/gprus/sr/women/long/quicklook/')
    c2122 = pd.read_html('https://skatingscores.com/2122/gprus/sr/women/long/quicklook/')
    f0304 = pd.read_html('https://skatingscores.com/0304/gprus/sr/women/results/')
    f0405 = pd.read_html('https://skatingscores.com/0405/gprus/sr/women/results/')
    f0506 = pd.read_html('https://skatingscores.com/0506/gprus/sr/women/results/')
    f0607 = pd.read_html('https://skatingscores.com/0607/gprus/sr/women/results/')
    f0708 = pd.read_html('https://skatingscores.com/0708/gprus/sr/women/results/')
    f0809 = pd.read_html('https://skatingscores.com/0809/gprus/sr/women/results/')
    f0910 = pd.read_html('https://skatingscores.com/0910/gprus/sr/women/results/')
    f1011 = pd.read_html('https://skatingscores.com/1011/gprus/sr/women/results/')
    f1112 = pd.read_html('https://skatingscores.com/1112/gprus/sr/women/results/')
    f1213 = pd.read_html('https://skatingscores.com/1213/gprus/sr/women/results/')
    f1314 = pd.read_html('https://skatingscores.com/1314/gprus/sr/women/results/')
    f1415 = pd.read_html('https://skatingscores.com/1415/gprus/sr/women/results/')
    f1516 = pd.read_html('https://skatingscores.com/1516/gprus/sr/women/results/')
    f1617 = pd.read_html('https://skatingscores.com/1617/gprus/sr/women/results/')
    f1718 = pd.read_html('https://skatingscores.com/1718/gprus/sr/women/results/')
    f1819 = pd.read_html('https://skatingscores.com/1819/gprus/sr/women/results/')
    f1920 = pd.read_html('https://skatingscores.com/1920/gprus/sr/women/results/')
    f2021 = pd.read_html('https://skatingscores.com/2021/gprus/sr/women/results/')
    f2122 = pd.read_html('https://skatingscores.com/2122/gprus/sr/women/results/')
    b0304 = b0304[1]
    b0405 = b0405[1]
    b0506 = b0506[1]
    b0607 = b0607[1]
    b0708 = b0708[1]
    b0809 = b0809[1]
    b0910 = b0910[1]
    b1011 = b1011[1]
    b1112 = b1112[1]
    b1213 = b1213[1]
    b1314 = b1314[1]
    b1415 = b1415[1]
    b1516 = b1516[1]
    b1617 = b1617[1]
    b1718 = b1718[1]
    b1819 = b1819[1]
    b1920 = b1920[1]
    b2021 = b2021[1]
    b2122 = b2122[1]
    b0304['season'] = 2004
    b0405['season'] = 2005
    b0506['season'] = 2006
    b0607['season'] = 2007
    b0708['season'] = 2008
    b0809['season'] = 2009
    b0910['season'] = 2010
    b1011['season'] = 2011
    b1112['season'] = 2012
    b1213['season'] = 2013
    b1314['season'] = 2014
    b1415['season'] = 2015
    b1516['season'] = 2016
    b1617['season'] = 2017
    b1718['season'] = 2018
    b1819['season'] = 2019
    b1920['season'] = 2020
    b2021['season'] = 2021
    b2122['season'] = 2022
    c0304 = c0304[1]
    c0405 = c0405[1]
    c0506 = c0506[1]
    c0607 = c0607[1]
    c0708 = c0708[1]
    c0809 = c0809[1]
    c0910 = c0910[1]
    c1011 = c1011[1]
    c1112 = c1112[1]
    c1213 = c1213[1]
    c1314 = c1314[1]
    c1415 = c1415[1]
    c1516 = c1516[1]
    c1617 = c1617[1]
    c1718 = c1718[1]
    c1819 = c1819[1]
    c1920 = c1920[1]
    c2021 = c2021[1]
    c2122 = c2122[1]
    c0304['season'] = 2004
    c0405['season'] = 2005
    c0506['season'] = 2006
    c0607['season'] = 2007
    c0708['season'] = 2008
    c0809['season'] = 2009
    c0910['season'] = 2010
    c1011['season'] = 2011
    c1112['season'] = 2012
    c1213['season'] = 2013
    c1314['season'] = 2014
    c1415['season'] = 2015
    c1516['season'] = 2016
    c1617['season'] = 2017
    c1718['season'] = 2018
    c1819['season'] = 2019
    c1920['season'] = 2020
    c2021['season'] = 2021
    c2122['season'] = 2022
    f0304 = f0304[1]
    f0405 = f0405[1]
    f0506 = f0506[1]
    f0607 = f0607[1]
    f0708 = f0708[1]
    f0809 = f0809[1]
    f0910 = f0910[1]
    f1011 = f1011[1]
    f1112 = f1112[1]
    f1213 = f1213[1]
    f1314 = f1314[1]
    f1415 = f1415[1]
    f1516 = f1516[1]
    f1617 = f1617[1]
    f1718 = f1718[1]
    f1819 = f1819[1]
    f1920 = f1920[1]
    f2021 = f2021[1]
    f2122 = f2122[1]
    f0304['season'] = 2004
    f0405['season'] = 2005
    f0506['season'] = 2006
    f0607['season'] = 2007
    f0708['season'] = 2008
    f0809['season'] = 2009
    f0910['season'] = 2010
    f1011['season'] = 2011
    f1112['season'] = 2012
    f1213['season'] = 2013
    f1314['season'] = 2014
    f1415['season'] = 2015
    f1516['season'] = 2016
    f1617['season'] = 2017
    f1718['season'] = 2018
    f1819['season'] = 2019
    f1920['season'] = 2020
    f2021['season'] = 2021
    f2122['season'] = 2022
    f0304['skater_name'] = f0304['Skater']
    f0405['skater_name'] = f0405['Skater']
    f0506['skater_name'] = f0506['Skater']
    f0607['skater_name'] = f0607['Skater']
    f0708['skater_name'] = f0708['Skater']
    f0809['skater_name'] = f0809['Skater']
    f0910['skater_name'] = f0910['Skater']
    f1011['skater_name'] = f1011['Skater']
    f1112['skater_name'] = f1112['Skater']
    f1213['skater_name'] = f1213['Skater']
    f1314['skater_name'] = f1314['Skater']
    f1415['skater_name'] = f1415['Skater']
    f1516['skater_name'] = f1516['Skater']
    f1617['skater_name'] = f1617['Skater']
    f1718['skater_name'] = f1718['Skater']
    f1819['skater_name'] = f1819['Skater']
    f1920['skater_name'] = f1920['Skater']
    f2021['skater_name'] = f2021['Skater']
    f2122['skater_name'] = f2122['Skater']
    f0304[['first_name','Skater']] = f0304['Skater'].loc[f0304['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0405[['first_name','Skater']] = f0405['Skater'].loc[f0405['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0506[['first_name','Skater']] = f0506['Skater'].loc[f0506['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0607[['first_name','Skater']] = f0607['Skater'].loc[f0607['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0708[['first_name','Skater']] = f0708['Skater'].loc[f0708['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0809[['first_name','Skater']] = f0809['Skater'].loc[f0809['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0910[['first_name','Skater']] = f0910['Skater'].loc[f0910['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1011[['first_name','Skater']] = f1011['Skater'].loc[f1011['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1112[['first_name','Skater']] = f1112['Skater'].loc[f1112['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1213[['first_name','Skater']] = f1213['Skater'].loc[f1213['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1314[['first_name','Skater']] = f1314['Skater'].loc[f1314['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1415[['first_name','Skater']] = f1415['Skater'].loc[f1415['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1516[['first_name','Skater']] = f1516['Skater'].loc[f1516['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1617[['first_name','Skater']] = f1617['Skater'].loc[f1617['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1718[['first_name','Skater']] = f1718['Skater'].loc[f1718['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1819[['first_name','Skater']] = f1819['Skater'].loc[f1819['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1920[['first_name','Skater']] = f1920['Skater'].loc[f1920['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f2021[['first_name','Skater']] = f2021['Skater'].loc[f2021['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f2122[['first_name','Skater']] = f2122['Skater'].loc[f2122['Skater'].str.split().str.len() == 2].str.split(expand=True)
    s2004 = f0304.merge(b0304,on='Skater').merge(c0304, on='Skater')
    s2005 = f0405.merge(b0405,on='Skater').merge(c0405, on='Skater')
    s2006 = f0506.merge(b0506,on='Skater').merge(c0506, on='Skater')
    s2007 = f0607.merge(b0607,on='Skater').merge(c0607, on='Skater')
    s2008 = f0708.merge(b0708,on='Skater').merge(c0708, on='Skater')
    s2009 = f0809.merge(b0809,on='Skater').merge(c0809, on='Skater')
    s2010 = f0910.merge(b0910,on='Skater').merge(c0910, on='Skater')
    s2011 = f1011.merge(b1011,on='Skater').merge(c1011, on='Skater')
    s2012 = f1112.merge(b1112,on='Skater').merge(c1112, on='Skater')
    s2013 = f1213.merge(b1213,on='Skater').merge(c1213, on='Skater')
    s2014 = f1314.merge(b1314,on='Skater').merge(c1314, on='Skater')
    s2015 = f1415.merge(b1415,on='Skater').merge(c1415, on='Skater')
    s2016 = f1516.merge(b1516,on='Skater').merge(c1516, on='Skater')
    s2017 = f1617.merge(b1617,on='Skater').merge(c1617, on='Skater')
    s2018 = f1718.merge(b1718,on='Skater').merge(c1718, on='Skater')
    s2019 = f1819.merge(b1819,on='Skater').merge(c1819, on='Skater')
    s2020 = f1920.merge(b1920,on='Skater').merge(c1920, on='Skater')
    s2021 = f2021.merge(b2021,on='Skater').merge(c2021, on='Skater')
    s2022 = f2122.merge(b2122,on='Skater').merge(c2122, on='Skater')
    gp_russia = pd.concat([s2004, s2005, s2006, s2007, s2008, s2009, s2010, s2011, s2012, s2013, s2014, 
                            s2015, s2016, s2017, s2018, s2019, s2020, s2021, s2022], axis=0)
    gp_russia['event'] = 'gp_russia'
    return gp_russia



def get_gp_japan():

    b0304 = pd.read_html('https://skatingscores.com/0304/gpjpn/sr/women/short/quicklook/')
    b0405 = pd.read_html('https://skatingscores.com/0405/gpjpn/sr/women/short/quicklook/')
    b0506 = pd.read_html('https://skatingscores.com/0506/gpjpn/sr/women/short/quicklook/')
    b0607 = pd.read_html('https://skatingscores.com/0607/gpjpn/sr/women/short/quicklook/')
    b0708 = pd.read_html('https://skatingscores.com/0708/gpjpn/sr/women/short/quicklook/')
    b0809 = pd.read_html('https://skatingscores.com/0809/gpjpn/sr/women/short/quicklook/')
    b0910 = pd.read_html('https://skatingscores.com/0910/gpjpn/sr/women/short/quicklook/')
    b1011 = pd.read_html('https://skatingscores.com/1011/gpjpn/sr/women/short/quicklook/')
    b1112 = pd.read_html('https://skatingscores.com/1112/gpjpn/sr/women/short/quicklook/')
    b1213 = pd.read_html('https://skatingscores.com/1213/gpjpn/sr/women/short/quicklook/')
    b1314 = pd.read_html('https://skatingscores.com/1314/gpjpn/sr/women/short/quicklook/')
    b1415 = pd.read_html('https://skatingscores.com/1415/gpjpn/sr/women/short/quicklook/')
    b1516 = pd.read_html('https://skatingscores.com/1516/gpjpn/sr/women/short/quicklook/')
    b1617 = pd.read_html('https://skatingscores.com/1617/gpjpn/sr/women/short/quicklook/')
    b1718 = pd.read_html('https://skatingscores.com/1718/gpjpn/sr/women/short/quicklook/')
    b1819 = pd.read_html('https://skatingscores.com/1819/gpjpn/sr/women/short/quicklook/')
    b1920 = pd.read_html('https://skatingscores.com/1920/gpjpn/sr/women/short/quicklook/')
    b2021 = pd.read_html('https://skatingscores.com/2021/gpjpn/sr/women/short/quicklook/')
    b2122 = pd.read_html('https://skatingscores.com/2122/gpjpn/sr/women/short/quicklook/')
    c0304 = pd.read_html('https://skatingscores.com/0304/gpjpn/sr/women/long/quicklook/')
    c0405 = pd.read_html('https://skatingscores.com/0405/gpjpn/sr/women/long/quicklook/')
    c0506 = pd.read_html('https://skatingscores.com/0506/gpjpn/sr/women/long/quicklook/')
    c0607 = pd.read_html('https://skatingscores.com/0607/gpjpn/sr/women/long/quicklook/')
    c0708 = pd.read_html('https://skatingscores.com/0708/gpjpn/sr/women/long/quicklook/')
    c0809 = pd.read_html('https://skatingscores.com/0809/gpjpn/sr/women/long/quicklook/')
    c0910 = pd.read_html('https://skatingscores.com/0910/gpjpn/sr/women/long/quicklook/')
    c1011 = pd.read_html('https://skatingscores.com/1011/gpjpn/sr/women/long/quicklook/')
    c1112 = pd.read_html('https://skatingscores.com/1112/gpjpn/sr/women/long/quicklook/')
    c1213 = pd.read_html('https://skatingscores.com/1213/gpjpn/sr/women/long/quicklook/')
    c1314 = pd.read_html('https://skatingscores.com/1314/gpjpn/sr/women/long/quicklook/')
    c1415 = pd.read_html('https://skatingscores.com/1415/gpjpn/sr/women/long/quicklook/')
    c1516 = pd.read_html('https://skatingscores.com/1516/gpjpn/sr/women/long/quicklook/')
    c1617 = pd.read_html('https://skatingscores.com/1617/gpjpn/sr/women/long/quicklook/')
    c1718 = pd.read_html('https://skatingscores.com/1718/gpjpn/sr/women/long/quicklook/')
    c1819 = pd.read_html('https://skatingscores.com/1819/gpjpn/sr/women/long/quicklook/')
    c1920 = pd.read_html('https://skatingscores.com/1920/gpjpn/sr/women/long/quicklook/')
    c2021 = pd.read_html('https://skatingscores.com/2021/gpjpn/sr/women/long/quicklook/')
    c2122 = pd.read_html('https://skatingscores.com/2122/gpjpn/sr/women/long/quicklook/')
    f0304 = pd.read_html('https://skatingscores.com/0304/gpjpn/sr/women/results/')
    f0405 = pd.read_html('https://skatingscores.com/0405/gpjpn/sr/women/results/')
    f0506 = pd.read_html('https://skatingscores.com/0506/gpjpn/sr/women/results/')
    f0607 = pd.read_html('https://skatingscores.com/0607/gpjpn/sr/women/results/')
    f0708 = pd.read_html('https://skatingscores.com/0708/gpjpn/sr/women/results/')
    f0809 = pd.read_html('https://skatingscores.com/0809/gpjpn/sr/women/results/')
    f0910 = pd.read_html('https://skatingscores.com/0910/gpjpn/sr/women/results/')
    f1011 = pd.read_html('https://skatingscores.com/1011/gpjpn/sr/women/results/')
    f1112 = pd.read_html('https://skatingscores.com/1112/gpjpn/sr/women/results/')
    f1213 = pd.read_html('https://skatingscores.com/1213/gpjpn/sr/women/results/')
    f1314 = pd.read_html('https://skatingscores.com/1314/gpjpn/sr/women/results/')
    f1415 = pd.read_html('https://skatingscores.com/1415/gpjpn/sr/women/results/')
    f1516 = pd.read_html('https://skatingscores.com/1516/gpjpn/sr/women/results/')
    f1617 = pd.read_html('https://skatingscores.com/1617/gpjpn/sr/women/results/')
    f1718 = pd.read_html('https://skatingscores.com/1718/gpjpn/sr/women/results/')
    f1819 = pd.read_html('https://skatingscores.com/1819/gpjpn/sr/women/results/')
    f1920 = pd.read_html('https://skatingscores.com/1920/gpjpn/sr/women/results/')
    f2021 = pd.read_html('https://skatingscores.com/2021/gpjpn/sr/women/results/')
    f2122 = pd.read_html('https://skatingscores.com/2122/gpjpn/sr/women/results/')
    b0304 = b0304[1]
    b0405 = b0405[1]
    b0506 = b0506[1]
    b0607 = b0607[1]
    b0708 = b0708[1]
    b0809 = b0809[1]
    b0910 = b0910[1]
    b1011 = b1011[1]
    b1112 = b1112[1]
    b1213 = b1213[1]
    b1314 = b1314[1]
    b1415 = b1415[1]
    b1516 = b1516[1]
    b1617 = b1617[1]
    b1718 = b1718[1]
    b1819 = b1819[1]
    b1920 = b1920[1]
    b2021 = b2021[1]
    b2122 = b2122[1]
    b0304['season'] = 2004
    b0405['season'] = 2005
    b0506['season'] = 2006
    b0607['season'] = 2007
    b0708['season'] = 2008
    b0809['season'] = 2009
    b0910['season'] = 2010
    b1011['season'] = 2011
    b1112['season'] = 2012
    b1213['season'] = 2013
    b1314['season'] = 2014
    b1415['season'] = 2015
    b1516['season'] = 2016
    b1617['season'] = 2017
    b1718['season'] = 2018
    b1819['season'] = 2019
    b1920['season'] = 2020
    b2021['season'] = 2021
    b2122['season'] = 2022
    c0304 = c0304[1]
    c0405 = c0405[1]
    c0506 = c0506[1]
    c0607 = c0607[1]
    c0708 = c0708[1]
    c0809 = c0809[1]
    c0910 = c0910[1]
    c1011 = c1011[1]
    c1112 = c1112[1]
    c1213 = c1213[1]
    c1314 = c1314[1]
    c1415 = c1415[1]
    c1516 = c1516[1]
    c1617 = c1617[1]
    c1718 = c1718[1]
    c1819 = c1819[1]
    c1920 = c1920[1]
    c2021 = c2021[1]
    c2122 = c2122[1]
    c0304['season'] = 2004
    c0405['season'] = 2005
    c0506['season'] = 2006
    c0607['season'] = 2007
    c0708['season'] = 2008
    c0809['season'] = 2009
    c0910['season'] = 2010
    c1011['season'] = 2011
    c1112['season'] = 2012
    c1213['season'] = 2013
    c1314['season'] = 2014
    c1415['season'] = 2015
    c1516['season'] = 2016
    c1617['season'] = 2017
    c1718['season'] = 2018
    c1819['season'] = 2019
    c1920['season'] = 2020
    c2021['season'] = 2021
    c2122['season'] = 2022
    f0304 = f0304[1]
    f0405 = f0405[1]
    f0506 = f0506[1]
    f0607 = f0607[1]
    f0708 = f0708[1]
    f0809 = f0809[1]
    f0910 = f0910[1]
    f1011 = f1011[1]
    f1112 = f1112[1]
    f1213 = f1213[1]
    f1314 = f1314[1]
    f1415 = f1415[1]
    f1516 = f1516[1]
    f1617 = f1617[1]
    f1718 = f1718[1]
    f1819 = f1819[1]
    f1920 = f1920[1]
    f2021 = f2021[1]
    f2122 = f2122[1]
    f0304['season'] = 2004
    f0405['season'] = 2005
    f0506['season'] = 2006
    f0607['season'] = 2007
    f0708['season'] = 2008
    f0809['season'] = 2009
    f0910['season'] = 2010
    f1011['season'] = 2011
    f1112['season'] = 2012
    f1213['season'] = 2013
    f1314['season'] = 2014
    f1415['season'] = 2015
    f1516['season'] = 2016
    f1617['season'] = 2017
    f1718['season'] = 2018
    f1819['season'] = 2019
    f1920['season'] = 2020
    f2021['season'] = 2021
    f2122['season'] = 2022
    f0304['skater_name'] = f0304['Skater']
    f0405['skater_name'] = f0405['Skater']
    f0506['skater_name'] = f0506['Skater']
    f0607['skater_name'] = f0607['Skater']
    f0708['skater_name'] = f0708['Skater']
    f0809['skater_name'] = f0809['Skater']
    f0910['skater_name'] = f0910['Skater']
    f1011['skater_name'] = f1011['Skater']
    f1112['skater_name'] = f1112['Skater']
    f1213['skater_name'] = f1213['Skater']
    f1314['skater_name'] = f1314['Skater']
    f1415['skater_name'] = f1415['Skater']
    f1516['skater_name'] = f1516['Skater']
    f1617['skater_name'] = f1617['Skater']
    f1718['skater_name'] = f1718['Skater']
    f1819['skater_name'] = f1819['Skater']
    f1920['skater_name'] = f1920['Skater']
    f2021['skater_name'] = f2021['Skater']
    f2122['skater_name'] = f2122['Skater']
    f0304[['first_name','Skater']] = f0304['Skater'].loc[f0304['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0405[['first_name','Skater']] = f0405['Skater'].loc[f0405['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0506[['first_name','Skater']] = f0506['Skater'].loc[f0506['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0607[['first_name','Skater']] = f0607['Skater'].loc[f0607['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0708[['first_name','Skater']] = f0708['Skater'].loc[f0708['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0809[['first_name','Skater']] = f0809['Skater'].loc[f0809['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0910[['first_name','Skater']] = f0910['Skater'].loc[f0910['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1011[['first_name','Skater']] = f1011['Skater'].loc[f1011['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1112[['first_name','Skater']] = f1112['Skater'].loc[f1112['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1213[['first_name','Skater']] = f1213['Skater'].loc[f1213['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1314[['first_name','Skater']] = f1314['Skater'].loc[f1314['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1415[['first_name','Skater']] = f1415['Skater'].loc[f1415['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1516[['first_name','Skater']] = f1516['Skater'].loc[f1516['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1617[['first_name','Skater']] = f1617['Skater'].loc[f1617['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1718[['first_name','Skater']] = f1718['Skater'].loc[f1718['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1819[['first_name','Skater']] = f1819['Skater'].loc[f1819['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1920[['first_name','Skater']] = f1920['Skater'].loc[f1920['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f2021[['first_name','Skater']] = f2021['Skater'].loc[f2021['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f2122[['first_name','Skater']] = f2122['Skater'].loc[f2122['Skater'].str.split().str.len() == 2].str.split(expand=True)
    s2004 = f0304.merge(b0304,on='Skater').merge(c0304, on='Skater')
    s2005 = f0405.merge(b0405,on='Skater').merge(c0405, on='Skater')
    s2006 = f0506.merge(b0506,on='Skater').merge(c0506, on='Skater')
    s2007 = f0607.merge(b0607,on='Skater').merge(c0607, on='Skater')
    s2008 = f0708.merge(b0708,on='Skater').merge(c0708, on='Skater')
    s2009 = f0809.merge(b0809,on='Skater').merge(c0809, on='Skater')
    s2010 = f0910.merge(b0910,on='Skater').merge(c0910, on='Skater')
    s2011 = f1011.merge(b1011,on='Skater').merge(c1011, on='Skater')
    s2012 = f1112.merge(b1112,on='Skater').merge(c1112, on='Skater')
    s2013 = f1213.merge(b1213,on='Skater').merge(c1213, on='Skater')
    s2014 = f1314.merge(b1314,on='Skater').merge(c1314, on='Skater')
    s2015 = f1415.merge(b1415,on='Skater').merge(c1415, on='Skater')
    s2016 = f1516.merge(b1516,on='Skater').merge(c1516, on='Skater')
    s2017 = f1617.merge(b1617,on='Skater').merge(c1617, on='Skater')
    s2018 = f1718.merge(b1718,on='Skater').merge(c1718, on='Skater')
    s2019 = f1819.merge(b1819,on='Skater').merge(c1819, on='Skater')
    s2020 = f1920.merge(b1920,on='Skater').merge(c1920, on='Skater')
    s2021 = f2021.merge(b2021,on='Skater').merge(c2021, on='Skater')
    s2022 = f2122.merge(b2122,on='Skater').merge(c2122, on='Skater')
    gp_japan = pd.concat([s2004, s2005, s2006, s2007, s2008, s2009, s2010, s2011, s2012, s2013, s2014, 
                            s2015, s2016, s2017, s2018, s2019, s2020, s2021, s2022], axis=0)
    gp_japan['event'] = 'gp_japan'
    return gp_japan


def get_gp_final():

    b0304 = pd.read_html('https://skatingscores.com/0304/gpf/sr/women/short/quicklook/')
    b0405 = pd.read_html('https://skatingscores.com/0405/gpf/sr/women/short/quicklook/')
    b0506 = pd.read_html('https://skatingscores.com/0506/gpf/sr/women/short/quicklook/')
    b0607 = pd.read_html('https://skatingscores.com/0607/gpf/sr/women/short/quicklook/')
    b0708 = pd.read_html('https://skatingscores.com/0708/gpf/sr/women/short/quicklook/')
    b0809 = pd.read_html('https://skatingscores.com/0809/gpf/sr/women/short/quicklook/')
    b0910 = pd.read_html('https://skatingscores.com/0910/gpf/sr/women/short/quicklook/')
    b1011 = pd.read_html('https://skatingscores.com/1011/gpf/sr/women/short/quicklook/')
    b1112 = pd.read_html('https://skatingscores.com/1112/gpf/sr/women/short/quicklook/')
    b1213 = pd.read_html('https://skatingscores.com/1213/gpf/sr/women/short/quicklook/')
    b1314 = pd.read_html('https://skatingscores.com/1314/gpf/sr/women/short/quicklook/')
    b1415 = pd.read_html('https://skatingscores.com/1415/gpf/sr/women/short/quicklook/')
    b1516 = pd.read_html('https://skatingscores.com/1516/gpf/sr/women/short/quicklook/')
    b1617 = pd.read_html('https://skatingscores.com/1617/gpf/sr/women/short/quicklook/')
    b1718 = pd.read_html('https://skatingscores.com/1718/gpf/sr/women/short/quicklook/')
    b1819 = pd.read_html('https://skatingscores.com/1819/gpf/sr/women/short/quicklook/')
    b1920 = pd.read_html('https://skatingscores.com/1920/gpf/sr/women/short/quicklook/')
    c0304 = pd.read_html('https://skatingscores.com/0304/gpf/sr/women/long/quicklook/')
    c0405 = pd.read_html('https://skatingscores.com/0405/gpf/sr/women/long/quicklook/')
    c0506 = pd.read_html('https://skatingscores.com/0506/gpf/sr/women/long/quicklook/')
    c0607 = pd.read_html('https://skatingscores.com/0607/gpf/sr/women/long/quicklook/')
    c0708 = pd.read_html('https://skatingscores.com/0708/gpf/sr/women/long/quicklook/')
    c0809 = pd.read_html('https://skatingscores.com/0809/gpf/sr/women/long/quicklook/')
    c0910 = pd.read_html('https://skatingscores.com/0910/gpf/sr/women/long/quicklook/')
    c1011 = pd.read_html('https://skatingscores.com/1011/gpf/sr/women/long/quicklook/')
    c1112 = pd.read_html('https://skatingscores.com/1112/gpf/sr/women/long/quicklook/')
    c1213 = pd.read_html('https://skatingscores.com/1213/gpf/sr/women/long/quicklook/')
    c1314 = pd.read_html('https://skatingscores.com/1314/gpf/sr/women/long/quicklook/')
    c1415 = pd.read_html('https://skatingscores.com/1415/gpf/sr/women/long/quicklook/')
    c1516 = pd.read_html('https://skatingscores.com/1516/gpf/sr/women/long/quicklook/')
    c1617 = pd.read_html('https://skatingscores.com/1617/gpf/sr/women/long/quicklook/')
    c1718 = pd.read_html('https://skatingscores.com/1718/gpf/sr/women/long/quicklook/')
    c1819 = pd.read_html('https://skatingscores.com/1819/gpf/sr/women/long/quicklook/')
    c1920 = pd.read_html('https://skatingscores.com/1920/gpf/sr/women/long/quicklook/')
    f0304 = pd.read_html('https://skatingscores.com/0304/gpf/sr/women/results/')
    f0405 = pd.read_html('https://skatingscores.com/0405/gpf/sr/women/results/')
    f0506 = pd.read_html('https://skatingscores.com/0506/gpf/sr/women/results/')
    f0607 = pd.read_html('https://skatingscores.com/0607/gpf/sr/women/results/')
    f0708 = pd.read_html('https://skatingscores.com/0708/gpf/sr/women/results/')
    f0809 = pd.read_html('https://skatingscores.com/0809/gpf/sr/women/results/')
    f0910 = pd.read_html('https://skatingscores.com/0910/gpf/sr/women/results/')
    f1011 = pd.read_html('https://skatingscores.com/1011/gpf/sr/women/results/')
    f1112 = pd.read_html('https://skatingscores.com/1112/gpf/sr/women/results/')
    f1213 = pd.read_html('https://skatingscores.com/1213/gpf/sr/women/results/')
    f1314 = pd.read_html('https://skatingscores.com/1314/gpf/sr/women/results/')
    f1415 = pd.read_html('https://skatingscores.com/1415/gpf/sr/women/results/')
    f1516 = pd.read_html('https://skatingscores.com/1516/gpf/sr/women/results/')
    f1617 = pd.read_html('https://skatingscores.com/1617/gpf/sr/women/results/')
    f1718 = pd.read_html('https://skatingscores.com/1718/gpf/sr/women/results/')
    f1819 = pd.read_html('https://skatingscores.com/1819/gpf/sr/women/results/')
    f1920 = pd.read_html('https://skatingscores.com/1920/gpf/sr/women/results/')
    b0304 = b0304[1]
    b0405 = b0405[1]
    b0506 = b0506[1]
    b0607 = b0607[1]
    b0708 = b0708[1]
    b0809 = b0809[1]
    b0910 = b0910[1]
    b1011 = b1011[1]
    b1112 = b1112[1]
    b1213 = b1213[1]
    b1314 = b1314[1]
    b1415 = b1415[1]
    b1516 = b1516[1]
    b1617 = b1617[1]
    b1718 = b1718[1]
    b1819 = b1819[1]
    b1920 = b1920[1]
    b0304['season'] = 2004
    b0405['season'] = 2005
    b0506['season'] = 2006
    b0607['season'] = 2007
    b0708['season'] = 2008
    b0809['season'] = 2009
    b0910['season'] = 2010
    b1011['season'] = 2011
    b1112['season'] = 2012
    b1213['season'] = 2013
    b1314['season'] = 2014
    b1415['season'] = 2015
    b1516['season'] = 2016
    b1617['season'] = 2017
    b1718['season'] = 2018
    b1819['season'] = 2019
    b1920['season'] = 2020
    c0304 = c0304[1]
    c0405 = c0405[1]
    c0506 = c0506[1]
    c0607 = c0607[1]
    c0708 = c0708[1]
    c0809 = c0809[1]
    c0910 = c0910[1]
    c1011 = c1011[1]
    c1112 = c1112[1]
    c1213 = c1213[1]
    c1314 = c1314[1]
    c1415 = c1415[1]
    c1516 = c1516[1]
    c1617 = c1617[1]
    c1718 = c1718[1]
    c1819 = c1819[1]
    c1920 = c1920[1]
    c0304['season'] = 2004
    c0405['season'] = 2005
    c0506['season'] = 2006
    c0607['season'] = 2007
    c0708['season'] = 2008
    c0809['season'] = 2009
    c0910['season'] = 2010
    c1011['season'] = 2011
    c1112['season'] = 2012
    c1213['season'] = 2013
    c1314['season'] = 2014
    c1415['season'] = 2015
    c1516['season'] = 2016
    c1617['season'] = 2017
    c1718['season'] = 2018
    c1819['season'] = 2019
    c1920['season'] = 2020
    f0304 = f0304[1]
    f0405 = f0405[1]
    f0506 = f0506[1]
    f0607 = f0607[1]
    f0708 = f0708[1]
    f0809 = f0809[1]
    f0910 = f0910[1]
    f1011 = f1011[1]
    f1112 = f1112[1]
    f1213 = f1213[1]
    f1314 = f1314[1]
    f1415 = f1415[1]
    f1516 = f1516[1]
    f1617 = f1617[1]
    f1718 = f1718[1]
    f1819 = f1819[1]
    f1920 = f1920[1]
    f0304['season'] = 2004
    f0405['season'] = 2005
    f0506['season'] = 2006
    f0607['season'] = 2007
    f0708['season'] = 2008
    f0809['season'] = 2009
    f0910['season'] = 2010
    f1011['season'] = 2011
    f1112['season'] = 2012
    f1213['season'] = 2013
    f1314['season'] = 2014
    f1415['season'] = 2015
    f1516['season'] = 2016
    f1617['season'] = 2017
    f1718['season'] = 2018
    f1819['season'] = 2019
    f1920['season'] = 2020
    f0304['skater_name'] = f0304['Skater']
    f0405['skater_name'] = f0405['Skater']
    f0506['skater_name'] = f0506['Skater']
    f0607['skater_name'] = f0607['Skater']
    f0708['skater_name'] = f0708['Skater']
    f0809['skater_name'] = f0809['Skater']
    f0910['skater_name'] = f0910['Skater']
    f1011['skater_name'] = f1011['Skater']
    f1112['skater_name'] = f1112['Skater']
    f1213['skater_name'] = f1213['Skater']
    f1314['skater_name'] = f1314['Skater']
    f1415['skater_name'] = f1415['Skater']
    f1516['skater_name'] = f1516['Skater']
    f1617['skater_name'] = f1617['Skater']
    f1718['skater_name'] = f1718['Skater']
    f1819['skater_name'] = f1819['Skater']
    f1920['skater_name'] = f1920['Skater']
    f0304[['first_name','Skater']] = f0304['Skater'].loc[f0304['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0405[['first_name','Skater']] = f0405['Skater'].loc[f0405['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0506[['first_name','Skater']] = f0506['Skater'].loc[f0506['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0607[['first_name','Skater']] = f0607['Skater'].loc[f0607['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0708[['first_name','Skater']] = f0708['Skater'].loc[f0708['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0809[['first_name','Skater']] = f0809['Skater'].loc[f0809['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0910[['first_name','Skater']] = f0910['Skater'].loc[f0910['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1011[['first_name','Skater']] = f1011['Skater'].loc[f1011['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1112[['first_name','Skater']] = f1112['Skater'].loc[f1112['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1213[['first_name','Skater']] = f1213['Skater'].loc[f1213['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1314[['first_name','Skater']] = f1314['Skater'].loc[f1314['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1415[['first_name','Skater']] = f1415['Skater'].loc[f1415['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1516[['first_name','Skater']] = f1516['Skater'].loc[f1516['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1617[['first_name','Skater']] = f1617['Skater'].loc[f1617['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1718[['first_name','Skater']] = f1718['Skater'].loc[f1718['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1819[['first_name','Skater']] = f1819['Skater'].loc[f1819['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1920[['first_name','Skater']] = f1920['Skater'].loc[f1920['Skater'].str.split().str.len() == 2].str.split(expand=True)
    s2004 = f0304.merge(b0304,on='Skater').merge(c0304, on='Skater')
    s2005 = f0405.merge(b0405,on='Skater').merge(c0405, on='Skater')
    s2006 = f0506.merge(b0506,on='Skater').merge(c0506, on='Skater')
    s2007 = f0607.merge(b0607,on='Skater').merge(c0607, on='Skater')
    s2008 = f0708.merge(b0708,on='Skater').merge(c0708, on='Skater')
    s2009 = f0809.merge(b0809,on='Skater').merge(c0809, on='Skater')
    s2010 = f0910.merge(b0910,on='Skater').merge(c0910, on='Skater')
    s2011 = f1011.merge(b1011,on='Skater').merge(c1011, on='Skater')
    s2012 = f1112.merge(b1112,on='Skater').merge(c1112, on='Skater')
    s2013 = f1213.merge(b1213,on='Skater').merge(c1213, on='Skater')
    s2014 = f1314.merge(b1314,on='Skater').merge(c1314, on='Skater')
    s2015 = f1415.merge(b1415,on='Skater').merge(c1415, on='Skater')
    s2016 = f1516.merge(b1516,on='Skater').merge(c1516, on='Skater')
    s2017 = f1617.merge(b1617,on='Skater').merge(c1617, on='Skater')
    s2018 = f1718.merge(b1718,on='Skater').merge(c1718, on='Skater')
    s2019 = f1819.merge(b1819,on='Skater').merge(c1819, on='Skater')
    s2020 = f1920.merge(b1920,on='Skater').merge(c1920, on='Skater')
    gp_final = pd.concat([s2004, s2005, s2006, s2007, s2008, s2009, s2010, s2011, s2012, s2013, s2014, 
                            s2015, s2016, s2017, s2018, s2019, s2020], axis=0)
    gp_final['event'] = 'gp_final'
    return gp_final


def get_worlds():

    b0405 = pd.read_html('https://skatingscores.com/0405/wc/sr/women/short/quicklook/')
    b0506 = pd.read_html('https://skatingscores.com/0506/wc/sr/women/short/quicklook/')
    b0607 = pd.read_html('https://skatingscores.com/0607/wc/sr/women/short/quicklook/')
    b0708 = pd.read_html('https://skatingscores.com/0708/wc/sr/women/short/quicklook/')
    b0809 = pd.read_html('https://skatingscores.com/0809/wc/sr/women/short/quicklook/')
    b0910 = pd.read_html('https://skatingscores.com/0910/wc/sr/women/short/quicklook/')
    b1011 = pd.read_html('https://skatingscores.com/1011/wc/sr/women/short/quicklook/')
    b1112 = pd.read_html('https://skatingscores.com/1112/wc/sr/women/short/quicklook/')
    b1213 = pd.read_html('https://skatingscores.com/1213/wc/sr/women/short/quicklook/')
    b1314 = pd.read_html('https://skatingscores.com/1314/wc/sr/women/short/quicklook/')
    b1415 = pd.read_html('https://skatingscores.com/1415/wc/sr/women/short/quicklook/')
    b1516 = pd.read_html('https://skatingscores.com/1516/wc/sr/women/short/quicklook/')
    b1617 = pd.read_html('https://skatingscores.com/1617/wc/sr/women/short/quicklook/')
    b1718 = pd.read_html('https://skatingscores.com/1718/wc/sr/women/short/quicklook/')
    b1819 = pd.read_html('https://skatingscores.com/1819/wc/sr/women/short/quicklook/')
    b2021 = pd.read_html('https://skatingscores.com/2021/wc/sr/women/short/quicklook/')
    b2122 = pd.read_html('https://skatingscores.com/2122/wc/sr/women/short/quicklook/')
    c0405 = pd.read_html('https://skatingscores.com/0405/wc/sr/women/long/quicklook/')
    c0506 = pd.read_html('https://skatingscores.com/0506/wc/sr/women/long/quicklook/')
    c0607 = pd.read_html('https://skatingscores.com/0607/wc/sr/women/long/quicklook/')
    c0708 = pd.read_html('https://skatingscores.com/0708/wc/sr/women/long/quicklook/')
    c0809 = pd.read_html('https://skatingscores.com/0809/wc/sr/women/long/quicklook/')
    c0910 = pd.read_html('https://skatingscores.com/0910/wc/sr/women/long/quicklook/')
    c1011 = pd.read_html('https://skatingscores.com/1011/wc/sr/women/long/quicklook/')
    c1112 = pd.read_html('https://skatingscores.com/1112/wc/sr/women/long/quicklook/')
    c1213 = pd.read_html('https://skatingscores.com/1213/wc/sr/women/long/quicklook/')
    c1314 = pd.read_html('https://skatingscores.com/1314/wc/sr/women/long/quicklook/')
    c1415 = pd.read_html('https://skatingscores.com/1415/wc/sr/women/long/quicklook/')
    c1516 = pd.read_html('https://skatingscores.com/1516/wc/sr/women/long/quicklook/')
    c1617 = pd.read_html('https://skatingscores.com/1617/wc/sr/women/long/quicklook/')
    c1718 = pd.read_html('https://skatingscores.com/1718/wc/sr/women/long/quicklook/')
    c1819 = pd.read_html('https://skatingscores.com/1819/wc/sr/women/long/quicklook/')
    c2021 = pd.read_html('https://skatingscores.com/2021/wc/sr/women/long/quicklook/')
    c2122 = pd.read_html('https://skatingscores.com/2122/wc/sr/women/long/quicklook/')
    f0405 = pd.read_html('https://skatingscores.com/0405/wc/sr/women/results/')
    f0506 = pd.read_html('https://skatingscores.com/0506/wc/sr/women/results/')
    f0607 = pd.read_html('https://skatingscores.com/0607/wc/sr/women/results/')
    f0708 = pd.read_html('https://skatingscores.com/0708/wc/sr/women/results/')
    f0809 = pd.read_html('https://skatingscores.com/0809/wc/sr/women/results/')
    f0910 = pd.read_html('https://skatingscores.com/0910/wc/sr/women/results/')
    f1011 = pd.read_html('https://skatingscores.com/1011/wc/sr/women/results/')
    f1112 = pd.read_html('https://skatingscores.com/1112/wc/sr/women/results/')
    f1213 = pd.read_html('https://skatingscores.com/1213/wc/sr/women/results/')
    f1314 = pd.read_html('https://skatingscores.com/1314/wc/sr/women/results/')
    f1415 = pd.read_html('https://skatingscores.com/1415/wc/sr/women/results/')
    f1516 = pd.read_html('https://skatingscores.com/1516/wc/sr/women/results/')
    f1617 = pd.read_html('https://skatingscores.com/1617/wc/sr/women/results/')
    f1718 = pd.read_html('https://skatingscores.com/1718/wc/sr/women/results/')
    f1819 = pd.read_html('https://skatingscores.com/1819/wc/sr/women/results/')
    f2021 = pd.read_html('https://skatingscores.com/2021/wc/sr/women/results/')
    f2122 = pd.read_html('https://skatingscores.com/2122/wc/sr/women/results/')
    b0405 = b0405[1]
    b0506 = b0506[1]
    b0607 = b0607[1]
    b0708 = b0708[1]
    b0809 = b0809[1]
    b0910 = b0910[1]
    b1011 = b1011[1]
    b1112 = b1112[1]
    b1213 = b1213[1]
    b1314 = b1314[1]
    b1415 = b1415[1]
    b1516 = b1516[1]
    b1617 = b1617[1]
    b1718 = b1718[1]
    b1819 = b1819[1]
    b2021 = b2021[1]
    b2122 = b2122[1]
    b0405['season'] = 2006
    b0506['season'] = 2007
    b0607['season'] = 2008
    b0708['season'] = 2009
    b0809['season'] = 2010
    b0910['season'] = 2011
    b1011['season'] = 2012
    b1112['season'] = 2013
    b1213['season'] = 2014
    b1314['season'] = 2015
    b1415['season'] = 2016
    b1516['season'] = 2017
    b1617['season'] = 2018
    b1718['season'] = 2019
    b1819['season'] = 2020
    b2021['season'] = 2022
    b2122['season'] = 2023
    c0405 = c0405[1]
    c0506 = c0506[1]
    c0607 = c0607[1]
    c0708 = c0708[1]
    c0809 = c0809[1]
    c0910 = c0910[1]
    c1011 = c1011[1]
    c1112 = c1112[1]
    c1213 = c1213[1]
    c1314 = c1314[1]
    c1415 = c1415[1]
    c1516 = c1516[1]
    c1617 = c1617[1]
    c1718 = c1718[1]
    c1819 = c1819[1]
    c2021 = c2021[1]
    c2122 = c2122[1]
    c0405['season'] = 2006
    c0506['season'] = 2007
    c0607['season'] = 2008
    c0708['season'] = 2009
    c0809['season'] = 2010
    c0910['season'] = 2011
    c1011['season'] = 2012
    c1112['season'] = 2013
    c1213['season'] = 2014
    c1314['season'] = 2015
    c1415['season'] = 2016
    c1516['season'] = 2017
    c1617['season'] = 2018
    c1718['season'] = 2019
    c1819['season'] = 2020
    c2021['season'] = 2022
    c2122['season'] = 2023
    f0405 = f0405[1]
    f0506 = f0506[1]
    f0607 = f0607[1]
    f0708 = f0708[1]
    f0809 = f0809[1]
    f0910 = f0910[1]
    f1011 = f1011[1]
    f1112 = f1112[1]
    f1213 = f1213[1]
    f1314 = f1314[1]
    f1415 = f1415[1]
    f1516 = f1516[1]
    f1617 = f1617[1]
    f1718 = f1718[1]
    f1819 = f1819[1]
    f2021 = f2021[1]
    f2122 = f2122[1]
    f0405['season'] = 2006
    f0506['season'] = 2007
    f0607['season'] = 2008
    f0708['season'] = 2009
    f0809['season'] = 2010
    f0910['season'] = 2011
    f1011['season'] = 2012
    f1112['season'] = 2013
    f1213['season'] = 2014
    f1314['season'] = 2015
    f1415['season'] = 2016
    f1516['season'] = 2017
    f1617['season'] = 2018
    f1718['season'] = 2019
    f1819['season'] = 2020
    f2021['season'] = 2022
    f2122['season'] = 2023
    f0405['skater_name'] = f0405['Skater']
    f0506['skater_name'] = f0506['Skater']
    f0607['skater_name'] = f0607['Skater']
    f0708['skater_name'] = f0708['Skater']
    f0809['skater_name'] = f0809['Skater']
    f0910['skater_name'] = f0910['Skater']
    f1011['skater_name'] = f1011['Skater']
    f1112['skater_name'] = f1112['Skater']
    f1213['skater_name'] = f1213['Skater']
    f1314['skater_name'] = f1314['Skater']
    f1415['skater_name'] = f1415['Skater']
    f1516['skater_name'] = f1516['Skater']
    f1617['skater_name'] = f1617['Skater']
    f1718['skater_name'] = f1718['Skater']
    f1819['skater_name'] = f1819['Skater']
    f2021['skater_name'] = f2021['Skater']
    f2122['skater_name'] = f2122['Skater']
    f0405[['first_name','Skater']] = f0405['Skater'].loc[f0405['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0506[['first_name','Skater']] = f0506['Skater'].loc[f0506['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0607[['first_name','Skater']] = f0607['Skater'].loc[f0607['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0708[['first_name','Skater']] = f0708['Skater'].loc[f0708['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0809[['first_name','Skater']] = f0809['Skater'].loc[f0809['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0910[['first_name','Skater']] = f0910['Skater'].loc[f0910['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1011[['first_name','Skater']] = f1011['Skater'].loc[f1011['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1112[['first_name','Skater']] = f1112['Skater'].loc[f1112['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1213[['first_name','Skater']] = f1213['Skater'].loc[f1213['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1314[['first_name','Skater']] = f1314['Skater'].loc[f1314['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1415[['first_name','Skater']] = f1415['Skater'].loc[f1415['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1516[['first_name','Skater']] = f1516['Skater'].loc[f1516['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1617[['first_name','Skater']] = f1617['Skater'].loc[f1617['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1718[['first_name','Skater']] = f1718['Skater'].loc[f1718['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1819[['first_name','Skater']] = f1819['Skater'].loc[f1819['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f2021[['first_name','Skater']] = f2021['Skater'].loc[f2021['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f2122[['first_name','Skater']] = f2122['Skater'].loc[f2122['Skater'].str.split().str.len() == 2].str.split(expand=True)
    s2005 = f0405.merge(b0405,on='Skater').merge(c0405, on='Skater')
    s2006 = f0506.merge(b0506,on='Skater').merge(c0506, on='Skater')
    s2007 = f0607.merge(b0607,on='Skater').merge(c0607, on='Skater')
    s2008 = f0708.merge(b0708,on='Skater').merge(c0708, on='Skater')
    s2009 = f0809.merge(b0809,on='Skater').merge(c0809, on='Skater')
    s2010 = f0910.merge(b0910,on='Skater').merge(c0910, on='Skater')
    s2011 = f1011.merge(b1011,on='Skater').merge(c1011, on='Skater')
    s2012 = f1112.merge(b1112,on='Skater').merge(c1112, on='Skater')
    s2013 = f1213.merge(b1213,on='Skater').merge(c1213, on='Skater')
    s2014 = f1314.merge(b1314,on='Skater').merge(c1314, on='Skater')
    s2015 = f1415.merge(b1415,on='Skater').merge(c1415, on='Skater')
    s2016 = f1516.merge(b1516,on='Skater').merge(c1516, on='Skater')
    s2017 = f1617.merge(b1617,on='Skater').merge(c1617, on='Skater')
    s2018 = f1718.merge(b1718,on='Skater').merge(c1718, on='Skater')
    s2019 = f1819.merge(b1819,on='Skater').merge(c1819, on='Skater')
    s2021 = f2021.merge(b2021,on='Skater').merge(c2021, on='Skater')
    s2022 = f2122.merge(b2122,on='Skater').merge(c2122, on='Skater')
    worlds = pd.concat([s2005, s2006, s2007, s2008, s2009, s2010, s2011, s2012, s2013, s2014, 
                            s2015, s2016, s2017, s2018, s2019, s2021, s2022], axis=0)
    worlds['event'] = 'worlds'
    return worlds


def get_olympics():

    b0506 = pd.read_html('https://skatingscores.com/0506/oly/sr/women/short/quicklook/')
    b0910 = pd.read_html('https://skatingscores.com/0910/oly/sr/women/short/quicklook/')
    b1314 = pd.read_html('https://skatingscores.com/1314/oly/sr/women/short/quicklook/')
    b1718 = pd.read_html('https://skatingscores.com/1718/oly/sr/women/short/quicklook/')
    b2122 = pd.read_html('https://skatingscores.com/2122/oly/sr/women/short/quicklook/')
    c0506 = pd.read_html('https://skatingscores.com/0506/oly/sr/women/long/quicklook/')
    c0910 = pd.read_html('https://skatingscores.com/0910/oly/sr/women/long/quicklook/')
    c1314 = pd.read_html('https://skatingscores.com/1314/oly/sr/women/long/quicklook/')
    c1718 = pd.read_html('https://skatingscores.com/1718/oly/sr/women/long/quicklook/')
    c2122 = pd.read_html('https://skatingscores.com/2122/oly/sr/women/long/quicklook/')
    f0506 = pd.read_html('https://skatingscores.com/0506/oly/sr/women/results/')
    f0910 = pd.read_html('https://skatingscores.com/0910/oly/sr/women/results/')
    f1314 = pd.read_html('https://skatingscores.com/1314/oly/sr/women/results/')
    f1718 = pd.read_html('https://skatingscores.com/1718/oly/sr/women/results/')
    f2122 = pd.read_html('https://skatingscores.com/2122/oly/sr/women/results/')
    b0506 = b0506[1]
    b0910 = b0910[1]
    b1314 = b1314[1]
    b1718 = b1718[1]
    b2122 = b2122[1]
    b0506['season'] = 2006
    b0910['season'] = 2010
    b1314['season'] = 2014
    b1718['season'] = 2018
    b2122['season'] = 2022
    c0506 = c0506[1]
    c0910 = c0910[1]
    c1314 = c1314[1]
    c1718 = c1718[1]
    c2122 = c2122[1]
    c0506['season'] = 2006
    c0910['season'] = 2010
    c1314['season'] = 2014
    c1718['season'] = 2018
    c2122['season'] = 2022
    f0506 = f0506[1]
    f0910 = f0910[1]
    f1314 = f1314[1]
    f1718 = f1718[1]
    f2122 = f2122[1]
    f0506['season'] = 2006
    f0910['season'] = 2010
    f1314['season'] = 2014
    f1718['season'] = 2018
    f2122['season'] = 2022
    f0506['skater_name'] = f0506['Skater']
    f0910['skater_name'] = f0910['Skater']
    f1314['skater_name'] = f1314['Skater']
    f1718['skater_name'] = f1718['Skater']
    f2122['skater_name'] = f2122['Skater']
    f0506[['first_name','Skater']] = f0506['Skater'].loc[f0506['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f0910[['first_name','Skater']] = f0910['Skater'].loc[f0910['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1314[['first_name','Skater']] = f1314['Skater'].loc[f1314['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f1718[['first_name','Skater']] = f1718['Skater'].loc[f1718['Skater'].str.split().str.len() == 2].str.split(expand=True)
    f2122[['first_name','Skater']] = f2122['Skater'].loc[f2122['Skater'].str.split().str.len() == 2].str.split(expand=True)
    s2006 = f0506.merge(b0506,on='Skater').merge(c0506, on='Skater')
    s2010 = f0910.merge(b0910,on='Skater').merge(c0910, on='Skater')
    s2014 = f1314.merge(b1314,on='Skater').merge(c1314, on='Skater')
    s2018 = f1718.merge(b1718,on='Skater').merge(c1718, on='Skater')
    s2022 = f2122.merge(b2122,on='Skater').merge(c2122, on='Skater')
    olympics = pd.concat([s2006, s2010, s2014, 
                            s2018, s2022], axis=0)
    olympics['event'] = 'olympics'
    return olympics


def get_competition_data():
    if os.path.exists('scores.csv'):
        return pd.read_csv('scores.csv')
    olympics = get_olympics()
    worlds = get_worlds()
    gp_final = get_gp_final()
    gp_japan = get_gp_japan()
    gp_russia = get_gp_russia()
    gp_china = get_gp_china()
    gp_france = get_gp_france()
    gp_canada = get_gp_canada()
    gp_usa = get_gp_usa()
    df = pd.concat([olympics, worlds, gp_final, gp_japan, gp_russia, gp_china, gp_france, gp_canada, gp_usa], axis=0)
    df.to_csv('scores.csv', index=False)
    df = df.reset_index()

    return df