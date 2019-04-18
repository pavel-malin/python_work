# 
def city_country(city='minsk', country='belarus'):
    city_name = city + ', ' + country
    return city_name.title()

c_name = city_country()
city_countrys = city_country('moscow', 'russia')
fist_city = city_country('warsaw', 'poland')
print(c_name + "\n" + city_countrys + "\n" + fist_city)


def city_0country(city='minsk', country='belarus'):
    if city:
        city_name = city + ', ' + country
        return city_name.title()
    elif country:
        city_name = city + ', ' + country
        return city_name.title()
    else:
        city_name = city + ', ' + country
        return city_name.title()

fist_city = city_0country('moscow', 'russia')
print(fist_city)

fist_city = city_0country('warsaw', 'poland')
print(fist_city)

fist_city = city_0country()
print(fist_city)