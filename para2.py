#!/usr/bin/env python3
#-*- coding: UTF-8 -*-



from para_tree import Paragraph, Sentence
import json
from anytree import RenderTree



para = u'A typical viral marketing model identifies influential users in a social network to maximize a single product adoption assuming unlimited user attention, campaign budgets, and time. In reality, multiple products need campaigns, users have limited attention, convincing users incurs costs, and advertisers have limited budgets and expect the adoptions to be maximized soon. Facing these user, monetary, and timing constraints, we formulate the problem as a submodular maximization task in a continuous-time diffusion model under the intersection of one matroid and multiple knapsack constraints. We propose a randomized algorithm estimating the user influence (Partial results in the paper on influence estimation have been published in a conference paper: Nan Du, Le Song, Manuel Gomez-Rodriguez, and Hongyuan Zha. Scalable influence estimation in continuous time diffusion networks. In Advances in Neural Information Processing Systems 26, 2013.) in a network (|V| nodes, |E| edges) to an accuracy of ϵ with n=O(1/ϵ2) randomizations and O~(n|E|+n|V|) computations. By exploiting the influence estimation algorithm as a subroutine, we develop an adaptive threshold greedy algorithm achieving an approximation factor ka/(2+2k) of the optimal when ka out of the k knapsack constraints are active. Extensive experiments on networks of millions of nodes demonstrate that the proposed algorithms achieve the state-of- the-art in terms of effectiveness and scalability.'
# sent = 'A typical viral marketing model identifies influential users in a social network to maximize a single product adoption assuming unlimited user attention, campaign budgets, and time'


Para = Paragraph(para_content = para)


head = Para.tree()[0]
print(RenderTree(head))


sents = Para.cut_para_to_sents()

for sent in sents:
    sentence = Sentence(para_content = para, sent_content = sent).attribute()

    with open('sents2.json', 'a') as f:
        f.write(json.dumps(sentence) + '\n')
