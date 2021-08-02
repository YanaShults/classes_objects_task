from autobus import Autobus

list_all_bus = []
# dict_all_bas = []

def create_autopark():
    n = int(input("Enter the number of buses: "))

    for bus in range(1, n+1):
        print(f"----------")
        number = int(input(f"Enter the route number of {bus} bus: "))
        start_name = input(f"Enter the starting point of {bus} bus: ")
        end_name = input(f"Enter the destination point of {bus} bus: ")
        time = input(f"Enter the travel time of {bus} bus: ")
        print(f"----------\n")
        new_autobus = Autobus(start_name, end_name, number, time)
        list_all_bus.append(new_autobus)
        # for i in list_all_bus:
        #     dict_all_bas.append({"number": i.number, "start_name": i.start_name,
        #                      "end_name": i.end_name, "time": i.time})
        with open("bus.txt", "a") as file:
            # file.write("----------\n")
            file.write(''.join(new_autobus.get_info()))
            # file.write("\n----------\n")

    return list_all_bus

def show_autopark():
    with open("bus.txt", "r") as file:
        print(file.read())

def sort_by_number():
    # sort_list_all_bus = sorted(list_all_bus, key=lambda i: i["number"])
    sort_list_all_bus = sorted(list_all_bus, key=lambda i: i.number)
    for i in sort_list_all_bus:
        print(i.get_info())

    # print(sort_list_all_bus)

def search_by_point(point):
    for i in list_all_bus:
        if point == i.start_name or point == i.end_name:
            print(i.get_info())

# print(create_autopark())
create_autopark()
# show_autopark()

# sort_by_number()
# search_by_point("Prague")


