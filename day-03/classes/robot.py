# Robot ###############
# name:str
# hardware:list
# software:list
# hello:method
#######################

class Robot:

    def __init__(self, name:str, hardware:list, software:list):
        self.name = name
        self.hardware = hardware
        self.software = software

    def __repr__(self):
        return f"Robot(hardware_count={self.hardware_count()}, software_count={self.software_count()})"

    def hardware_count(self):
        return len(self.hardware)

    def software_count(self):
        return len(self.software)

    def hello(self, user):
        return f"Greetings {user}, my name is {self.name}. I am at your service"

all_robots = []