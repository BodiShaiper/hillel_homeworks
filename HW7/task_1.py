import sys


def my_custom_print(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    output = sep.join(map(str, args)) + end

    if file in (sys.stdout, sys.stderr):
        file.write(output)
        if flush:
            file.flush()
    else:
        with open(file, 'a') as f:
            f.write(output)
            if flush:
                f.flush()


# Example usage
my_custom_print('Hello', 'world!')
my_custom_print('This is', 'just another', 'example', 'to', 'check', 'the', 'function!')
