from metrics import *



def init_dict_multiwords_expression(corpuspath):
    #open the file
    with open(corpuspath, 'r') as corpus:
        #read the file line by line
        for line in corpus:
            #split the line into words
            words = line.split()
            #create a list of ngrams and get all the ngrams lenght 2 to 8
            for i in range(1,9):
                bysize = {}
                for j in range(len(words)-i+1):
                    ngram = ' '.join(words[j:j+i])
                    #if the ngram is not in the dictioionary, add it
                    if ngram not in bysize:
                        bysize[ngram]={}
                        bysize[ngram]["freq"] = 1
                        bysize[ngram]["SCP"] = 0
                        bysize[ngram]["MaxOmegaPlusSCP"] = 0
                        bysize[ngram]["MaxOmegaMinusSCP"] = 0
                        bysize[ngram]["Dice"]=0
                        bysize[ngram]["MaxOmegaPlusDice"] = 0
                        bysize[ngram]["MaxOmegaMinusDice"] = 0
                    else:
                        #increment the ngram freq value
                        bysize[ngram]["freq"] += 1
                ngrams[i] = bysize
    
def fill_dict_multiwords_expression():
    for i in range(8,1,-1):
        print("size of n_grams: ",i)
        for ngram, value in ngrams[i].items():
            calculSCP(ngram,value)
            calculDice(ngram,value)
            first_multiword_expression = ngram.split()[0:i-1]
            first_multiword_expression = ' '.join(first_multiword_expression)
            if(ngrams[i-1][first_multiword_expression]["SCP"] == 0):
                calculSCP(first_multiword_expression, ngrams[i-1][first_multiword_expression])
            if(ngrams[i-1][first_multiword_expression]["Dice"] == 0):
                calculDice(first_multiword_expression, ngrams[i-1][first_multiword_expression])
            second_multiword_expression = ngram.split()[1:i]
            second_multiword_expression = ' '.join(second_multiword_expression)
            if(ngrams[i-1][second_multiword_expression]["SCP"] == 0):
                calculSCP(second_multiword_expression, ngrams[i-1][second_multiword_expression])
            if(ngrams[i-1][second_multiword_expression]["Dice"] == 0):
                calculDice(second_multiword_expression, ngrams[i-1][second_multiword_expression])
            if(i!=2):
                ngrams[i-1][first_multiword_expression]["MaxOmegaPlusSCP"] = max(ngrams[i-1][first_multiword_expression]["MaxOmegaPlusSCP"],ngrams[i][ngram]["SCP"])
                ngrams[i-1][second_multiword_expression]["MaxOmegaPlusSCP"] = max(ngrams[i-1][second_multiword_expression]["MaxOmegaPlusSCP"],ngrams[i][ngram]["SCP"])
                ngrams[i-1][first_multiword_expression]["MaxOmegaPlusDice"] = max(ngrams[i-1][first_multiword_expression]["MaxOmegaPlusDice"],ngrams[i][ngram]["Dice"])
                ngrams[i-1][second_multiword_expression]["MaxOmegaPlusDice"] = max(ngrams[i-1][second_multiword_expression]["MaxOmegaPlusDice"],ngrams[i][ngram]["Dice"])
            if(i!=8):
                ngrams[i][ngram]["MaxOmegaMinusSCP"] = max(ngrams[i-1][first_multiword_expression]["SCP"],ngrams[i-1][second_multiword_expression]["SCP"])
                ngrams[i][ngram]["MaxOmegaMinusDice"] = max(ngrams[i-1][first_multiword_expression]["Dice"],ngrams[i-1][second_multiword_expression]["Dice"])

