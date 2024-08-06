file_name = 'country_info.txt'
countries = {}
with open(file_name, encoding='utf-8') as info:
    info.readline()
    for line in info:
        data = line.strip().split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')

        country_dict = {
            'name': country,
            'capital': capital,
            'code': code,
            'code3': code3,
            'dialing': dialing,
            'timezone': timezone,
            'currency': currency
        }
        print(country_dict)
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict

print(countries)


name = input('Enter country name').casefold()

capital_name = countries[name]['capital']

print(capital_name)
