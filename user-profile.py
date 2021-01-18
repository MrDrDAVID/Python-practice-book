def build_user_profile(first_name, last_name, **user_info):
    '''Builds a profile dictionary from given arguments'''
    user_profile = {}

    user_profile['first name'] = first_name
    user_profile['last name'] = last_name

    for key, value in user_info.items():
        user_profile[key] = value

    return user_profile

david_profile = build_user_profile('David', 'Garza', location='Paramount', boo='laineyboo', occupation='Software engineer')
print(david_profile)