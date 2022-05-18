import sys
import nltk
import math
import numpy
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import bigrams

def calcolaTokensTesto(sentences_list):
    tokensTOT = []
    for sentence in sentences_list:
        tokens = word_tokenize(sentence)
        tokensTOT += tokens
    return tokensTOT

def calcolaTokensPOS(sentences_list):
    posTOT = []
    for sentence in sentences_list:
        tokens = word_tokenize(sentence)
        pos = nltk.pos_tag(tokens)
        posTOT+=pos
    return posTOT

def most_commonPOS(tokensPOS_list, tokens_list, testo):
    distribuzioneFreq = nltk.FreqDist(tokensPOS_list)
    commonPOS10 = distribuzioneFreq.most_common(10)
    print("le 10 POS più frequenti di", testo)
    print(commonPOS10)
    print()
    namesPOS_list = []
    verbsPOS_list = []
    for bigramma in tokensPOS_list:
        if(bigramma[1] in ["NN", "NNS", "NNP", "NNPS"]):
            namesPOS_list.append(bigramma)
        if(bigramma[1] in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]):
            verbsPOS_list.append(bigramma)
    distribuzioneFreqNames = nltk.FreqDist(namesPOS_list)
    distribuzioneFreqVerbs = nltk.FreqDist(verbsPOS_list)
    commonNames20 = distribuzioneFreqNames.most_common(20)
    print("i 20 sostantivi più frequenti di", testo)
    print(commonNames20)
    print()
    commonVerbs20 = distribuzioneFreqVerbs.most_common(20)
    print("i 20 verbi più frequenti di", testo)
    print(commonVerbs20)
    print()
    bigrams_list = list(bigrams(tokens_list))
    bigramsOrd_list = []
    namesPOSord_list = []
    for bigramma in namesPOS_list:
        namesPOSord_list.append(bigramma[0])
    verbsPOSord_list = []
    for bigramma in  verbsPOS_list:
        verbsPOSord_list.append(bigramma[0])
    for bigramma in bigrams_list:
        if((bigramma[0] in namesPOSord_list) and (bigramma[1] in verbsPOSord_list)):
            bigramsOrd_list.append(bigramma)
    distribuzioneFreqBigrammi1 = nltk.FreqDist(bigramsOrd_list)
    commonBigrammi1 = distribuzioneFreqBigrammi1.most_common(20)
    print("i 20 bigrammi composti da un Sostantivo seguito da un Verbo più frequenti di", testo)
    print(commonBigrammi1)
    print()
    adjective_list = []
    for bigramma in tokensPOS_list:
        if(bigramma[1] in ["JJ", "JJR", "JJS"]):
            adjective_list.append(bigramma[0])
    bigramsOrd_list2 = []
    for bigramma in bigrams_list:
        if((bigramma[0] in adjective_list) and (bigramma[1] in namesPOSord_list)):
            bigramsOrd_list2.append(bigramma)
    distribuzioneFreqBigrammi2 = nltk.FreqDist(bigramsOrd_list2)
    commonBigrammi2 = distribuzioneFreqBigrammi2.most_common(20)
    print("i 20 bigrammi composti da un Aggettivo seguito da un Sostantivo più frequenti di", testo)
    print(commonBigrammi2)
    print()

def calcolaProbBigrams(tokens_list, testo):
    #lista token dove ogni token deve ave una frequenza maggiore di 3
    tokensTOT = []
    for token in tokens_list:
        if(tokens_list.count(token)>3):
            tokensTOT.append(token)

    bigrammi_list = list(bigrams(tokensTOT))
    distribuzioneFreqBigrammi = nltk.FreqDist(bigrammi_list)
    commonBigrammi20 = distribuzioneFreqBigrammi.most_common(20)
    listaBigrammiOrdinata = []
    print(testo)
    #Calcolo probabilità congiunta
    for bigramma in commonBigrammi20:
        listaBigrammiOrdinata.append(bigramma[0])
    for bigramma in listaBigrammiOrdinata:
        frequenzaBigramma = bigrammi_list.count(bigramma)
        frequenzaA = tokensTOT.count(bigramma[0])
        probCondizionata = frequenzaBigramma/frequenzaA
        probCongiunta = (frequenzaA/len(tokensTOT))*(probCondizionata)
        print("probabilità congiunta del bigramma", bigramma, "\t", probCongiunta)
    print()
    #Calcolo probabilità condizionata
    for bigramma in listaBigrammiOrdinata:
        frequenzaBigramma = bigrammi_list.count(bigramma)
        frequenzaA = tokensTOT.count(bigramma[0])
        probCondizionata = frequenzaBigramma/frequenzaA
        print("probabilità condizionata del bigramma", bigramma, "\t", probCondizionata)
    print()
    #Calcolo Local Mutual Information
    for bigramma in listaBigrammiOrdinata:
        frequenzaBigramma = bigrammi_list.count(bigramma)
        frequenzaA = tokensTOT.count(bigramma[0])
        probCondizionata = frequenzaBigramma/frequenzaA
        probCongiunta = (frequenzaA/len(tokensTOT))*(probCondizionata)
        frequenzaB = tokensTOT.count(bigramma[1])

        #Calcolo probabilità congiunta come se A e B fossero indipendenti 
        probA = frequenzaA/len(tokensTOT)
        probB = frequenzaB/len(tokensTOT)
        probCongiuntaAB = probA*probB

        localMUtualInformation = frequenzaBigramma * math.log2(probCongiunta/probCongiuntaAB)
        print("LMI del bigramma", bigramma, "\t", localMUtualInformation)
    print()

