import math

repoStarCount = 30 # how many star does your repo have on GitHub, 30 is example
repoDaysCreated = 500 # days passed after your repo has been created on GitHub, 500 is example
repoInsertedLines = 1000 # how many lines of code has been added by you on your repo on GitHub, 1000 is example

repoSignificanceFactor = 3 ** math.log(repoStarCount+1,10)
repoAgingFactor = math.e ** (-repoDaysCreated/1095)
repoSlocFactor = 2 ** math.log(repoInsertedLines+1,1000)
gitHubScore = repoSignificanceFactor * repoAgingFactor * repoSlocFactor

stackOverFlowScore = 10 # stackoverflow score coming directly from StackOverFlow API

totalScore = gitHubScore + stackOverFlowScore