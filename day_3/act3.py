def flatten_dict(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                output_dict[f"{key}.{sub_key}"] = sub_value
        else:
            output_dict[key] = value
    return output_dict

def unflatten_dict(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        if "." in key:
            split_key = key.split(".")
            if split_key[0] not in output_dict:
                output_dict[split_key[0]] = {}
            output_dict[split_key[0]][split_key[1]] = value
        else:
            output_dict[key] = value
    return output_dict


def treemap(func, input_list):
    output_list = []
    for item in input_list:
        if isinstance(item, list):
            output_list.append(treemap(func, item))
        else:
            output_list.append(func(item))
    return output_list


if __name__ ==  "__main__":
    print(flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4})) # should print {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}
    print(unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4})) # should print {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}
    print(treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])) # should print [1, 4, [9, 16, [25]]]