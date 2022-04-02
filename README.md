# Fluent

Decorator that makes all methods "fluent"

# How to use

```python
from fluent import fluent


@fluent()
class YourBestClass:
    ...
```

If you provide method names, it will exclude from modify:

```python
from fluent import fluent


@fluent('your_beautiful_method')
class YourBestClass:
    def your_beautiful_method(self, *args, **kwargs):
        ...
```

or

```python
from fluent import fluent


@fluent('your_beautiful_method_1', 'your_beautiful_method_2')
class YourBestClass:
    def your_beautiful_method_1(self, *args, **kwargs):
        ...

    def your_beautiful_method_2(self, *args, **kwargs):
        ...
```

# Dependencies
 
- [inspect_mate](https://pypi.org/project/inspect_mate/)