def filter_kwargs(model, kwargs):
    expected_fields = [field.name for field in model._meta.concrete_fields]
    filtered_kwargs = {arg: kwargs[arg] for arg in kwargs if arg in expected_fields}
    return filtered_kwargs
