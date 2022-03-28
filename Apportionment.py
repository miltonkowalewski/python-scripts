import uuid
import random
from typing import List

def getQueues():
    return [
        {
            "name": f"queue-{uuid.uuid4()}",
            "messages": random.randrange(start=0, stop=100)
        }
        for i in range(10)
    ]

def getMessages():
    return [f"message-{i}" for i in range(1000000)]

queues = getQueues()
messages = getMessages()

print(queues[0])
print(messages[0])

class ApportionmentObject:

    data: list = []

    def __init__(self, current_quantity, ref) -> None:
        self.current_quantity = current_quantity
        self.ref = ref

class Apportionment:
    def __calc_load(self, score, value_division, amount_of_data):
        return round((score / value_division if value_division else 1) * amount_of_data)

    def score_adjustment(self, list_of_numbers: list):
        if 0 in list_of_numbers:
            return [number+1 for number in list_of_numbers]
        else:
            return list_of_numbers

    def load(self, apportionments: List[ApportionmentObject], data: list, reverse: bool = True):
        amount_of_data = len(data) # 4532
        apportionments.sort(key=lambda x: x.current_quantity, reverse=reverse)
        scores = self.score_adjustment([apportionment.current_quantity for apportionment in apportionments])
        value_division = sum(scores) # 322
        cached_position = 0
        for index, score in enumerate(scores[::-1]):
            quantity_to_load = self.__calc_load(score, value_division, amount_of_data)
            apportionments[index].data = data[cached_position:quantity_to_load+cached_position]
            cached_position = quantity_to_load+cached_position
        return apportionments

charge = Apportionment().load([ApportionmentObject(queue["messages"], queue["name"]) for queue in queues], messages)

for c in charge:
    print(f"Apportionment quantity: {len(c.data)} - Queue: {c.ref} - Current Quantity:{c.current_quantity}")
