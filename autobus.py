class Autobus:
    # all_bus = []

    def __init__(self, start_name, end_name, number, time):
        self.start_name = start_name
        self.end_name = end_name
        self.number = number
        self.time = time
        # Autobus.all_bus.append(self)

    def get_start_name(self):
        return self.start_name

    def set_start_name(self, new_start):
        self.start_name = new_start

    def get_end_name(self):
        return self.end_name

    def set_end_name(self, new_end):
        self.end_name = new_end

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time


    def get_info(self):
        return (f"----------\n"
                f"Route number: {self.number}\n"
                f"Starting point: {self.start_name}\n"
                f"Destination point: {self.end_name}\n"
                f"Travel time: {self.time}\n"
                f"----------\n")