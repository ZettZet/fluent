__version__ = "0.1.0"

from typing import TypeVar, Any, Callable

from inspect_mate import get_class_methods, get_regular_methods

T = TypeVar('T')

__all__ = ('fluent',)


def fluent(*exclude_method_names: str) -> Callable[[T], T]:
    """Builds class decorator, that wraps any method
    that not starts or ends with underscore('_') and not in exclude list.

    Also, it will not affect built-ins methods such as '__init__', '__str__' etc.

    WARNING: This decorator effects on your code.
    Therefore, IDE will mark all fluent calls as a warning and debug tools may provide invalid info. Remember it

    :param exclude_method_names: methods in this list will be not affected by this decorator
    :return: actual class decorator
    """

    def _class_decorator(cls: T, bmn=exclude_method_names) -> T:
        def __decorator(func: Callable[[...], Any]):
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
                return args[0]

            return wrapper

        methods = get_regular_methods(cls) + get_class_methods(cls)
        for name, method in methods:
            if not (name.startswith('_') or name.endswith('_') or name in bmn):
                setattr(cls, name, __decorator(method))

        return cls

    return _class_decorator
