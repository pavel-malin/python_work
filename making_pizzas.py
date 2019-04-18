import pizza
pizza.make_1pizza(16, 'peppironi')
pizza.make_1pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_1pizza
make_1pizza(16, 'peppironi')
make_1pizza(12, 'mishrooms', 'green peppers', 'extra cheese')

from pizza import make_1pizza as mp
mp(16, 'peppironi')
mp(12, 'mishrooms', 'green peppers', 'extra cheese')

import pizza as p
p.make_1pizza(16, 'peppironi')
p.make_1pizza(12, 'mishrooms', 'green peppers', 'extra cheese')
'''
from pizza import *
make_1pizza(16, 'peppironi')
make_1pizza(12, 'mishrooms', 'green peppers', 'extra cheese')
'''