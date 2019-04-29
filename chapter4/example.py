# encoding: utf8

import nn
import searchengine as se

# get_ipython().magic(u'logstart example.py append')


def test_nn():
    online, pharmacy = 1, 2
    spam, notspam = 1, 2
    possible = [spam, notspam]
    neuralnet = nn.searchnet('nntest.db')
    neuralnet.maketables()
    neuralnet.trainquery([online], possible, notspam)
    neuralnet.trainquery([online, pharmacy], possible, spam)
    neuralnet.trainquery([pharmacy], possible, notspam)
    neuralnet.getresult([online, pharmacy], possible)
    neuralnet.getresult([online], possible)
    neuralnet.trainquery([online], possible, notspam)
    neuralnet.getresult([online], possible)
    neuralnet.trainquery([online], possible, notspam)
    neuralnet.getresult([online], possible)
    quit()


def test_se_crawler():
    """
    Test search engine cralwer
    """
    crawler = se.crawler('crawler.db')
    crawler.createindextables()
    pages = ['https://mengyangyang.org/', 'https://docs.python.org/2/']
    crawler.crawl(pages, 2)
    crawler.calculatepagerank(20)


def test_se_search():
    searcher = se.searcher('crawler.db')
    result = searcher.query('python language blog')
    print result


if __name__ == '__main__':
    test_se_search()
