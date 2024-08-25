import time

class Producer:
    """Define the resource-intensive object to instantiate"""
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")


class Proxy:
    """Define relatively less resource-intensive proxy to instantiate"""
    def __init__(self):
        self.occupied = False
        self.producer = None

    def produce(self):
        print("Artist is checking if producer is available")
        if (not self.occupied):
            self.producer = Producer()
            self.occupied = True
            time.sleep(2)
            self.producer.meet()
        else:
            time.sleep(2)
            print("Producer is busy")


p = Proxy()
p.produce()
p.produce()