from PIL.DdsImagePlugin import module


def introspection_info(obj):
    
    type_obj = type(obj).__name__
    attribute = [at for at in dir(obj) if not callable(getattr(obj, at))]
    methods = [m for m in dir(obj) if getattr(obj, m)]
    module = obj.__class__.__module__



    dict_info = {'type': type_obj, 'attribute': attribute, 'methods': methods, 'module': module}
    return dict_info




number_info = introspection_info(42)
print(number_info)