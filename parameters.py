"""
Model parameters
"""

import math
import numpy as np

# gravity (m s-2) 
g  = 9.8086

Pi = math.pi
    
rho = 1000.

'''
soil hydraulic parameters
'''
# mm/s
hyds = 0.023635

bch  = 5.537291

# abs(soil%sucs_vec(:,1)/1000. (m) the soil matric potential at saturation 
sucs = 0.073613075

#ssat, saturated water content
theta_sat = 0.396073

#watr, residual water content
theta_r   = 0.02

# Specific gas constant J/(kg·K) (wikipedia's value is 461.5)
Rwv = 461.4
    
# lm=1.73e-5, converts units
gamma = 0.0000173 

# C%A33, inertial sublayer sw/us, given by the ratio of the standard deviation of vertical velocity to the friction velocity in the inertial sublayer above the canopy
a_3 = 1.25 

# rough%hruff (m) canopy height for evergreen broadleaf
h  = 20. #35. 
#rough%hruff = MAX( 1.e-6,veg%hc - 1.2*ssnow%snowd/MAX(ssnow%ssdnn,100.)), canopy height above snow level
    
# C%CSW canopy sw decay (Weil theory), determine decrease rate of standard deviation of canopy vertical velocity
Csw = 0.50 
    
# C%CTL (K s-1)  Wagga wheat (RDD 1992, Challenges), relates to temperature under canopy to the friction velocity and canopy height
Ctl = 0.40 

# (Jm-2) surface tension of liquid water 
sigma = 0.071 

#  canopy%sublayer_dz, height above the soil surface of U_x
z = 0.005

# air%rlam (J kg-1) latent heat of vaporization 
Lv = 2501400. 
# air%rlam= C%HL (J kg-1) 

# rt_Dff=2.5e-5 (m2 s-1), diffusion of wtare vapor
D = 0.0000282 
