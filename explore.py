import pandas as pd
import acquire
import prepare
import numpy as np
from IPython.display import Markdown, display
from IPython.core import display as ICD
import seaborn as sns
import matplotlib.pyplot as plt
import textwrap

def printmd(string):
    display(Markdown(string))

def scores_season(train):

    df1 = train.groupby(train.season)['short_score', 'short_elements_score', 'short_components_score', 'free_score',  'free_elements_score', 'free_components_score', 'event_score'].mean().round(2)
    df2 = train.where(train.top == 'usa').groupby(train.season)['short_score', 'short_elements_score', 'short_components_score', 'free_score',  'free_elements_score', 'free_components_score', 'event_score'].mean().round(2)
    df3 = train.where(train.top == 'top').groupby(train.season)['short_score', 'short_elements_score', 'short_components_score', 'free_score',  'free_elements_score', 'free_components_score', 'event_score'].mean().round(2)
    df4 = train.where((train.top == 'top') & (train.country != 'russia')).groupby(train.season)['short_score', 'short_elements_score', 'short_components_score', 'free_score',  'free_elements_score', 'free_components_score', 'event_score'].mean().round(2)
    df5 = train.where(train.top == 'other').groupby(train.season)['short_score', 'short_elements_score', 'short_components_score', 'free_score',  'free_elements_score', 'free_components_score', 'event_score'].mean().round(2)
    
    printmd('**Mean Event Scores by Season**')
    ICD.display(df1)
    print('')
    printmd('**Mean USA Event Scores by Season**')
    ICD.display(df2)
    print('')
    printmd('**Mean Event Scores by Season -  Top Performing Countries**')
    ICD.display(df3)
    print('')
    printmd('**Mean Event Scores by Season -  Top Performing Countries (excluding Russia)**')
    ICD.display(df4)
    print('')
    printmd('**Mean Event Scores by Season - Other Countries**')
    ICD.display(df5)


def top_score(country):
  if country == 'usa':
    return "usa"
  elif (country == 'canada') | (country == 'russia') | (country == 'japan') | (country == 'south_korea') | (country == 'italy'):
    return 'top'
  else:
    return 'other'

def usa_score(country):
  if country == 'usa':
    return "usa"
  else:
    return 'other'


