import pandas as pd
import numpy as np
import requests
import os
import acquire
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from IPython.display import Markdown, display
import textwrap

np.random.seed(123)

def prepare_competition_data(df):

    df = df.drop(columns=['QA', 'QA.1', 'QB', 'QB.1', 'PR', 'PR.1', 'Nat_x', 'Nat_y', 'season_x', 'season_y', '#_x', '#_y'])
    df['SP'] = df.SP.fillna('no_best')
    df['FS'] = df.FS.fillna('no_best')
    df['Solo Jump'] = df['Solo Jump'].fillna('3Lz')
    df['Total'] = df['Total'].fillna('no_best')
    df = df.dropna()
    df.rename(columns={'Skater':'last_name', 'SP': 'short_best', 'SP.1': 'short_score', 'SP.2': 'short_place', 'Total': 'event_best', 'Total.1': 'event_score', 'Unnamed: 0': 'event_final_place',  'Combo Jump': 'short_combo_jump', 'Solo Jump': 'short_solo_jump', 'Axel': 'short_axel_jump', 'TES_x': 'short_elements_score', 'TES.1_x': 'short_elements_rank', 'PCS_x': 'short_components_score', 'PCS.1_x': 'short_components_rank', 'TES_y': 'free_elements_score', 'TES.1_y': 'free_elements_rank', 'PCS_y': 'free_components_score', 'PCS.1_y': 'free_components_rank', 'FS': 'free_best', 'FS.1': 'free_score', 'FS.2': 'free_place', 'Nat': 'country', 'Elements': 'free_elements', 'TSS_x': 'short_overall', 'TSS_y': 'free_overall'}, inplace=True)
    df['short_best'] = df['short_best'].replace({'PB': 'skater_best', 'SB': 'skater_season_best'})
    df['free_best'] = df['free_best'].replace({'PB': 'skater_best', 'SB': 'skater_season_best'})
    olympic_skaters = df.skater_name[df.event == 'olympics'].unique()
    df['olympian'] = df.apply(lambda x: True if x.skater_name in olympic_skaters else False, axis=1)
    df_oly = df[df['olympian'] == True]
    df_oly = df_oly.replace({'<<':'@'}, regex=True)
    df_oly['free_elements'] = df_oly['free_elements'].replace({'x':'##'}, regex=True)
    df_oly['free_deductions'] = (df_oly['free_overall'].str[1:2]).astype(float)
    df_oly['short_deductions'] = (df_oly['short_overall'].str[1:2]).astype(float)
    df_oly['event_deductions'] = df_oly['short_deductions'] + df_oly['free_deductions']
    df_oly['free_elements'] = df_oly['free_elements'].replace({'q':'~'}, regex=True)
    df_oly['free_elements'] = df_oly['free_elements'].replace({'e':'$'}, regex=True)
    df_oly['short_combo_jump'] = df_oly['short_combo_jump'].replace({'e':'$'}, regex=True)
    df_oly['short_axel_jump'] = df_oly['short_axel_jump'].replace({'e':'$'}, regex=True)
    df_oly['short_solo_jump'] = df_oly['short_solo_jump'].replace({'e':'$'}, regex=True)
    df_oly['under_rotations'] = df_oly.apply(lambda x: x.str.contains("\<"), axis=1).sum(axis=1)
    df_oly['downgrades'] = df_oly.apply(lambda x: x.str.contains("\@"), axis=1).sum(axis=1)
    df_oly['edge_error'] = df_oly.apply(lambda x: x.str.contains("\$"), axis=1).sum(axis=1)
    df_oly['suspected_edge_error'] =  df_oly.apply(lambda x: x.str.contains("\!"), axis=1).sum(axis=1)
    df_oly['suspected_rotation_error'] = df_oly.apply(lambda x: x.str.contains('\~'), axis=1).sum(axis=1)
    df_oly['combo_no_credit'] =  df_oly.apply(lambda x: x.str.contains("\+COMBO"), axis=1).sum(axis=1)
    df_oly['illegal_element'] =  df_oly.apply(lambda x: x.str.contains("\*"), axis=1).sum(axis=1)
    df_oly['under_rotations'] = df_oly['under_rotations'].astype(float)
    df_oly['downgrades'] = df_oly['downgrades'].astype(float)
    df_oly['edge_error'] = df_oly['edge_error'].astype(float)
    df_oly['suspected_edge_error'] =  df_oly['suspected_edge_error'].astype(float)
    df_oly['suspected_rotation_error'] = df_oly['suspected_rotation_error'].astype(float)
    df_oly['combo_no_credit'] =  df_oly['combo_no_credit'].astype(float)
    df_oly['illegal_element'] =  df_oly['illegal_element'].astype(float)
    df_oly['event_deductions'] = df_oly['event_deductions'].astype(float)
    df_oly['jump_errors_all'] = df_oly['under_rotations'] + df_oly['downgrades'] + df_oly['edge_error'] + + df_oly['combo_no_credit'] + df_oly['illegal_element'] + df_oly['event_deductions']
    df_oly['jump_errors_costly'] = df_oly['downgrades'] + df_oly['combo_no_credit'] + df_oly['event_deductions']
    df_oly['country_flag'] = df_oly['country']
    df_oly['country'] = df_oly.country_flag.replace({'🇯🇵': 'japan', '🇺🇸': 'usa', '🇷🇺': 'russia', '🇨🇦': 'canada',
                                           '🇰🇷': 'south_korea', '🇮🇹': 'italy', '🇨🇳': 'china',
                                            '🇫🇮': 'finland', '🇭🇺': 'hungary', '🇬🇪': 'georgia',
                                            '🇩🇪': 'germany', '🇨🇭':'switzerland', '🇫🇷':'france',
                                            '🇦🇺': 'australia', '🇪🇪': 'estonia', '🇰🇿':'kazakhstan',
                                            '🇺🇦': 'ukraine', '🇺🇿': 'uzbekistan', '🇸🇰': 'slovakia',
                                            '🇭🇷': 'croatia', '🇹🇷': 'turkey', '🇦🇿': 'azerbaijan',
                                            '🇧🇪': 'belgium', '🇨🇿':'czech_republic', '🇪🇸': 'spain',
                                            '🇵🇱': 'poland', '🇦🇹': 'austria', '🇧🇾': 'belarus',
                                            '🇧🇬': 'bulgaria', '🇧🇷': 'brazil', '🇱🇺': 'luxembourg'})
    df = pd.DataFrame(df_oly)
    df['event_score'] = df.event_score.astype(float)
    df['triple_triple'] = df.apply(lambda x: x.str.contains("3S+3") | x.str.contains("3T+3") | x.str.contains("3Lo+3") | x.str.contains("3F+3") | x.str.contains("3Lz+3"), axis=1).sum(axis=1)
    df['quad'] = df.apply(lambda x: x.str.contains("4S") | x.str.contains("4T") | x.str.contains("4Lo") | x.str.contains("4F") | x.str.contains("4Lz"), axis=1).sum(axis=1)
    df['triple_axel'] = df.apply(lambda x: x.str.contains("3A"), axis=1).sum(axis=1)
    df = df.drop(columns=['last_name', 'country_flag', 'short_best', 'olympian', 'free_best', 'event_best', 'first_name', 'short_combo_jump', 'short_solo_jump', 'short_axel_jump'])
    df['season'] = df.season.astype('object')
    df2006 = pd.DataFrame(df[(df.season <= 2006)].where(df.event != 'olympics'))
    o2006 = pd.DataFrame(df[df.season == 2006].where(df.event == 'olympics'))
    df2010 = pd.DataFrame(df[(df.season <= 2010) & (df.season > 2006)].where(df.event != 'olympics'))
    o2010 = pd.DataFrame(df[df.season == 2010].where(df.event == 'olympics'))
    df2014 = pd.DataFrame(df[(df.season <= 2014) & (df.season > 2010)].where(df.event != 'olympics'))
    o2014 = pd.DataFrame(df[df.season == 2014].where(df.event == 'olympics'))
    df2018 = pd.DataFrame(df[(df.season <= 2018) & (df.season > 2014)].where(df.event != 'olympics'))
    o2018 = pd.DataFrame(df[df.season == 2018].where(df.event == 'olympics'))
    df2022 = pd.DataFrame(df[(df.season <= 2022) & (df.season > 2018)].where(df.event != 'olympics'))
    o2022 = pd.DataFrame(df[df.season == 2022].where(df.event == 'olympics'))
    df2006 = df2006.dropna()
    o2006 = o2006.dropna()
    df2010 = df2010.dropna()
    o2010 = o2010.dropna()
    df2014 = df2014.dropna()
    o2014 = o2014.dropna()
    df2018 = df2018.dropna()
    o2018 = o2018.dropna()
    df2022 = df2022.dropna()
    o2022 = o2022.dropna()
    o2006 = o2006[['skater_name', 'country', 'event_final_place', 'short_score', 'short_elements_score', 'short_components_score', 'free_elements_score', 'free_components_score', 'free_score', 'event_score', 'season']]
    o2010 = o2010[['skater_name', 'country', 'event_final_place', 'short_score', 'short_elements_score', 'short_components_score', 'free_elements_score', 'free_components_score', 'free_score', 'event_score', 'season']]
    o2014 = o2014[['skater_name', 'country', 'event_final_place', 'short_score', 'short_elements_score', 'short_components_score', 'free_elements_score', 'free_components_score', 'free_score', 'event_score', 'season']]
    o2018 = o2018[['skater_name', 'country', 'event_final_place', 'short_score', 'short_elements_score', 'short_components_score', 'free_elements_score', 'free_components_score', 'free_score', 'event_score', 'season']]
    o2022 = o2022[['skater_name', 'country', 'event_final_place', 'short_score', 'short_elements_score', 'short_components_score', 'free_elements_score', 'free_components_score', 'free_score', 'event_score', 'season']]
    o2006 = o2006.rename(columns={'event_final_place': 'oly_event_final_place', 'short_score': 'oly_short_score', 'short_elements_score': 'oly_short_elements_score', 'short_components_score': 'oly_short_components_score', 'free_elements_score': 'oly_free_elements_score', 'free_components_score': 'oly_free_components_score', 'free_score': 'oly_free_score', 'event_score':'oly_event_score'})
    o2010 = o2010.rename(columns={'event_final_place': 'oly_event_final_place', 'short_score': 'oly_short_score', 'short_elements_score': 'oly_short_elements_score', 'short_components_score': 'oly_short_components_score', 'free_elements_score': 'oly_free_elements_score', 'free_components_score': 'oly_free_components_score', 'free_score': 'oly_free_score', 'event_score':'oly_event_score'})
    o2014 = o2014.rename(columns={'event_final_place': 'oly_event_final_place', 'short_score': 'oly_short_score', 'short_elements_score': 'oly_short_elements_score', 'short_components_score': 'oly_short_components_score', 'free_elements_score': 'oly_free_elements_score', 'free_components_score': 'oly_free_components_score', 'free_score': 'oly_free_score', 'event_score':'oly_event_score'})
    o2018 = o2018.rename(columns={'event_final_place': 'oly_event_final_place', 'short_score': 'oly_short_score', 'short_elements_score': 'oly_short_elements_score', 'short_components_score': 'oly_short_components_score', 'free_elements_score': 'oly_free_elements_score', 'free_components_score': 'oly_free_components_score', 'free_score': 'oly_free_score', 'event_score':'oly_event_score'})
    o2022 = o2022.rename(columns={'event_final_place': 'oly_event_final_place', 'short_score': 'oly_short_score', 'short_elements_score': 'oly_short_elements_score', 'short_components_score': 'oly_short_components_score', 'free_elements_score': 'oly_free_elements_score', 'free_components_score': 'oly_free_components_score', 'free_score': 'oly_free_score', 'event_score':'oly_event_score'})
    df2006 = df2006.groupby(df2006.skater_name).mean()
    df2010 = df2010.groupby(df2010.skater_name).mean()
    df2014 = df2014.groupby(df2014.skater_name).mean()
    df2018 = df2018.groupby(df2018.skater_name).mean()
    df2022 = df2022.groupby(df2022.skater_name).mean()
    df06 = df2006.merge(o2006, on='skater_name')
    df10 = df2010.merge(o2010, on='skater_name')
    df14 = df2014.merge(o2014, on='skater_name')
    df18 = df2018.merge(o2018, on='skater_name')
    df22 = df2022.merge(o2022, on='skater_name')
    df = pd.concat([df06, df10, df14, df18, df22], axis=0)
    df['season'] = df.season.astype(int)
    df['short_place'] = df['short_place'].round()
    df['free_place'] = df['free_place'].round()

    return df

def printmd(string):
    display(Markdown(string))

def split_data(df):

    train, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train, test_size=.3, random_state=123)

    printmd('**number of train records: {:}**'.format(len(train)))
    printmd('**number of validate records: {:}**'.format(len(validate)))
    printmd('**number of test records: {:}**'.format(len(test)))
    return train, validate, test

