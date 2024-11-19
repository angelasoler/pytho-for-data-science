
def NULL_not_found(object: any) -> int:
    obj_type = type(object)

    if object is None:
        var_name = 'Nothing'
    elif (object == ''):
        var_name = 'Empty'
    elif object != object:
        var_name = 'Cheese'
    elif object is False and isinstance(object, bool):
        var_name = 'Fake'
    elif object == 0:
        var_name = 'Zero'
    else:
        print("Type not Found")
        return 1
    print(f'{var_name}: {object} {obj_type}')
    return 0
