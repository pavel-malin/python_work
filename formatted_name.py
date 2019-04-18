# 
def get_formatted_name(first_name, last_name):
    '''Returns a neatly formatted full name'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_0name(first_name, middle_name, last_name):
    '''Returns a neatly formatted full name'''
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_0name('john', 'lee', 'hooker')
print(musician)

def get_formatted_1name(first_name, last_name, middle_name=''):
    '''Returns a neatly formatted full name'''
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_1name('jimi', 'hendrix')
print(musician)

musician = get_formatted_1name('john', 'hooker', 'lee')
print(musician)