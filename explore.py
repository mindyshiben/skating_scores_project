def map_score(country):
        if country == 'usa':
            return "usa"
        elif (country == 'canada') | (country == 'russia') | (country == 'japan') | (country == 'south_korea') | (country == 'italy'):
            return 'top'
        else:
            return 'other'

train["top"] = train["country"].apply(lambda country: map_score(country))