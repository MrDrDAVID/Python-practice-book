current_users = ['laineyboo', 'laineysboo', 'wackboy', 'mrdrdavid', 'admin', 'john']
new_users = ['laineyboo', 'batman', 'laineysboo', 'robin', 'boo123', 'JOHN']

for user in new_users:
    if user.lower() in current_users:
        print('Sorry, but the username ' + user + ' is not available')
    else:
        print('The username ' + user + ' is available')