import ProductionOrder

class mes_utils:
    @staticmethod
    def get_order_by_number(production_line, order_number):
        for order in production_line:
            if order.order_number == order_number:
                return order
        return None


    @staticmethod
    def calculate_production_efficiency(order: ProductionOrder):
        if order.__finished:
            return order.__produced_units / order.__quantity * 100
        else:
            raise Exception('Cannot calculate efficiency for this order')