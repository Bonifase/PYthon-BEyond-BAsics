from typing import Any


class Trace:
    def __init__(self,):
        """
        Purpose: value
        """

        self.enabled = True
    # end alternate constructor

    def __call__(self, f: callable) -> callable:
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling %s...' % f)
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

l = [1, 2, 3, 4, 5, 6]
for _ in range(len(l-2)):
    print(f'Rotating list {l}...')
    l = rotate_list(l)