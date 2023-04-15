from pprint import pprint

def hello_world(*args, **kwargs):
    print('hello world')
    pprint(args)
    pprint(kwargs)


if __name__ == "__main__":
    import fire
    fire.core.Display = lambda lines, out: print(*lines, file=out)
    fire.Fire({
        'hello_world': hello_world,
    })