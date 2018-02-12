# Paragraph_structure


Core Functions: 

1, parse and analyse a paragraph, according to the meaning and importance of each sentence

2, get a parsed tree from a paragraph, and get three attributes(weight, level, children) of each sentence


Attributes:

1, weight: the number of keywords

2, level: the more its keywords are, the higher its level is

3, children: a sentence's keywords are more than its children and include the most of its children's keywords

(keywords: the meaningful and useful words of a sentences, most of them are nouns)


Handling Process:

1, web crawling for all the urls from which the source articles(papers and their abstracts) can be gotten

2, parseing the article, and generating its tree and its sentences' three attributes


Files:

spides_abs.py: web crawling (1,urls 2,abstracts)

para_tree.py: generate a tree structure for a paragraph

url.txt: all the crawled urls

url_4.txt: the 4th kind of crawled urls, which are used for latter processing

tree/*: each file includes the crawled abstract and its tree 






