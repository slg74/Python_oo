#!/usr/bin/python

class Plane:
    def __init__(self, manufacturer, designation, engine_type, wingspan, max_airspeed):
    	self.manufacturer = manufacturer
    	self.designation  = designation
    	self.engine_type  = engine_type
    	self.wingspan     = wingspan
    	self.max_airspeed = max_airspeed

    def get_manufacturer(self):
    	return self.manufacturer

    def get_designation(self):
    	return self.designation

    def get_engine_type(self):
    	return self.engine_type

    def get_wingspan(self):
    	return self.wingspan

    def get_max_airspeed(self):
    	return self.max_airspeed


def main():

	plane_001 = Plane("Boeing", "777", "Turbofan", "200.00ft", "587 mph ... 945 km/h")

	print plane_001.get_manufacturer()
	print plane_001.get_designation()
	print plane_001.get_engine_type()
	print plane_001.get_wingspan()
	print plane_001.get_max_airspeed()

	print "\n\n"

	plane_002 = Plane("General Dynamics", "F-16", "Turbofan", "33.00ft", "1500 mph")

	print plane_002.get_manufacturer()
	print plane_002.get_designation()
	print plane_002.get_engine_type()
	print plane_002.get_wingspan()
	print plane_002.get_max_airspeed()
	
if __name__ == '__main__':
	main()

