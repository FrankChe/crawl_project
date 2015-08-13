#coding:utf-8
__author__ = 'chexiaoyu'

import urllib
import urllib2
import json

class Crawl:

    def __init__(self):
        self.stories_population = []
        self.stories_cities = []
        self.stories_GDP = []

    def get_GDP(self):
        self.stories_cities = []
        self.stories_GDP = []

        values = {"m":"QueryData","dbcode":"fsnd","rowcode":"reg","colcode":"sj","wds":"[{'wdcode':'zb','valuecode':'A020101'}]","dfwds":"[]","k1":"1439429397267"}
        data = urllib.urlencode(values)
        url = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData'
        request = urllib2.Request(url, data)
        response = urllib2.urlopen(request)
        js = response.read()
        js = json.loads(js)

        for i in range(len(js['returndata']['datanodes'])):
            temp = []
            temp.append(js['returndata']['datanodes'][i]['data']['strdata'])
            temp.append(js['returndata']['datanodes'][i]['wds'][1]['valuecode'])
            temp.append(js['returndata']['datanodes'][i]['wds'][2]['valuecode'])
            self.stories_GDP.append(temp)



    def get_population(self):
        self.stories_population = []
        self.stories_cities = []
        values = {"m":"QueryData","dbcode":"fsnd","rowcode":"reg","colcode":"sj","wds":"[{'wdcode':'zb','valuecode':'A03080302'}]","dfwds":"[]","k1":"1439369419140"}
        data = urllib.urlencode(values)
        url = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData'
        request = urllib2.Request(url, data)
        response = urllib2.urlopen(request)

        js =  response.read()
        js = json.loads(js)

        for i in range(len(js['returndata']['datanodes'])):
            temp = []
            temp.append(js['returndata']['datanodes'][i]['data']['strdata'])
            temp.append(js['returndata']['datanodes'][i]['wds'][1]['valuecode'])
            temp.append(js['returndata']['datanodes'][i]['wds'][2]['valuecode'])
            self.stories_population.append(temp)

        #print self.stories_population

        for i in range(len(js['returndata']['wdnodes'][1]['nodes'])):
            temp = []
            temp.append(js['returndata']['wdnodes'][1]['nodes'][i]['cname'])
            temp.append(js['returndata']['wdnodes'][1]['nodes'][i]['code'])
            self.stories_cities.append(temp)

        #print self.stories_cities
        # print js['returndata']['datanodes'][0]['wds'][1]['valuecode']
        # print js['returndata']['datanodes'][0]['wds'][2]['valuecode']
        #print js.key("returndata").key("datanodes")[0].key("wds")[1].key("valuecode").value()
        #str = js.returndata.datanodes[1].wds[1].valuecode
        #print json.loads(response.read())

cr = Crawl()
cr.get_population()
