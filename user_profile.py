def build_profile(first, last, **user_info):
    '''Builds a dictionary with user information.'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
user_profile = build_profile('albert', 'einstein',
                            location ='princeton',
                            field='physics')

print(user_profile)

def build_0profile(first, last, **user_info):
    '''Builds a dictionary with user information.'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_0profile('adama', 'bern',
                            mapder='gop',
                            birber='ammy')
print(user_profile)