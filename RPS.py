keys = ['RPS','PRS','SRP','RSP','PSR','SPR','RRS','RSR','SRR','RRP','RPR','PRR',
'RSS','SRS','SSR','PSS','SPS','SSP','PPR','PRP','RPP','PPS','PSP','SPP',
'RRR','PPP','SSS']

dictionary = { 'RPS' : [1/3,1/3,1/3],
'PRS':[1/3,1/3,1/3],
'SRP':[1/3,1/3,1/3],
'RSP':[1/3,1/3,1/3],
'PSR':[1/3,1/3,1/3],
'SPR':[1/3,1/3,1/3],
'RRS':[1/3,1/3,1/3],
'RSR':[1/3,1/3,1/3],
'SRR':[1/3,1/3,1/3],
'RRP':[1/3,1/3,1/3],
'RPR':[1/3,1/3,1/3],
'PRR':[1/3,1/3,1/3],
'RSS':[1/3,1/3,1/3],
'SRS':[1/3,1/3,1/3],
'SSR':[1/3,1/3,1/3],
'PSS':[1/3,1/3,1/3],
'SPS':[1/3,1/3,1/3],
'SSP':[1/3,1/3,1/3],
'PPR':[1/3,1/3,1/3],
'PRP':[1/3,1/3,1/3],
'RPP':[1/3,1/3,1/3],
'PPS':[1/3,1/3,1/3],
'PSP':[1/3,1/3,1/3],
'SPP':[1/3,1/3,1/3],
'RRR':[1/3,1/3,1/3],
'PPP':[1/3,1/3,1/3],
'SSS':[1/3,1/3,1/3],
}
matrix = [
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],
  [1/3,1/3,1/3],]





def player(prev_play, opponent_history=[]):

    opponent_history.append(prev_play)# add last move

    if(len(opponent_history) <= 3): # before we have enough data
      return 'R' # can be anything

    a = countNextMoves(opponent_history) 
    # count all possible next moves from this possition


    countR=0
    countP=0
    countS=0

    for x in a[0]:
      if(x == 'R'): countR+=1
      elif(x =='P'): countP+=1
      else: countS+=1

    
    if (countR >= countS) and (countR >= countP): 
        return 'P' # return paper if we have a lot of rocks
  
    elif (countP >= countR) and (countP >= countS): 
        return 'S' # return scissors if we have a lot of paper
    else: 
        return 'R' # return rock if we have a lot of scissors


def countNextMoves(opponent_history):
  first = opponent_history[-3]
  second = opponent_history[-2]
  third = opponent_history[-1]

  string = first+second+third

  allMoves = ""
  for x in opponent_history:
    allMoves += x

# we use KMP for pattern recognition
# we will find all recurrances of last THREE played 
# symbols and try to predict the next one
  listOfIndexes= KMPSearch(string, allMoves)

  listOfNextMoves = []
  for index in listOfIndexes:
    if (index+len(string)) <= len(allMoves)-1:
      next = allMoves[index+len(string)]
      listOfNextMoves.append(next)

  return [listOfNextMoves,string]
  # we return list of next moves
  # string is useless now, I'll try to implement that later




# Knuth-Morris-Pratt algoritm
# returns list of indexes of patterns
def KMPSearch(pat, txt): 
	M = len(pat)
	listOfIndexes = []
	N = len(txt) 

	 
	lps = [0]*M 
	j = 0 


	computeLPSArray(pat, M, lps) 

	i = 0 
	while i < N: 
		if pat[j] == txt[i]: 
			i += 1
			j += 1

		if j == M: 
			listOfIndexes.append(i-j)
			j = lps[j-1] 

		 
		elif i < N and pat[j] != txt[i]: 
			
			if j != 0: 
				j = lps[j-1] 
			else: 
				i += 1
	return listOfIndexes



def computeLPSArray(pat, M, lps): 
	len = 0  

	lps[0] 
	i = 1

	
	while i < M: 
		if pat[i]== pat[len]: 
			len += 1
			lps[i] = len
			i += 1
		else: 
			
			if len != 0: 
				len = lps[len-1] 

			 
			else: 
				lps[i] = 0
				i += 1

