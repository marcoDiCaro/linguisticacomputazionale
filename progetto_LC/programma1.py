import sys
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize

def calcolaTokensTesto(sentences_list):
    tokensTOT = []
    for sentence in sentences_list:
        tokens = word_tokenize(sentence)
        tokensTOT += tokens
    return tokensTOT

def calcolaMediaTokens(tokens_list):
    charTokensTOT = 0
    for token in tokens_list:
        chars = len(token)
        charTokensTOT+=chars
    return len(tokens_list)/charTokensTOT

def calcolaVocabolario(tokens_list):
    tokens5000 = tokens_list[0:5000]
    vocabolario = set(tokens5000)
    return vocabolario

def calcolcaDistribuzioneClassiFreq(tokens_list, testo):
    print("distribuzione delle classi di frequenza di", testo)
    for i in range(0, len(tokens_list), 500):
        hapax = []
        v5 = []
        v10 = []
        listaTokens = tokens_list[0:i+500]
        vocabolario = set(listaTokens)
        for token in vocabolario:
            conteggio = listaTokens.count(token)
            if (conteggio == 1):
                hapax.append(token)
            if (conteggio == 5):
                v5.append(token)
            if (conteggio == 10):
                v10.append(token)
        print(i, "-", len(tokens_list))
        print("distribuzione di frequenza di v1\t", len(hapax))
        print("distribuzione di frequenza di v5\t", len(v5))
        print("distribuzione di frequenza di v10\t", len(v10))
        print()
    print()

def calcolaTokensPOS(sentences_list):
    posTOT = []
    for sentence in sentences_list:
        tokens = word_tokenize(sentence)
        pos = nltk.pos_tag(tokens)
        posTOT+=pos
    return posTOT

def calcolaSostantivi(tokensPOS_list):
    sostantiviTOT_list = []
    for bigramma in tokensPOS_list:
        if(bigramma[1] in ["NN", "NNS", "NNP", "NNPS"]):
            sostantiviTOT_list.append(bigramma)
    return sostantiviTOT_list

def calcolaVerbi(tokensPOS_list):
    verbiTOT_list = []
    for bigramma in tokensPOS_list:
        if(bigramma[1] in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]):
            verbiTOT_list.append(bigramma)
    return verbiTOT_list

def calcolaAvverbi(tokensPOS_list):
    avverbiTOT_list = []
    for bigramma in tokensPOS_list:
        if(bigramma[1] in ["RB", "RBR", "RBS"]):
            avverbiTOT_list.append(bigramma)
    return avverbiTOT_list

def calcolaAggettivi(tokensPOS_list):
    aggettiviTOT_list = []
    for bigramma in tokensPOS_list:
        if(bigramma[1] in ["JJ", "JJR", "JJS"]):
            aggettiviTOT_list.append(bigramma)
    return aggettiviTOT_list

def calcolaTokensPOSord(tokensPOS_list):
    ordPOStot_list = []
    for bigramma in tokensPOS_list:
        if(bigramma[1] not in [",", "."]):
            ordPOStot_list.append(bigramma)
    return ordPOStot_list

