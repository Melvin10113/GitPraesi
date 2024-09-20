import ProductionLine
import ProductionOrder
import MES_Utils

class MES:

    def __init__(self):
        self.__productionLines = []

    def add_production_line(self, name):
        self.__productionLines.append(ProductionLine.ProductionLine(name))

    def get_production_lines(self):
        for line in self.__productionLines:
            print(f"Produktionslinie: {line.get_production_line_name()}")

    def get_production_line(self, name):
        try:
            index = next(i for i, line in enumerate(self.__productionLines) if line.get_production_line_name() == name)
            return self.__productionLines[index]
        except StopIteration:
            return None

    def create_production_order(self, production_line_name, order_number, product_name, quantity):
        self.get_production_line(production_line_name).add_order(ProductionOrder.ProductionOrder(order_number, product_name, quantity))
        return None

    def produce_units(self, production_line_name):
        for production_line in self.__productionLines:
            all_orders = production_line.get_orders()
            for order in all_orders:
                print(order.get_name() + " " + (str)(order.get_quantity()))
                print()
        return
    
    def start_production_order(self, production_line_name, order_number):
        production_line = self.get_production_line(production_line_name)
        order = MES_Utils.get_order_by_number(production_line, order_number)


if __name__ == '__main__':
    mes = MES()
    mes.add_production_line("1")

    #add order to production line
    mes.create_production_order("1", 1, "Schuh", 10)
    #get all orders from production line
    ordersFromLine1 = mes.get_production_line("1").get_orders()
    for order in ordersFromLine1:
        print("order number: " + str(order.get_order_number()) + ", product name: " + order.get_name() +
              ", units produced: " + str(order.get_produced_units()) + ", started: " + str(order.get_started_status()) +
              ", finished: " + str(order.get_finished_status()))
        
    print("---------------")
    mes.get_production_lines()
    mes.create_production_order("1", 1, "test", 100)

    mes.produce_units("1")


