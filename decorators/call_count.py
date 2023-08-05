from typing import Any


class CallCount:
    def __init__(self, f):
        """
        Purpose: function that is called
        """

        self.f = f
        self.count = 0
    # end alternate constructor

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.count += 1
        return self.f(*args, **kwds)


@CallCount
def hello(name):
    print('hello %s' % name)