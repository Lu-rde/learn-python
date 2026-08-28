# Rocket Mission Control
def rocket_data ():
     rocket_name = input ("Rocket Name:")
     rocket_mass = float (input("Rocket Mass:"))
     fuel_mass = float(input("Fuel Mass:"))
     number_of_engines = int (input ("Number of Engines:"))
     destination = input ("Destination:")

     return rocket_mass, rocket_name, fuel_mass, number_of_engines, destination

rocket_mass, rocket_name, fuel_mass, number_of_engines, destination = rocket_data ()

def rocket_calculations ():
     dry_mass = rocket_mass - fuel_mass

     fuel_percentage = fuel_mass / rocket_mass *100

     return dry_mass, fuel_percentage

dry_mass , fuel_percentage = rocket_calculations ()

print (f"\n ROCKET REPORT: \n Rocket Name: {rocket_name}, \n Rocket Mass:{rocket_mass}, \n Fuel Mass: {fuel_mass},\n Number of Engines:{number_of_engines}, \n Destination: {destination}, \n Dry Mass: {dry_mass}, \n Fuel Percentage: {fuel_percentage}")

print ("\n ROCKET TESTS:")

if fuel_percentage >= 50:
    print ("\n FUEL: READY")

else:
     print ("\n FUEL: ERROR")

if number_of_engines >0:
     print ("\n ENGINES: READY")

else :
     print ("\n ENGINES: ERROR")

if fuel_mass < rocket_mass :
     print ("\n MASS : CHECKED")

else: print("\n MASS: ERROR")

if fuel_percentage >= 50 and number_of_engines>0 and fuel_mass<rocket_mass:
    print ("\n STATUS: READY FOR LAUNCH")
    for num in range (5,0,-1):
        print ("\n T",num)
    print ("\n LIFTOFF!")

else :
     print ("\n STATUS: LAUNCH ABORTED")

