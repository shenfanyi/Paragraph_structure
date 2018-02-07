#!/usr/bin/env python3
#-*- coding: UTF-8 -*-



from anytree import Node, RenderTree
import spacy
from spacy.symbols import NOUN

nlp = spacy.load('en')



class Paragraph(object):


    def __init__(self, para_content):
        self.para_content = para_content


    def cut_para_to_sents(self):
        sents_raw = self.para_content.split('.')

        sents_handled = list()
        for i in sents_raw:
            if i != '' and i != '\n':
                sent = i.strip('\n').strip().replace('\n', ' ')
                sents_handled.append(sent)
        return sents_handled


    def tree(self):

        def keywords(sent):
            keywords = list()
            # sent = sent.encode('unicode-escape')
            cutted = nlp(sent)
            for word in cutted:
                if word.pos == NOUN:
                    keywords.append(word)
            return keywords

        def find_key_by_value(dic, val):
            key_list = []
            for key, value in dic.items():
                if value == val:
                    key_list.append(key)
            return key_list

        def isin(item, li):
            for i in li:
                if str(item) is str(i) or str(item) == str(i):
                    return True
            return False

        def values_by_keys(dic, keys):
            values = list()
            for i in keys:
                values.append(dic[i])
            return values

        def cut_para_to_sents():
            sents_raw = self.para_content.split('.')

            sents_handled = list()
            for i in sents_raw:
                if i != '' and i != '\n':
                    sent = i.strip('\n').strip().replace('\n', ' ')
                    sents_handled.append(sent)
            return sents_handled


        sents_handled = cut_para_to_sents()

        dic_sent = {}
        for i in range(len(sents_handled)):
            dic_sent[i] = sents_handled[i]

        dic_keywords = {}
        for i in range(len(dic_sent)):
            dic_keywords[i] = keywords(dic_sent[i])

        dic_weight = {}
        for i in range(len(sents_handled)):
            dic_weight[i] = len(dic_keywords[i])


        head = Node('head')

        index = list(dic_weight.keys())

        index_pop = list()
        for i in range(100):
            if len(index_pop) < len(index):
                index_poped = [i for i in index if i not in index_pop]
                # print(index_poped)

                weights = values_by_keys(dic_weight, index_poped)
                max_weight = max(weights)
                max_index = find_key_by_value(dic_weight, max_weight)

                for i in max_index:
                    level_1 = Node(dic_sent[i], parent=head)
                    index_pop.append(i)

                for i in index_poped:
                    for j in range(len(dic_keywords[i])):
                        x = dic_keywords[i][j]
                        y = dic_keywords[max_index[-1]]
                        if isin(x,y):
                            level_2 =  Node(dic_sent[i], parent=level_1)
                            index_pop.append(i)
                            break

            else:
                break

        return head, dic_sent, dic_weight




class Sentence(object):

    def __init__(self, para_content, sent_content):
        self.para_content = para_content
        self.sent_content = sent_content


    def attribute(self):

        para_attr = Paragraph(self.para_content).tree()

        head_tree = para_attr[0]
        level = 2
        children = []
        for i in head_tree.children:
            # print(i.name)
            # print(self.sent_content)
            if i.name == self.sent_content:
                level = 1
                children = i.children
                break
        children_list =  []
        if len(children) != 0:
            for i in children:
                children_list.append(i.name)

        dic_sent = para_attr[1]
        dic_weight = para_attr[2]
        for index, sent in dic_sent.items():
            if sent == self.sent_content:
                weight = dic_weight[index]

        return weight, level, children_list


