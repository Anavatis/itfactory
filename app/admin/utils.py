import functools


def admin_required(f):

    @functools.wraps(f)
    def decorator(*args, **kwargs):
        return f(*args, **kwargs)

    return decorator