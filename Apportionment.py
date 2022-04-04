import uuid
import random
from typing import List

def getQueues():
    return [
        {
            "name": f"queue-{uuid.uuid4()}",
            "messages": random.randrange(start=0, stop=100),
            "asdasd": "asdsad"
        }
        for i in range(random.randrange(start=10, stop=15))
    ]

def getMessages():
    return [f"message-{i}" for i in range(3)]

queues = getQueues()
messages = getMessages()

print(queues[0])
print(messages[0])

class ApportionmentObject:

    def __init__(self, current_quantity, ref) -> None:
        self.current_quantity = current_quantity
        self.ref = ref
        self.data = []

class Apportionment:
    def __calc_load(self, score, value_division, amount_of_data):
        value = round((score / value_division if value_division else 1) * amount_of_data)
        return value if value else 1

    def score_adjustment(self, list_of_numbers: list):
        if 0 in list_of_numbers:
            return [number+1 for number in list_of_numbers]
        else:
            return list_of_numbers

    def load(self, apportionments: List[ApportionmentObject], data: list, reverse: bool = True):
        amount_of_data = len(data)
        apportionments.sort(key=lambda x: x.current_quantity, reverse=reverse)
        scores = self.score_adjustment([apportionment.current_quantity for apportionment in apportionments])
        value_division = sum(scores)
        cached_position = 0
        for index, score in enumerate(scores[::-1]):
            quantity_to_load = self.__calc_load(score, value_division, amount_of_data)
            apportionments[index].data = data[cached_position:quantity_to_load+cached_position]
            cached_position = quantity_to_load+cached_position
        return apportionments

print(len(messages))
charge = Apportionment().load([ApportionmentObject(queue["messages"], queue["name"]) for queue in queues], messages, False)

for c in charge:
    print(f"Apportionment quantity: {len(c.data)} - Queue: {c.ref} - Current Quantity:{c.current_quantity}")

print()
