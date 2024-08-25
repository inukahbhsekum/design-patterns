from functools import wraps


def make_blink(function):
    """Defines a decorator"""

    # This will make the decorator transparent in terms of name and docs
    @wraps(function)

    def decorator(*args, **kwargs):
        ret = function(*args, **kwargs)

        return "<blink>" + ret + "</blink>"
    
    return decorator


@make_blink
def hello_world(word1, word2):
    return "Hello, world! " + word1 + word2


print(hello_world("new world 1", "new world 2"))
print(hello_world("new world 3", "new world 4"))
print(hello_world.__doc__)
print(hello_world.__name__)