def calcolaMarkov1(sentences_list, tokens_list, testo):
    vocabolario = set(tokens_list)
    distribuzione_tokens = nltk.FreqDist(tokens_list)
    bigrams_list = list(bigrams(tokens_list))
    distribuzione_bigrams = nltk.FreqDist(bigrams_list)
    markovMAX = 0.0
    markovMAX2 = 0.0
    markovMAX3 = 0.0
    markovMAX4 = 0.0
    markovMAX5 = 0.0
    markovMAX6 = 0.0
    markovMAX7 = 0.0
    for sentence in sentences_list:
         tokens_sentence = word_tokenize(sentence)
         bigrams_sentence = list(bigrams(tokens_sentence))
         token1 = bigrams_sentence[0][0]
         probabilita = (distribuzione_tokens[token1]+1)/(len(tokens_list)+len(vocabolario))
         for bigramma in bigrams_sentence:
             freqBigramma = (distribuzione_bigrams[bigramma])
             frequenzaA = distribuzione_tokens[bigramma[0]]
             probCondizionata = (freqBigramma+1)/(frequenzaA+len(vocabolario))
             probabilita = probabilita*probCondizionata
             if(len(tokens_sentence)==8 and probabilita > markovMAX):
                markovMAX = probabilita
             if(len(tokens_sentence)==9 and probabilita > markovMAX2):
                markovMAX2 = probabilita
             if(len(tokens_sentence)==10 and probabilita > markovMAX3):
                markovMAX3 = probabilita
             if(len(tokens_sentence)==11 and probabilita > markovMAX4):
                markovMAX4 = probabilita
             if(len(tokens_sentence)==12 and probabilita > markovMAX5):
                markovMAX5 = probabilita
             if(len(tokens_sentence)==13 and probabilita > markovMAX6):
                markovMAX6 = probabilita
             if(len(tokens_sentence)==14 and probabilita > markovMAX7):
                markovMAX7 = probabilita
    print("markov1 di", testo)
    print("probabilitaMAX frase con lunghezza 8\t", markovMAX)
    print("probabilitaMAX frase con lunghezza 9\t", markovMAX2)
    print("probabilitaMAX frase con lunghezza 10\t", markovMAX3)
    print("probabilitaMAX frase con lunghezza 11\t", markovMAX4)
    print("probabilitaMAX frase con lunghezza 12\t", markovMAX5)
    print("probabilitaMAX frase con lunghezza 13\t", markovMAX6)
    print("probabilitaMAX frase con lunghezza 14\t", markovMAX7)
    print()

def analisiLinguistica(tokensPOS_list, testo):
    nomi = []
    luoghi = []
    analisi = nltk.ne_chunk(tokensPOS_list)
    for nodo in analisi:
        NE = ""
        if hasattr(nodo, "label"):
            if nodo.label() == "PERSON":
                for partNE in nodo.leaves():
                    NE = NE + " " + partNE[0]
                nomi.append(NE)
            if nodo.label() == "GPE":
                for partNE in nodo.leaves():
                    NE = NE + " " + partNE[0]
                luoghi.append(NE)
    distNomi = nltk.FreqDist(nomi)
    distNomiOrdinati = distNomi.most_common(15)
    print("i 15 nomi propri di persona più frequenti di", testo)
    print(distNomiOrdinati)
    print()
    distLuoghi = nltk.FreqDist(luoghi)
    distLuoghiOrdinati = distLuoghi.most_common(15)
    print("i 15 nomi propri di luogo più frequenti di", testo)
    print(distLuoghiOrdinati)
    print()

def main(testo1, testo2):
    text_file1 = open(testo1, mode="r", encoding="utf-8")
    text_file2 = open(testo2, mode="r", encoding="utf-8")
    text1 = text_file1.read()
    text2 = text_file2.read()
    sentences_list1 = sent_tokenize(text1)
    sentences_list2 = sent_tokenize(text2)
    tokensPOS_list1 = calcolaTokensPOS(sentences_list1)
    tokensPOS_list2 = calcolaTokensPOS(sentences_list2)
    tokens_list1 = calcolaTokensTesto(sentences_list1)
    tokens_list2 = calcolaTokensTesto(sentences_list2)
    most_commonPOS(tokensPOS_list1, tokens_list1, testo1)
    most_commonPOS(tokensPOS_list2, tokens_list2, testo2)
    calcolaProbBigrams(tokens_list1, testo1)
    calcolaProbBigrams(tokens_list2, testo2)
    calcolaMarkov1(sentences_list1, tokens_list1, testo1)
    calcolaMarkov1(sentences_list2, tokens_list2, testo2)
    analisiLinguistica(tokensPOS_list1, testo1)
    analisiLinguistica(tokensPOS_list2, testo2)

main(sys.argv[1], sys.argv[2])