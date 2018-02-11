#!/usr/bin/env python3
#-*- coding: UTF-8 -*-



import urllib3
import re
from bs4 import BeautifulSoup
from para_tree import Paragraph, Sentence
import json
from anytree import RenderTree



# urls = list()
# for i in range(1,19):
#
#     source_url = 'http://jmlr.org/papers/v' + str(i) + '/'
#
#     http = urllib3.PoolManager()
#     r = http.request('GET', source_url)
#
#     soup = BeautifulSoup(r.data, 'html.parser', from_encoding='utf-8')
#     # print(soup.prettify())
#
#     # links_1 = soup.find_all('a', href=re.compile(r"^(http).*(a|b).html"))
#     # links_2 = soup.find_all('a', href=re.compile(r"^[^http]^[^/].*(a|b).html"))
#     # links_3 = soup.find_all('a', href=re.compile(r"^/.*(a|b).html"))
#     links_4 = soup.find_all('a', href=re.compile(r"^[^http].*\d.html"))
#     #
#     # for link in links_1:
#     #     url = link['href']
#     #     urls.append(url)
#     #
#     # for link in links_2:
#     #     url = link['href']
#     #     urls.append(source_url + url)
#     #
#     # for link in links_3:
#     #     url = link['href']
#     #     urls.append(source_url[:-1] + url)
#
#     for link in links_4:
#         url = link['href']
#         urls.append('http://jmlr.org' + url)
#
# print(len(urls))
# print(urls)
#
# for url in urls:
#     with open('url_4.txt', 'a') as f:
#         f.write(url + '\n')



urls = open("url_4.txt").readlines()
print(urls)

n = 0
for i in urls:
    url = i[:-1]
    print(url)
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        # print(r.data)

        soup = BeautifulSoup(r.data, 'html.parser', from_encoding='utf-8')
        # print(soup.prettify())

        cont = soup.find_all('div', id="content")

        cont_str = str(cont)
        abs_str = cont_str.split('\n\n')[1].split('<')[0]
        print(abs_str)


        n += 1

        filename = 'tree/' + str(n) + '.json'
        with open(filename, 'a') as f:
            f.write(str(abs_str) + '\n\n')


        Para = Paragraph(para_content=abs_str)
        head = Para.tree()[0]
        print(RenderTree(head))

        sents = Para.cut_para_to_sents()

        for sent in sents:
            sentence = Sentence(para_content=abs_str, sent_content=sent).attribute()

            with open(filename, 'a') as f:
                f.write(json.dumps(sentence) + '\n')

        # break


    except BaseException:
        continue
    else:
        continue

print(n)



