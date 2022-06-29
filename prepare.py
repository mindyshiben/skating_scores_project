import pandas as pd
import numpy as np
import requests
import os
import acquire


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
    df_oly['jump_errors_all'] = df_oly['under_rotations'] + df_oly['downgrades'] + df_oly['edge_error'] + df_oly['suspected_edge_error'] + df_oly['suspected_rotation_error'] + df_oly['combo_no_credit'] + df_oly['illegal_element'] + df_oly['event_deductions']
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
    return df_oly 