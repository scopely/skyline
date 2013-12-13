import urllib2
import urllib
import json

class Graphite:

    def __init__(self, metric_name):
        self.metric_name = metric_name
        self.url = "http://graphite1.scopely.io/render/"
    
    def time_series(self, from_time):
        values = {'target': self.metric_name, 'from': from_time, 'format': 'json'}
        data = urllib.urlencode(values)
        req = urllib2.Request(self.url, data)
        http_response = urllib2.urlopen(req)
        response = json.loads(http_response.read()) 
        for data_set in response:
            target = data_set[u'target'].encode('ascii', 'ignore')
            if target == self.metric_name:
                return data_set["datapoints"]

