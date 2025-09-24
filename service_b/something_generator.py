import random
from const import SOMETHINGS

from grpc_gen import something_pb2


def process_somethings(something_obj: something_pb2.SomethingMessage) -> something_pb2.SomethingMessage:
    """
    fill the 'something_from_another_service' field of something_obj with a random something from SOMETHINGS
    return: something_pb2.SomethingMessage
    """
    something_obj.something_from_another_service = random.choice(SOMETHINGS)

    return something_obj
