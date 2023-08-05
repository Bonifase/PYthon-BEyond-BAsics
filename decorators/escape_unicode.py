def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap

@escape_unicode
def northen_city():
    return "TromsÓ"

print(northen_city())