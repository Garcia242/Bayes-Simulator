#import rocketpy

class rocket:
    def __init__(self, burn, thrust, mass, fuel_mass, fin_area, nose_area, CoM, CoP):

        self.burn = burn #burn time 
        self.thrust = thrust #thrust
        self.mass = mass #mass
        self.fuel_mass = fuel_mass #fuel mass
        self.fin_area = fin_area #area for the fins
        self.nose_area = nose_area #area for the nose cone 
        self.drag_coefficient = 0.5 #drag coefficient
        self.CoM = CoM #center of mass (y position)
        self.CoP = CoP #center of pressure (y position)
        
        #define angles of the rocket wrt the vertical
        #theta = angle of the rocket with respect to the vertical
        #phi = angle of the rocket with respect to the horizontal
        #psi = angle of the rocket rotating abount its axis
        self.theta = 0
        self.phi = 0
        self.psi = 0
        
        #
        self.g = 9.81 #acceleration due to gravity
        self.rho = 1.225 #density of air

        
    def position_init(self, x, y, z, vx, vy, vz, r):
        # Initialize the position and velocity of the rocket's center of mass
        self.pos = [x, y, z]
        self.vel = [vx, vy, vz]
        self.r = [0,0,r]
        self.time = 0
        return x, y, z
    
    

    def forces (self):
        if self.time < self.burn:
            
            
            
            
            

        else: 




        
