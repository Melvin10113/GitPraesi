import ProductionOrder


class ProductionLine:

    def __init__(self, name: int):
        self.__name = name
        self.__production_line_orders = []

    def add_order(self, order):
        self.__production_line_orders.append(order)

    def get_production_line_name(self):
        return self.__name

    def get_orders(self):
        return self.__production_line_orders
    
    def get_order(self, order_number):
        return self.__production_line_orders[order_number]
    