import rocketpy

class rocket
    def __init__(self, burn, thrust, mass, fuel_mass, fin_area, nose_area):

        self.burn = burn #burn time 
        self.thrust = thrust #thrust
        self.mass = mass #mass
        self.fuel_mass = fuel_mass #fuel mass
        self.fin_area = fin_area #area for the fins
        self.nose_area = nose_area #area for the nose cone 
        self.drag_coefficient = 0.5 #drag coefficient
        
    def position_init(self, x, y, z, vx, vy, vz):
        # Initialize the position and velocity of the rocket
        # Calculate the position of the rocket
        self.pos = [x, y, z]
        self.vel = [vx, vy, vz]
    return x , y, z


        
