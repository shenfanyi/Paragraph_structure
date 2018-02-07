#!/usr/bin/env python3
#-*- coding: UTF-8 -*-




from para_tree import Paragraph, Sentence
import json
from anytree import RenderTree



para = '''
 This paper presents the Averaged CVB (ACVB) inference and offers convergence-guaranteed and practically
 useful fast Collapsed Variational Bayes (CVB) inferences.  CVB inferences yield more
precise inferences of Bayesian probabilistic models than Variational Bayes (VB) inferences. How-
ever, their convergence aspect is fairly unknown and has not been scrutinized. To make CVB more
useful, we study their convergence behaviors in a empirical and practical approach.  We develop
a convergence-guaranteed algorithm for any CVB-based inference called ACVB, which enables
automatic convergence detection and frees non-expert practitioners from the difficult and costly
manual monitoring of inference processe s.  In experiments, ACVB inferences are comparable to
or better than those of existing  inference methods and deterministic, fast, and provide easier con-
vergence detection.  These features are especially convenient for  who want precise
Bayesian inference with assured convergence.
'''


Para = Paragraph(para_content = para)


head = Para.tree()[0]
print(RenderTree(head))


sents = Para.cut_para_to_sents()

for sent in sents:
    sentence = Sentence(para_content = para, sent_content = sent).attribute()

    with open('sents1.json', 'a') as f:
        f.write(json.dumps(sentence) + '\n')


