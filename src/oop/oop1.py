# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# Base class: Vehicle

class Vehicle():
    pass


# Branch route 1: Ground

class GroundVehicle(Vehicle):
    pass

# Ground branches to the two types of ground vehicles:

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass


# Branch route 2: Flight

class FlightVehicle(Vehicle):
    pass

# Flight branches to the two types of flight vehicles:

class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass