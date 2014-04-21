__author__ = 'dungdt'

import re
from collections import Counter

punctuationPattern  = re.compile(r'[\"\'\!\$%\^\&\*\(\)\`\~\?\/\{\}\[\]\|\:\;\.\,]+')
tokenizePattern     = re.compile(r'[\w#@]+')
categories          = {
    'agriculture': ['barley', 'castorseed', 'cocoa', 'coconut', 'coffee', 'corn', 'cotton',
                    'oat', 'oilseed', 'orange', 'palmkernel', 'potato', 'rapeseed', 'red-bean',
                    'rice', 'rubber', 'rye', 'sorghum', 'soy-oil', 'soybean', 'sunseed', 'tea',
                    'wheat', 'grain', 'groundnut', 'lei', 'linseed', ],
    'business': ['cpi', 'dfl', 'dkr', 'dlr', 'bop', 'cpu', 'crude', 'naphtha', 'rand',
                 'reserves', 'retail', 'ringgit', 'stg', 'trade', 'wpi', 'gnp', 'inventories',
                 'ipi', 'lead', 'lit', 'acq', 'ship', 'hog', ],
    'industry': ['castor-oil', 'citruspulp', 'coconut-oil', 'copra-cake', 'corn-oil',
                 'cornglutenfeed', 'cotton-oil', 'palm-oil', 'rape-meal', 'rape-oil', 'soy-meal',
                 'sugar', 'sun-meal', 'sun-oil', 'tapioca', 'veg-oil', 'wool', 'groundnut-oil',
                 'lin-meal', 'lin-oil', 'lumber', 'meal-feed', 'fuel', 'nat-gas', 'heat',
                 'jet', 'gas', 'pet-chem', 'plywood', 'propane', 'alum', 'palladium', 'platinum',
                 'silver', 'strategic-metal', 'zinc', 'gold', 'iron-steel', 'fishmeal', ],
    # 'life': ['carcass',  'pork-belly',  'housing',  'interest',  'jobs',  'l-cattle', ],
    'money': ['saudriyal', 'can', 'copper', 'cruzado', 'dmk', 'nickel', 'nkr', 'nzdlr', 'peseta',
              'rupiah', 'skr', 'tin', 'yen', 'money-fx', 'austdlr', 'earn', 'money-supply',
              'income', 'instal-debt', 'livestock', ],
    # 'politics': ['ship', 'hog',],
}



# Return the list of terms
def tokenize(text):
    terms = Counter()
    text = punctuationPattern.sub(' ', text.lower())
    matches = tokenizePattern.findall(text)

    for term in matches:
        if len(term) > 2:
            terms[term] += 1

    return terms


def extractLabel(filePath):
    rawCategory = filePath.split('/')[-2].lower()

    for category, rawCategories in categories.items():
        if rawCategory in rawCategories:
            return category

    return None