def main(testo1, testo2):
    text_file1 = open(testo1, mode="r", encoding="utf-8")
    text_file2 = open(testo2, mode="r", encoding="utf-8")
    text1 = text_file1.read()
    text2 = text_file2.read()
    sentences_list1 = sent_tokenize(text1)
    print("Numero frasi", testo1, "\t", len(sentences_list1))
    sentences_list2 = sent_tokenize(text2)
    print("Numero frasi", testo2, "\t", len(sentences_list2))

    #Confronto i due testi sulla base del numero di frasi
    print()
    if(len(sentences_list1) > len(sentences_list2)):
        print(testo1, "ha più frasi")
    elif(len(sentences_list1) < len(sentences_list2)):
        print(testo2, "ha più frasi")
    else:
        print(testo1, "\t", testo2, "hanno lo stesso numero di frasi")
    print()
    
    tokens_list1 = calcolaTokensTesto(sentences_list1)
    print("Numero tokens", testo1, "\t", len(tokens_list1))
    tokens_list2 = calcolaTokensTesto(sentences_list2)
    print("Numero tokens", testo2, "\t", len(tokens_list2))

    #Confronto i due testi sulla base del numero di tokens
    print()
    if(len(tokens_list1) > len(tokens_list2)):
        print(testo1, "ha più tokens")
    elif(len(tokens_list1) < len(tokens_list2)):
        print(testo2, "ha più tokens")
    else:
        print(testo1, "\t", testo2, "hanno lo stesso numero di tokens")
    print()

    media_sentence1 = len(sentences_list1)/len(tokens_list1)
    print("lunghezza media frasi in termini di token", testo1, "\t", media_sentence1)
    media_sentence2 = len(sentences_list2)/len(tokens_list2)
    print("lunghezza media frasi in termini di token", testo2, "\t", media_sentence2)
    media_tokens1 = calcolaMediaTokens(tokens_list1)
    print("lunghezza media parole in termini di caratteri", testo1, "\t", media_tokens1)
    media_tokens2 = calcolaMediaTokens(tokens_list2)
    print("lunghezza media parole in termini di caratteri", testo2, "\t", media_tokens2)

    print()

    vocabolario1 = calcolaVocabolario(tokens_list1)
    print("Grandezza vocabolario", testo1, "\t", len(vocabolario1))
    vocabolario2 = calcolaVocabolario(tokens_list2)
    print("Grandezza vocabolario", testo2, "\t", len(vocabolario2))

    #Confronto i due testi sulla base della grandezza del vocabolario
    print()
    if(len(vocabolario1) > len(vocabolario2)):
        print(testo1, "ha un vocabolario più grande")
    elif(len(vocabolario1) < len(vocabolario2)):
        print(testo2, "ha un vocabolario più grande")
    else:
        print(testo1, "\t", testo2, "hanno la stessta grandenzza di vocabolario")
    print()

    type_token_ratio1 = len(vocabolario1)/5000
    print("TTR", testo1, "\t", type_token_ratio1)
    type_token_ratio2 = len(vocabolario2)/5000
    print("TTR", testo2, "\t", type_token_ratio2)

    #Confronto i due testi sulla base della ricchezza lessicale
    print()
    if(type_token_ratio1 > type_token_ratio2):
        print(testo1, "ha una ricchezza lessicale più grande")
    elif(type_token_ratio1 < type_token_ratio2):
        print(testo2, "ha una ricchezza lessicale più grande")
    else:
        print(testo1, "\t", testo2, "hanno la stessta ricchezza lessicale")
    print()

    calcolcaDistribuzioneClassiFreq(tokens_list1, testo1)
    calcolcaDistribuzioneClassiFreq(tokens_list2, testo2)

    tokensPOS_list1 = calcolaTokensPOS(sentences_list1)
    tokensPOS_list2 = calcolaTokensPOS(sentences_list2)
    sostantiviTOT_testo1 = calcolaSostantivi(tokensPOS_list1)
    sostantiviTOT_testo2 = calcolaSostantivi(tokensPOS_list2)
    media_sostantivi1 = len(sostantiviTOT_testo1)/len(sentences_list1)
    print("media di Sostantivi per frase", testo1, "\t", media_sostantivi1)
    media_sostantivi2 = len(sostantiviTOT_testo2)/len(sentences_list2)
    print("media di Sostantivi per frase", testo2, "\t", media_sostantivi2)
    verbiTOT_testo1 = calcolaVerbi(tokensPOS_list1)
    verbiTOT_testo2 = calcolaVerbi(tokensPOS_list2)
    media_verbi1 = len(verbiTOT_testo1)/len(sentences_list1)
    print("media di verbi per frase", testo1, "\t", media_verbi1)
    media_verbi2 = len(verbiTOT_testo2)/len(sentences_list2)
    print("media di verbi per frase", testo2, "\t", media_verbi2)
    avverbiTOT_testo1 = calcolaAvverbi(tokensPOS_list1)
    avverbiTOT_testo2 = calcolaAvverbi(tokensPOS_list2)
    aggettiviTOT_testo1 = calcolaAggettivi(tokensPOS_list1)
    aggettiviTOT_testo2 = calcolaAggettivi(tokensPOS_list2)

    #Lista parole nel testo ad esclusione dei segni di punteggiatura marcati con POS "," "."
    tokensPOSord_list1 = calcolaTokensPOSord(tokensPOS_list1)
    tokensPOSord_list2 = calcolaTokensPOSord(tokensPOS_list2)

    #calcolo la densità lessicale
    print()
    densitaLes_testo1 = (len(sostantiviTOT_testo1) + len(verbiTOT_testo1) + len(avverbiTOT_testo1) + len(aggettiviTOT_testo1)) / len(tokensPOSord_list1)
    print("densità lessicale", testo1, "\t", densitaLes_testo1)
    densitaLes_testo2 = (len(sostantiviTOT_testo2) + len(verbiTOT_testo2) + len(avverbiTOT_testo2) + len(aggettiviTOT_testo2)) / len(tokensPOSord_list2)
    print("densità lessicale", testo2, "\t", densitaLes_testo2)

main(sys.argv[1], sys.argv[2])