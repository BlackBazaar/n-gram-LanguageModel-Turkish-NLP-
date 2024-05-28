def n_gram_text(text, n):
    textDicts = {}
    for i in range(len(text) - (n - 1)):
        ngram = text[i:i + n]
        if " " not in ngram:
            if ngram in textDicts:
                textDicts[ngram] += 1
            else:
                textDicts[ngram] = 1
    #for k,v in textDicts.items():
        #print(k,":",v)

    return textDicts

def n_gram_Text_possibility(text_dict,n_gramposb):
    n_Text_gramposb = {}
    for key in text_dict.keys():
        if key not in n_gramposb:
            n_Text_gramposb[key] = 0
        else:
            n_Text_gramposb[key] = n_gramposb[key] 

    return n_Text_gramposb

def n_gram_parse(filename,n):
    file = open(filename ,"r",encoding='utf-8').read().split("\n")
    n_gram_2list = []
    n_gramdict = {}

    for word in file:
        for i in range(0,len(word)-n+1):
            last = word[i:i+n]
            if " " not in last:
                n_gram_2list.append(last)
            else:
                i+= 1
                
    for j in range(0,len(n_gram_2list)):
        if n_gram_2list[j] in n_gramdict:
            n_gramdict[n_gram_2list[j]] += 1
        else:
            n_gramdict[n_gram_2list[j]] = 1
    return n_gramdict

def n_gram_possibility(n_gramdict):
    n_gramposb = {}
    length = 0
    for value in n_gramdict.values():
        length += value
    for key in n_gramdict.keys():
        n_gramposb[key] = n_gramdict[key] / length
    return n_gramposb
    
def detect_swear(n_gramposb,text,n,threshold):
    text_wordlist = []
    swear_word_list = []
    for word in text.split():
        text_wordlist.append(word)

    for word in text_wordlist:
        total_possb = 0
        text_dict = n_gram_text(word.lower(), n)
        text_possibilityDict = n_gram_Text_possibility(text_dict,n_gramposb)

        for swear_word_posib in text_possibilityDict.values():
            total_possb += swear_word_posib

        percentage = int((total_possb/0.1)*100)
        print(word," --> %" + str(percentage))

        if total_possb > threshold:
            swear_word_list.append(word)

    return swear_word_list

#def calculate_threshold(n_gramposb, percentile=95):
    # Get the list of probabilities
    #probabilities = list(n_gramposb.values())

    # Sort probabilities in descending order
    #sorted_probs = sorted(probabilities, reverse=True)

    # Find the threshold value based on percentile
    #threshold_index = int(len(sorted_probs) * (percentile / 100))
    #threshold_value = sorted_probs[threshold_index]

    #return 0

def main():
    n = 3
    n_gramdict = n_gram_parse("kufurlist.txt",n)
    
    n_gramposb = n_gram_possibility(n_gramdict)
    #text = "Merhaba senin amınakoyarım orospu çocuğu kendine gel yarramı senin kafana sürterim anneni sikerim senin kafasızorospuçocu yarramın dölü skerim seni rrospu"
    text = "Merhaba güzel insan sen iyiki varsın bugün çok daha güzel giyinmişsin kıyafetini nerden aldın ve bu kadar güzel bir insan olmayı kime borçlusun boktan bir insansın"
    #text = "Merhaba amk"
    #threshold = calculate_threshold(n_gramdict) 
    threshold = 0.017
    swear_word_list = detect_swear(n_gramposb,text,n,threshold)
    
    print("Cümledeki küfürlerin listesi -->",swear_word_list)

    threshold_percentage = int((threshold/0.1)*100)
    print("threshold percentage --> %" + str(threshold_percentage))


main()    