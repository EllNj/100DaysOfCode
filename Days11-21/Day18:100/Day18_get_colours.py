import colorgram
temp = colorgram.extract('spot_image.jpg', 12)
colours = []
for each in temp:
    r = each.rgb.r
    g = each.rgb.g
    b = each.rgb.b
    colours.append((r, g, b))
print(colours)
