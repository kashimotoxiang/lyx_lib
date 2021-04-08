import time
import os


def timestamp():
    return int(time.time())


def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('func:%r took: %2.4f sec' % (f.__name__, te - ts))
        return result

    return timed


def aria_format(url):
    path, filename = os.path.split(url)

    path = path.lstrip(r'https://').lstrip(r'http://')

    result = url + '\n dir=' + path + '\n out=' + filename + '\n'
    return result


def log(data, filename, stop=False, table_head=None):
    with open(filename, 'w', encoding='utf-8') as f:
        # write markdown header
        if table_head:
            f.write('|')
            for head in table_head:
                f.write(str(head))
                f.write('\t|\t')

            f.write('\n')

            f.write('|')
            for _ in range(len(table_head)):
                f.write('--- |')
            f.write('\n')

        for item in data:
            if isinstance(item, list) or isinstance(item, tuple):
                if table_head:
                    f.write('|')

                for element in item:
                    f.write(str(element) + '\t')
                    # write markdown splitter
                    if table_head:
                        f.write('|\t')
            else:
                f.write(str(item))

            f.write('\n')
    if stop:
        assert False
