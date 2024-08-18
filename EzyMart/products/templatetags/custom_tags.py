from django import template
register = template.Library()

@register.filter(name = 'chunks')
def chunks(list_data, row_size):
    nanban = []
    i = 0
    for data in list_data:
        nanban.append(data)
        i += 1
        if len(nanban) == row_size:
            yield nanban
            nanban = []
    yield nanban