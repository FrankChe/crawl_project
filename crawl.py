#coding:utf-8
__author__ = 'chexiaoyu'

import urllib
import urllib2
import json
import cookielib

class Crawl:

    def __init__(self):
        self.stories_population = []
        self.stories_cities = []
        self.stories_GDP = []
        self.stories_population_total = []
        self.stories_population_type = []
        self.stories_GDP_total = []
        self.stories_GDP_type = []

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

    def get_population_total(self):
        self.stories_population_total = []
        self.stories_population_type = []
        #values = {"m":"QueryData","dbcode":"hgnd","rowcode":"zb","colcode":"sj","wds":"[]","dfwds":"[]","k1":"1439432529672"}
        #data = urllib.urlencode(values)
        url = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%5D'
        #request = urllib2.Request(url, data)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        js = response.read()
        js = json.loads(js)

        for i in range(len(js['returndata']['datanodes'])):
            # (data,code,year)
            temp = []
            temp.append(js['returndata']['datanodes'][i]['data']['data'])
            temp.append(js['returndata']['datanodes'][i]['wds'][0]['valuecode'])
            temp.append(js['returndata']['datanodes'][i]['wds'][1]['valuecode'])
            self.stories_population_total.append(temp)

        for i in range(len(js['returndata']['wdnodes'][0]['nodes'])):
            temp = []
            temp.append(js['returndata']['wdnodes'][0]['nodes'][i]['cname'])
            temp.append(js['returndata']['wdnodes'][0]['nodes'][i]['code'])
            self.stories_population_type.append(temp)

    def get_GDP_total(self):
        self.stories_GDP_total = []
        self.stories_GDP_type = []
        # url = 'http://data.stats.gov.cn/easyquery.htm'
        url = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%5D&k1=1439446314050'
        # values = {"m":"QueryData","dbcode":"hgnd","rowcode":"zb","colcode":"sj","wds":[],"dfwds":[{'wdcode':'sj','valuecode':'LAST20'}],"k1":"1439443331900"}
        # data = urllib.urlencode(values)
        header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36','X-Requested-With':'XMLHttpRequest','Cookie':'JSESSIONID=999609E65DEE6CA3D7E411599C59E5C4; experience=show; _gscu_1771678062=39353681rjp1lk12; _gscbrs_1771678062=1; u=6'}
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        request = urllib2.Request(url=url,headers=header)
        response = opener.open(request)
        #response = urllib2.urlopen(request)
        js = response.read()
        js = json.loads(js)

        for i in range(len(js['returndata']['datanodes'])):
            #(data,code,year)
            temp = []
            temp.append(js['returndata']['datanodes'][i]['data']['strdata'])
            temp.append(js['returndata']['datanodes'][i]['wds'][0]['valuecode'])
            temp.append(js['returndata']['datanodes'][i]['wds'][1]['valuecode'])
            self.stories_GDP_total.append(temp)

        for i in range(len(js['returndata']['wdnodes'][0]['nodes'])):
            #(name,code)
            temp = []
            temp.append(js['returndata']['wdnodes'][0]['nodes'][i]['cname'])
            temp.append(js['returndata']['wdnodes'][0]['nodes'][i]['code'])
            self.stories_GDP_type.append(temp)









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

#cr = Crawl()
#cr.get_population()
