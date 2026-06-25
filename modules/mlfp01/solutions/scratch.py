# Unit 9-19a
price_psf = 2000
size_sqf = 1000
address = '35 Jalan Tua Kong'
region = 'East'
floor = 9
unit = '19a'
property_name = 'Blissful Homes'

# Collections
# List
row1 = [2000, 1000, '35 Jalan Tua Kong', 'East', 9, '19a', 'Blissful Homes']

# List of lists = Table
table1 = [
    [2000, 1000, '35 Jalan Tua Kong', 'East', 9, '19a', 'Blissful Homes'],
    [2400, 800, '35 Jalan Tua Kong', 'East', 4, '34', 'Blissful Homes']
]

# To access row 1 of table1
print(table1[0]) # by position
# To access the size of row 1 unit
print(table1[0][1])


# Dictionaries
row1_dict = {
    price_psf: 2000,
    size_sqf: 1000,
    address: '35 Jalan Tua Kong',
    region: 'East',
    floor: 9,
    unit: '19a',
    property_name: 'Blissful Homes',
}

# To get the size
row1_dict['size_sqf']

table1_list_of_dict = [
    {
        price_psf: 2000,
        size_sqf: 1000,
        address: '35 Jalan Tua Kong',
        region: 'East',
        floor: 9,
        unit: '19a',
        property_name: 'Blissful Homes',
        date: datetime(2010, 1, 1)
    },
    {
        price_psf: 2400,
        size_sqf: 800,
        address: '35 Jalan Tua Kong',
        region: 'East',
        floor: 4,
        unit: '34',
        property_name: 'Blissful Homes',
        date: datetime(2007, 12, 12)
    }
]

table1_dict_of_dict = {
    datetime(2010, 1, 1): {
        price_psf: 2000,
        size_sqf: 1000,
        address: '35 Jalan Tua Kong',
        region: 'East',
        floor: 9,
        unit: '19a',
        property_name: 'Blissful Homes',
    },
    datetime(2007, 12, 12): {
        price_psf: 2400,
        size_sqf: 800,
        address: '35 Jalan Tua Kong',
        region: 'East',
        floor: 4,
        unit: '34',
        property_name: 'Blissful Homes',
    }
}

# For loop vs while loop
