from a import a
from functools import partial

b = partial(a, 1)
b.__doc__ = "This WILL NOT appear in the html output."

def c(x):
    return x

d = partial(c, 1)
d.__doc__ = "This WILL appear in the html output."
