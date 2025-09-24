import random
from const import SOMETHINGS
from schema import SomethingSchema


def process_somethings(something_obj: SomethingSchema) -> dict:
    """
    fill the 'something_from_another_service' field of something_obj with a random something from SOMETHINGS
    return: dict
    """
    something_obj.something_from_another_service = random.choice(SOMETHINGS)

    return something_obj.__dict__
