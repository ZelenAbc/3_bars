import json

FILE_PATH = './bars.json'


def load_data(file_path):
    with open(file_path, 'r') as f:
        json_data = f.read()
    data = json.loads(json_data)
    return data


def get_distance_in_square_between_points(p1, p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2


def get_biggest_bar(data):
    bars = data['features']
    return max(bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(data):
    bars = data['features']
    return min(bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    bars = data['features']
    my_point = [longitude, latitude]
    return min(bars, key=lambda x: get_distance_in_square_between_points(x['geometry']['coordinates'], my_point))


if __name__ == '__main__':
    data_with_bars = load_data(FILE_PATH)

    ask = "Tell please longitude and latitude: "
    position = list(map(float, input(ask).split()))

    biggest_bar = get_biggest_bar(data_with_bars)
    smallest_bar = get_smallest_bar(data_with_bars)
    closest_bar = get_closest_bar(data_with_bars, *position)

    text = 'Biggest bar\'s global id:\n{}\n' \
           'Smallest bar\'s global id:\n{}\n' \
           'Closest bar\'s global id:\n{}\n'

    result = text.format(*map(lambda x: x['properties']['Attributes']['global_id'], [biggest_bar, smallest_bar, closest_bar]))

    print(result)
