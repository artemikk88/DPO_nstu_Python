def shipment_cost(goods_count):
    if goods_count == 1:
        return 10.95
    elif goods_count > 1:
        cost = 10.95 + (goods_count-1)*2.95
        return cost
    return 0


goods_count = int(input("Введите количество товаров в заказе: "))
print("Сумма доставки: ", shipment_cost(goods_count), "$")
