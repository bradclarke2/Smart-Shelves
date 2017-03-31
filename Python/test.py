import Objects.product as product

test = product.makeProductGrid()

for x in test:
    print(x.name, ",", x.tpnb, ",",x.height, ",",x.width, ",",x.depth, ",",x.weight)