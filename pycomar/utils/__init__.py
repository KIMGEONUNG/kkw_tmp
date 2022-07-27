import uuid
from datetime import datetime


__all__ = ['gen_id']


def gen_id(name='', date=False, delimiter='_', len_hash=7):
    id = ''
    id += datetime.today().strftime('%Y%m%d') + delimiter if date else ''
    id += name + delimiter if name != '' else ''
    id += uuid.uuid4().hex[:len_hash]
    return id


if __name__ == '__main__':

    print(gen_id("hello"))
    print(gen_id("hello", True))
