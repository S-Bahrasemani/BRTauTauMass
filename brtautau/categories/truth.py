import math
from math import pi
from rootpy.tree import Cut

from .base import Category
TRUE_RESONANCE_PT = Cut('parent_pt>50')
TRUE_LEAD_JET_50 = Cut('true_jet1_no_overlap_pt>50000')
TRUE_SUBLEAD_JET_30 = Cut('true_jet2_no_overlap_pt>30000')
TRUE_2J = Cut('num_true_jets_no_overlap>1')
TRUE_JETS_DETA = 'true_dEta_jet1_jet2_no_overlap>{0}'
TRUE_JETS_MASS = Cut('true_mass_jet1_jet2_no_overlap>250000')


HADHAD = Cut('hadhad == 1')
LEPHAD = Cut('lephad ==1')
TAU1_ETA = Cut('abs(ditau_tau0_eta) < 2.5')
TAU2_ETA = Cut('abs(ditau_tau1_eta) < 2.5')
TAU1_PT = Cut('ditau_tau0_pt > 25.')
TAU2_PT = Cut('ditau_tau1_pt > 15.')

MET = Cut('met_et > 20.') ## evtsel_MET 
DR_TAUS = Cut('0.8 < ditau_dr< 2.4')
DETA_TAUS = Cut('ditau_deta < 1.5')
DPHI_MIN_TAUS_MET = Cut ('ditau_met_min_dphi< {}'.format( pi / 4))

## LEPHAD specific cuts
MT = Cut('transverse_mass_tau1_tau2 < 70000')
TAU_PT = Cut("tau1_pt > 20000. ")
LEP_PT = Cut("tau2_pt > 12000.")

PRESELECTION = (
    HADHAD 
    & DETA_TAUS
    & DR_TAUS
    & TAU1_PT & TAU2_PT
    & MET
    & DPHI_MIN_TAUS_MET
    &TRUE_RESONANCE_PT
    )

PRESELECTION_LH = (
    LEPHAD 
    & TAU1_ETA & TAU2_ETA
    & TAU_PT & LEP_PT
    & MT
    )



CUTS_TRUE_VBF = (
    TRUE_2J 
    & TRUE_LEAD_JET_50
    & TRUE_SUBLEAD_JET_30
    & Cut(TRUE_JETS_DETA.format(2.0))
    )

CUTS_TRUE_BOOSTED = (
    TRUE_RESONANCE_PT
    )

CUTS_TRUE_VBF_CUTBASED = (
    TRUE_2J 
    & TRUE_LEAD_JET_50
    & TRUE_SUBLEAD_JET_30
    & Cut(TRUE_JETS_DETA.format(2.6))
    & TRUE_JETS_MASS
    ) 

class Category_Preselection_TH(Category):
    name = 'preselection'
    label = '#tau_{had}#tau_{had} Preselection'
    common_cuts = PRESELECTION
 
class Category_Preselection_TH_LH(Category):
    name = 'preselection'
    label = '#tau_{lep}#tau_{had} Preselection'
    common_cuts = PRESELECTION_LH
 
