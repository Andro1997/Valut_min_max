import untangle
valutes = {}
resource = 'http://www.cbr.ru/scripts/XML_daily.asp'

obj = untangle.parse(resource)
valute = obj.ValCurs.Valute

for v in valute:
    name = v.Name.cdata
    price = v.Value.cdata
    valutes[name] = float(price.replace(",", ".", 1))

peacturs_max = ''
peacturs_min = ''

max = valutes[name]
min = valutes[name]

def get_max(valutes, max, peacturs_max):
    for key, value in valutes.items():
        if value >= float(max):
            max = value
            peacturs_max = "{}, max: {}".format(key, max)
    return peacturs_max

def get_min(valutes, min, peacturs_min):
    for key, value in valutes.items():
        if value <= float(min):
            min = value
            peacturs_min = "{}, min: {}".format(key, min)
    return peacturs_min

print(get_max(valutes, max, peacturs_max))
print(get_min(valutes, min, peacturs_min))