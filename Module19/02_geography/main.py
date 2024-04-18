num_countries = int(input('Количество стран: '))
country = []
countries = []
country_dict = dict()


for i_country in range(num_countries):
    print('{} страна: '.format(i_country + 1), end='')
    country.append(input('').split())

for i in range(num_countries):
    country_dict[country[i][0]] = list(country[i][1:])

countries.append(list(country_dict.keys()))

for i_city in range(3):
    print('{}й город: '.format(i_city + 1), end='')
    city = input()
    step = 0
    for i in country_dict.values():
        if city in i:
            print('Город {0} расположен в стране {1}.'.format(city, countries[0][step]))
        else:
            step += 1
            if step > num_countries - 1:
                print('По городу {} данных нет.'.format(city))