def plot_scores(train):

    plt.rcParams["figure.figsize"] = (12,3)
    fontsize = 30
    ax1 = (train.where((train.season == 2006) | (train.season == 2022)).groupby(['season','usa']).mean()['oly_event_score'].unstack().plot(kind='barh', fontsize= fontsize))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Olympics Final Score', size = 12)
    plt.ylabel('Season', size = 12)
    plt.title('Average Olympic Final Score- USA vs. Other Countries ', size = 20)
    plt.show()
    printmd('**Chart Anaylsis:**')
    s1 = ("On average, final scores at the Olympic games have increased from 2006 to 2022, however the average increase for non-USA athletes is substantially greater than that of USA athletes. The difference in increase is so great that USA althetes as a whole clearly outscored all other athletes in 2006, but in 2022, the mean score of all other athletes exceeds the mean score of US athletes.  The following graphs are set in this same format, but examine scores from events preceding the Olympics for the purpose of analyzing where USA skaters may be lacking.")
    print('\n'.join(textwrap.wrap(s1, width=80, replace_whitespace=False)))
    print('')
    print('-----------------------------------------------------------------------')
    print('')
    print('')

    ax2 = (train.where((train.season == 2006) | (train.season == 2022)).groupby(['season','usa']).mean()['event_score'].unstack().plot(kind='barh'))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Events- Final Score' , size = 12)
    plt.ylabel('Season', size = 12)
    plt.title('Other Events Final Score (Avg) - USA vs. Other Countries', size = 20)
    plt.show()
    printmd('**Chart Anaylsis:**')
    s2 = ("When looking at major international competitions preceeding the Olympics, we see a very similar pattern for USA athlete scores compared to all other athlete scores. Additionally, when comparing this chart to the Olympic Scores chart, we can see that non_USA athletes have had their best scores at the Olympics in 2022 whereas USA athletes had worse scores at the 2022 Olympics when compared to prior event averages in this chart. Interestingly, this is only the case in 2022 and in 2006, both USA and non-USA athletes tending to score very similarly in the Olympics to the events preceding the Olympics.")
    print('\n'.join(textwrap.wrap(s2, width=80, replace_whitespace=False)))
    print('')
    print('-----------------------------------------------------------------------')
    print('')
    print('')

    ax3 = (train.where((train.season == 2006) | (train.season == 2022)).groupby(['season','usa']).mean()['short_score'].unstack().plot(kind='barh'))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Short Program- Final Score' , size = 12)
    plt.ylabel('Season', size = 12)
    plt.title('Short Program Score (Avg) - USA vs. Other Countries', size = 20)
    plt.show()
    printmd('**Chart Anaylsis:**')
    s3 = ("The average total short program scores of USA athletes have increased from 2006-2022 very similiarly to the increase of average short program scores of non-USA athletes, but it does look like non-USA athletes have still had a slightly higher increase. In this category, the USA athletes outscored non-USA athletes in both 2006 and 2022, but non-USA athletes are not as far behind USA athletes in 2022 as they were in 2006.")
    print('\n'.join(textwrap.wrap(s3, width=80, replace_whitespace=False)))
    print('')
    print('-----------------------------------------------------------------------')
    print('')
    print('')

    ax4 = (train.where((train.season == 2006) | (train.season == 2022)).groupby(['season','usa']).mean()['short_elements_score'].unstack().plot(kind='barh'))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Short Program Elements Score' , size = 12)
    plt.ylabel('Season', size = 12)
    plt.title('Short Program Elements Score (Avg) - USA vs. Other Countries', size = 20)
    plt.show()
    printmd('**Chart Anaylsis:**')
    s4 = ("While USA athletes were ahead of non-USA athletes in the total short program score in 2006 and 2022, non-USA athletes outscored USA athletes in the elements portion of the short program score in 2022. This shows that USA athletes are really falling behind in this category")
    print('\n'.join(textwrap.wrap(s4, width=80, replace_whitespace=False)))
    print('')
    print('-----------------------------------------------------------------------')
    print('')
    print('')

    ax5 = (train.where((train.season == 2006) | (train.season == 2022)).groupby(['season','usa']).mean()['short_components_score'].unstack().plot(kind='barh'))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Short Program Components Score' , size = 12)
    plt.ylabel('Season', size = 12)
    plt.title('Short Program Components Score (Avg) - USA vs. Other Countries', size = 20)
    plt.show()
    printmd('**Chart Anaylsis:**')
    s5 = ("The components portion of the short program score increases look very similar to the total short program scores. The USA athletes were ahead in 2006 and 2022, but the margin between USA and non-USA athletes has decreased and if this trend continues, non-USA athletes would eventually outscore USA athletes in this category as they have done in the elements score of the short program.")
    print('\n'.join(textwrap.wrap(s5, width=80, replace_whitespace=False)))
    print('')
    print('-----------------------------------------------------------------------')
    print('')
    print('')

    ax6 = (train.where((train.season == 2006) | (train.season == 2022)).groupby(['season','usa']).mean()['free_score'].unstack().plot(kind='barh'))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Free Program- Final Score' , size = 12)
    plt.ylabel('Season', size = 12)
    plt.title('Free Program Score (Avg) - USA vs. Other Countries', size = 20)
    plt.show()
    printmd('**Chart Anaylsis:**')
    s6 = ("Non-USA athletes have increased the total free program score by a much higher percentage that USA athletes. USA athletes were clearly ahead in free program scores in 2006 and in 2022, non-USA athletes have surpasses USA athletes in this category. As the athletes typically earn around twice as many points in the free program compared to the short program, the free program score is about twice as important for the overall event score. The USA athletes falling behind in this category may be very costly to event outcomes.")
    print('\n'.join(textwrap.wrap(s6, width=80, replace_whitespace=False)))
    print('')
    print('-----------------------------------------------------------------------')
    print('')
    print('')

    ax7 = (train.where((train.season == 2006) | (train.season == 2022)).groupby(['season','usa']).mean()['free_elements_score'].unstack().plot(kind='barh'))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Free Program Elements Score' , size = 12)
    plt.ylabel('Season', size = 12)
    plt.title('Free Program Elements Score (Avg) - USA vs. Other Countries', size = 20)
    plt.show()
    printmd('**Chart Anaylsis:**')
    s7 = ("The elements portion of the free program score appears to be the most problematic for USA athletes. On average, USA athletes increased the free program elements score by aapproximately 10 points whereas non-USA athletes have increased their free program elements score by over 20 points. Non-USA athletes were behind USA athletes in this category in 2006, but in 2022, non-USA athletes undoubtable surpassed USA athletes by a significant margin. This category is likely the most influential factor contributing to lower competition scores for USA athletes.")
    print('\n'.join(textwrap.wrap(s7, width=80, replace_whitespace=False)))
    print('')
    print('-----------------------------------------------------------------------')
    print('')
    print('')

    ax8 = (train.where((train.season == 2006) | (train.season == 2022)).groupby(['season','usa']).mean()['free_components_score'].unstack().plot(kind='barh'))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Free Program Components Score' , size = 12)
    plt.ylabel('Season', size = 12)
    plt.title('Free Program Components Score (Avg) - USA vs. Other Countries', size = 20)
    plt.show()
    printmd('**Chart Anaylsis:**')
    s8 = ("Interestingly, the USA athletes have still outscored non-USA athletes in the program components portion of the free program score in 2022. This even further demonstrates how costly low free program element scores are for US athletes")
    print('\n'.join(textwrap.wrap(s8, width=80, replace_whitespace=False)))
    print('')
    print('-----------------------------------------------------------------------')
    print('')
    print('')
