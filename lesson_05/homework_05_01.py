# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements
cars_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
    'Kia': ('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': ('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
    'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': ('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
    'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': ('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}

search_criteria = (2017, 1.6, 36000)
# print(search_criteria[0],search_criteria[1],search_criteria[2])
year_value = search_criteria[0]  # year>=2017
engine_capacity_value = search_criteria[1]  # engine_capacity>=1.6
price_value = search_criteria[2]  # price<=36000
cars_count = 5

# сортування
sorted_cars = sorted(cars_data.items(), key=lambda x: x[1][4])
sorted_cars1 = dict(sorted_cars)


def find_cars_by_year(year):
    return [car_id for car_id, car_data in sorted_cars1.items() if car_data[1] >= year]


developers1 = find_cars_by_year(year_value)


def find_cars_by_engine_capacity(engine_capacity):
    return [car_id for car_id, car_data in sorted_cars1.items() if car_data[2] >= engine_capacity]


developers2 = find_cars_by_engine_capacity(engine_capacity_value)


def find_cars_by_price(price):
    return [car_id for car_id, car_data in sorted_cars1.items() if car_data[2] <= price]


developers3 = find_cars_by_price(price_value)
logical_intersection = set(developers1).intersection(set(developers2)).intersection(set(developers3))
# print('Автомобілі, які відповідають критеріям пошуку.',logical_intersection)

print(f"\nСортований список з {cars_count} автомобілів:")
count = 1
for car_id, car_list in sorted_cars:
    if count <= cars_count and car_id in logical_intersection:
        count += 1
        print(f"{car_id} : year {car_list[1]}, engine_capacity {car_list[2]}, price {car_list[4]}")
