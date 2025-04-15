class Logger(object):

    def __init__(self):
        self.arr_mes={}

    def shouldPrintMessage(self, timestamp, message):
        last_ts=self.arr_mes.get(message, -float('inf'))
        if timestamp-last_ts<10:
            return False
        self.arr_mes[message]=timestamp
        return True



log =Logger()
log.shouldPrintMessage(1,"foo")
log.shouldPrintMessage(2,"bar")
log.shouldPrintMessage(3,"foo")
log.shouldPrintMessage(8,"bar")
log.shouldPrintMessage(10,"foo")
log.shouldPrintMessage(11,"foo")

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)