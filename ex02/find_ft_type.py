
def all_thing_is_obj(object: any) -> int:
    num_obj = [int, bool, float]
    type_name = type(object).__name__
    type_def = type(object)
    
    if isinstance(object, str):
        print(f'{object} is in the kitchen: {type_def}')
    elif type(object) in num_obj:
        print("Type not found")
    else:
        print(f'{type_name}: {type_def}')
    return 42
