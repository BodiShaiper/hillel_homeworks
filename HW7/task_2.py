def my_custom_filter(function, iterable):
    for item in iterable:
        if function(item):
            yield item
