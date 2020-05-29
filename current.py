import json
from json.decoder import JSONDecodeError


def add_cur_user(db_user):
    with open('current.json', 'w') as outfile:
        json.dump(db_user, outfile, default=str)


def get_cur_user():
    try:
        with open('current.json') as f:
            return json.load(f)
    except JSONDecodeError:
        pass


def del_cur_user():
    open('current.json', 'w').close()
