import json
import numpy as np
from textblob import TextBlob
from scipy.stats.stats import pearsonr
reviewData = open("yelp_academic_dataset_review.json", "r").readlines()

businessInfo = {}    # Make an empty dictionary
for d in reviewData[0:20]:
  parsed = json.loads(d)
  business = parsed["business_id"]
  score = parsed["stars"]
  text = parsed["text"]
  tb = TextBlob(text)
  polarity = tb.sentiment.polarity
  correlation = pearsonr()
  businessData = businessInfo.get(business, [])  # Get the list of scores and polarities out of businessInfo. If there's no entry for that business yet, get an empty list.
  businessData.append((score, polarity,))         # Append a tuple to businessData. businessData is always a list of tuples where the first value is the score and the second value is the polarity.
  businessInfo[business] = businessData

for key, value in businessInfo.items():
    print (key, value)

businessCorrelations = {}      # Make an empty dictionary that will be a business (key) vs correlation (value) dictionary
scores = []
polarities = []
for business, scoreAndPolarity in businessInfo.iteritems():      # Iterates over all the items in the dictionary using the form "key, value".
  for x in range(len(scoreAndPolarity)):
  	scores.append((scoreAndPolarity[x])[0])
  	polarities.append((scoreAndPolarity[x])[1])
  correlation = pearsonr(scores, polarities)
#  businessCorrelations.append((business, correlation,)) # If we had made businessCorrelations a list instead, this would have made tuples of business and correlations
  businessCorrelations[business] = correlation

# show business with associated correlation
for business, correlations in businessCorrelations.iteritems():
  print (business, correlations) 
