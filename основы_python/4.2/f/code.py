def order(*request):
    global in_stock
    recipe = {"Эспрессо": {"coffee": 1, "milk": 0, "cream": 0},
              "Капучино": {"coffee": 1, "milk": 3, "cream": 0},
              "Макиато": {"coffee": 2, "milk": 1, "cream": 0},
              "Кофе по-венски": {"coffee": 1, "milk": 0, "cream": 2},
              "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
              "Кон Панна": {"coffee": 1, "milk": 0, "cream": 1}}
    coffee, milk, cream = in_stock["coffee"], in_stock["milk"], in_stock["cream"]
    in_request = None
    for req in request:
        coffee_, milk_, cream_ = recipe[req]["coffee"], recipe[req]["milk"], recipe[req]["cream"]
        if coffee_ <= coffee and milk_ <= milk and cream_ <= cream:
            coffee -= coffee_
            milk -= milk_
            cream -= cream_
            in_request = req
            break
    in_stock.update({"coffee": coffee, "milk": milk, "cream": cream})
    if not in_request:
        return 'К сожалению, не можем предложить Вам напиток'
    return in_request
