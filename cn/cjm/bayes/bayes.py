# coding:utf-8

import os
import sys
import codecs

# 将训练样本中的中文文章分词并存入文本文件中
# import jieba.posseg as pseg  
# 
# if __name__ == '__main__':
#     corpus = []
#     f = codecs.open("./news_spam.csv", "r", "utf-8")  
#     f1 = codecs.open("./news_spam_jieba.csv", "w", "utf-8")
#     count = 0
#     while True:  
#         line = f.readline()  
#         if line:  
#             count = count + 1
#             line = line.split(",")
#             s = line[1]
#             words=pseg.cut(s)
#             temp = []
#             for key in words:
#                 temp.append(key.word)
#             sentence = " ".join(temp)
#             print line[0],',',sentence
#             corpus.append(sentence)
#             f1.write(line[0])
#             f1.write(',')
#             f1.write(sentence)
#             f1.write('\n')
#         else:  
#             break
#     f.close()
#     f1.close()
#  
#     
######################################################  
#Multinomial Naive Bayes Classifier  
print '*************************\nNaive Bayes\n*************************'  
from sklearn.naive_bayes import MultinomialNB  
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == '__main__':
    # 读取文本构建语料库
    corpus = []
    labels = []
    corpus_test = []
    labels_test = []
    f = codecs.open("./sms_spam.txt", "rb")  
    count = 0
    while True:  
        line = f.readline()  
        if count == 0:
            # 跳过第一行
            count = count + 1
            continue
        if line:  
            count = count + 1
            line = line.split(",")
            label = line[0]
            sentence = line[1]
            corpus.append(sentence)
            if "ham"==label:
                labels.append(0)
            elif "spam"==label:
                labels.append(1)
            if count > 5550:
                corpus_test.append(sentence)
                if "ham"==label:
                    labels_test.append(0)
                elif "spam"==label:
                    labels_test.append(1)
        else:
            break
     
    vectorizer=CountVectorizer()
    fea_train = vectorizer.fit_transform(corpus)
    print vectorizer.get_feature_names()
    print fea_train.toarray()
#      
    vectorizer2=CountVectorizer(vocabulary=vectorizer.vocabulary_)
    fea_test = vectorizer2.fit_transform(corpus_test)
#     print fea_test
    print fea_test.toarray()
#     print vectorizer2.get_feature_names()
    #create the Multinomial Naive Bayesian Classifier  
    clf = MultinomialNB(alpha = 1)   
    clf.fit(fea_train,labels)
       
    pred = clf.predict(fea_test);  
    for p in pred:
        if p == 0:
            print "正常邮件"
        else:
            print "垃圾邮件"
        
    