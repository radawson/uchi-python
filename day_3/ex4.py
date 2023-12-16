def flatten_dict(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                output_dict[f"{key}.{sub_key}"] = sub_value
        else:
            output_dict[key] = value
    return output_dict


input_dict = {
    'a': 1,
    'b': {
        'i': 2,
        'j': 3
    },
    'c': 4
}

flatten_dict(input_dict)
# {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}