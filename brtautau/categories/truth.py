from rootpy.tree import Cut

from .base import Category
TRUE_RESONANCE_PT = Cut('true_resonance_pt>100000')
TRUE_LEAD_JET_50 = Cut('true_jet1_no_overlap_pt>50000')
TRUE_SUBLEAD_JET_30 = Cut('true_jet2_no_overlap_pt>30000')
TRUE_2J = Cut('num_true_jets_no_overlap>1')
TRUE_JETS_DETA = 'true_dEta_jet1_jet2_no_overlap>{0}'
TRUE_JETS_MASS = Cut('true_mass_jet1_jet2_no_overlap>250000')


HADHAD = Cut('hadhad == 1')
LEPHAD = Cut('lephad ==1')
TAU1_ETA = Cut('abs(tau1_eta) < 2.5')
TAU2_ETA = Cut('abs(tau2_eta) < 2.5')
TAU1_PT = Cut('tau1_pt > 15000.')
TAU2_PT = Cut('tau2_pt > 15000.')
MET = Cut('evtsel_MET > 20000.')

PRESELECTION = (
    HADHAD 
    & TAU1_ETA & TAU2_ETA
    & TAU1_PT & TAU2_PT
    & MET
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

# class Category_Preselection(Category):
#     name = 'preselection'
#     label = '#tau_{had}#tau_{had} Preselection'
#     common_cuts = PRESELECTION
 
