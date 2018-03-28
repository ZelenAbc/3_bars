import json

FILE_PATH = './bars.json'


def load_data(file_path):
    with open(file_path, 'r') as f:
        json_data = f.read()
    data = json.loads(json_data)
    return data


def get_distance_in_square_between_points(p1, p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2


def get_biggest_bar(bars):
    return max(bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars):
    return min(bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars, longitude, latitude):
    my_point = [longitude, latitude]
    return min(bars, key=lambda x: get_distance_in_square_between_points(x['geometry']['coordinates'], my_point))


if __name__ == '__main__':
    data_with_bars = load_data(FILE_PATH)
    bars_list = data_with_bars['features']

    ask = "Tell please longitude and latitude: "
    position = list(map(float, input(ask).split()))

    biggest_bar = get_biggest_bar(bars_list)
    smallest_bar = get_smallest_bar(bars_list)
    closest_bar = get_closest_bar(bars_list, *position)

    template_for_print = 'Biggest bar\'s global id: {}\n' \
                         'Smallest bar\'s global id: {}\n' \
                         'Closest bar\'s global id: {}\n'

    text_for_print = template_for_print.format(*map(
        lambda x: x['properties']['Attributes']['global_id'],
        [biggest_bar, smallest_bar, closest_bar]))

    print(text_for_print)
