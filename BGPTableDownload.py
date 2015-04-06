import basesinfonierspout
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import requests

class BGPTableDownload(basesinfonierspout.BaseSinfonierSpout):

    def __init__(self):

        basesinfonierspout.BaseSinfonierSpout().__init__()

    def useropen(self):
        
        self.interval = int(self.getParam("frequency"))        
        
        self.sched = BlockingScheduler()
        self.sched.add_job(self.job, "interval", seconds=self.interval, id="bgptable")
        self.sched.start()

    def usernextTuple(self):

        pass
        
    def job(self):
        
        query = "http://bgp.potaroo.net/v6/as2.0/bgptable.txt"
        self.log(query)
        headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0"
        }
        r = requests.get(query, headers=headers)
        self.emit()
        
BGPTableDownload().run()
