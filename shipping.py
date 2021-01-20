# shipping.py

import sys


def get_hermes_price(item_value):
    base_cost = 290
    
    # Signature is required for all purchases
    signature = 90

    if item_value <= 2000:
        cover = 0
    elif item_value <= 5000:
        cover = 0.03 * item_value - 60
    elif item_value <= 8000:
        cover = 0.01 * item_value + 40
    elif item_value <= 9500:
        cover = 0.02 * item_value - 40
    elif item_value <= 20000:
        cover = 0.04 * item_value - 230
    elif item_value <= 25000:
        cover = 0.05 * item_value - 430
    elif item_value <= 30000:
        cover = 0.04 * item_value - 180
    else:
        cover = 1020

    return (base_cost + signature + cover)


def get_collect_plus_yodel_price(item_value):
    base_cost = 279

    if item_value <= 5000:
        cover = 100
    elif item_value <= 10000:
        cover = 200
    elif item_value <= 15000:
        cover = 300
    elif item_value <= 30000:
        cover = 500

    return (base_cost + cover)


def get_royal_mail_price(item_value):
    if item_value <= 10000:
        return 510
    elif item_value <= 50000:
        return 885
    elif item_value <= 100000:
        return 985
    elif item_value <= 250000:
        return 1185


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Invalid arguments:")
        print(sys.argv)
    else:
        item_value = int(sys.argv[1])
        shipping_costs = {
            "Hermes": get_hermes_price(item_value),
            "CollectPlus (Yodel)": get_collect_plus_yodel_price(item_value),
            "Royal Mail": get_royal_mail_price(item_value)
        }

        print("\n--------------------------------------------------------------")
        print("To ship a package worth £{:.2f}:\n".format(item_value/100))
        for (courier, price) in shipping_costs.items():
            print("{}: £{:.2f}".format(courier, price/100))

        cheapest_courier = min(shipping_costs, key=shipping_costs.get)
        
        print("\n--------------------------------------------------------------")
        print("Cheapest courier is {}, who charge £{:.2f}.".format(cheapest_courier, shipping_costs[cheapest_courier]/100))
        print("--------------------------------------------------------------")
