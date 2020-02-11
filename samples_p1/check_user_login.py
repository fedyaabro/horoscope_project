from samples_p1.db import list_users


def reg_user():
    registered_users = list_users()
    i = 0
    while i < len(registered_users):
        username = registered_users[i][0]
        last_seen = registered_users[i][1]
        print(username, last_seen)
        i += 1
