import itertools as it

import json
filename = 'data/belleville_businesses.txt'


def reformatted_data(filename):
    with open(filename, 'r') as f:
        for key, group in it.groupby(f, lambda line: line.startswith('View Details')):
            if not key:
                group = list(group)
                del group[1]
                if len(group) > 3:
                    del group[3]
                print(group)
                with open(r'new_file.txt', 'a') as fp:
                    for item in group:
                        # write each item on a new line
                        fp.write(item)
        print('Done')


def count_integer_occurrences(string):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    return count


def convert_cleaned_file_to_JSON(filename, output_filename='belleville_businesses.json'):
    businesses = []
    with open(filename, 'r') as f:
        for key, group in it.groupby(f, lambda line: line.startswith('\n')):
            if not key:
                group = list(group)
                business = {
                    'name': group[0].strip(),
                    'address': '',
                    'phone': ''
                }
                if len(group) == 2:
                    # if phone number is present, it will be the last item in the list and will have 10 digits
                    if count_integer_occurrences(group[-1]) > 9:
                        business['phone'] = group[-1].strip()
                    else:
                        business['address'] = group[-1].strip()
                # if all 3 elements are present
                if len(group) == 3:
                    business['phone'] = group[2].strip()
                    business['address'] = group[1].strip()
                businesses.append(business)
        with open(output_filename, 'w') as fp:
            json.dump(businesses, fp)


convert_cleaned_file_to_JSON(filename)
