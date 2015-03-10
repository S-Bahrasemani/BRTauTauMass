from rootpy.tree import Cut

from .base import Category

HADHAD = Cut('hadhad == 1')
TAU1_ETA = Cut('abs(tau1_eta) < 2.5')
TAU2_ETA = Cut('abs(tau2_eta) < 2.5')

PRESELECTION = (
    HADHAD 
    & TAU1_ETA & TAU2_ETA
    )

class Category_Preselection(Category):
    name = 'preselection'
    label = '#tau_{had}#tau_{had} Preselection'
    common_cuts = PRESELECTION
