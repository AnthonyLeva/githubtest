# pylint: disable=w,c
import random


def gen_adjective():
    """Generate a random adjective.

    Arguments: Doesn't take any arguments.
    """
    seq = [
        'nice', 'perfect', 'good', 'great', 'hot', 'awesome', 'kind',
        'sophisticated', 'beautiful', 'exhausted', 'relaxed', 'chill', 'tired',
        'happy', 'sad', 'shocked', 'surprised', 'pretty', 'cute', 'handsome',
        'confused', 'lost'
    ]
    adj = random.choice(seq)
    return adj
