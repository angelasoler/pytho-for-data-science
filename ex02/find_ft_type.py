
def all_thing_is_obj(object: any) -> int:
    type_name = type(object).__name__
    type_def = type(object)
    
    if isinstance(object, str):
        print(f'{object} is in the kitchen: {type_def}')
    elif isinstance(object, int):
        print("Type not found")
    else:
        print(f'{type_name}: {type_def}')
    return 42
