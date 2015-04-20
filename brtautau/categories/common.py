from rootpy.tree import Cut
from math import pi

from .base import Category
from .. import MMC_MASS
from .. import Coll_MASS
# All basic cut definitions are here

TAU1_MEDIUM = Cut('tau1_JetBDTSigMedium==1')
TAU2_MEDIUM = Cut('tau2_JetBDTSigMedium==1')
TAU1_TIGHT = Cut('tau1_JetBDTSigTight==1')
TAU2_TIGHT = Cut('tau2_JetBDTSigTight==1')

ID_MEDIUM = TAU1_MEDIUM & TAU2_MEDIUM
ID_TIGHT = TAU1_TIGHT & TAU2_TIGHT
ID_MEDIUM_TIGHT = (TAU1_MEDIUM & TAU2_TIGHT) | (TAU1_TIGHT & TAU2_MEDIUM)


## LEPHAD basic cut definitions, tau1 is hadronic and tau2 is lepton 

TAU1_Positive = Cut('tau1_charge ==1')
TAU1_Negative = Cut('tau1_charge ==-1')
TAU2_Positive = Cut('tau2_charge ==1')
TAU2_Negative = Cut('tau2_charge ==-1')

TAU2_ISO_LEP = Cut('tau2_is_isolated_lep ==1')
MT = Cut('tarnsverse_mass_tau1_tau2 < 70000')
TAU_BJET = Cut('is_tau_b_jet')

TAU_MEDIUM_LEP_ISO = TAU1_TIGHT & TAU2_ISO_LEP 

# ID cuts for control region where both taus are medium but not tight
ID_MEDIUM_NOT_TIGHT = (TAU1_MEDIUM & -TAU1_TIGHT) & (TAU2_MEDIUM & -TAU2_TIGHT)

TAU_SAME_VERTEX = Cut('tau_same_vertex')

LEAD_TAU_35 = Cut('tau1_pt > 35000')
SUBLEAD_TAU_25 = Cut('tau2_pt > 25000')

LEAD_JET_50 = Cut('jet1_pt > 50000')
SUBLEAD_JET_30 = Cut('jet2_pt > 30000')
AT_LEAST_1JET = Cut('jet1_pt > 30000')

CUTS_2J = LEAD_JET_50 & SUBLEAD_JET_30
CUTS_1J = LEAD_JET_50 & (- SUBLEAD_JET_30)
CUTS_0J = (- LEAD_JET_50)

MET = Cut('MET_et > 20000')
DR_TAUS = Cut('0.8 < dR_tau1_tau2 < 2.4')
DETA_TAUS = Cut('dEta_tau1_tau2 < 1.5')
DETA_TAUS_CR = Cut('dEta_tau1_tau2 > 1.5')
RESONANCE_PT = Cut('resonance_pt > 100000')

# use .format() to set centality value
MET_CENTRALITY = 'MET_bisecting || (dPhi_min_tau_MET < {0})'

# common preselection cuts
PRESELECTION = (
    LEAD_TAU_35 & SUBLEAD_TAU_25
    & ID_MEDIUM_TIGHT
    & MET
    & Cut('%s > 0' % MMC_MASS)
    & Cut('%s > 0' % Coll_MASS)
    & DR_TAUS
    & TAU_SAME_VERTEX
    )




PRESELECTION_LH = (
    

)



# VBF category cuts
CUTS_VBF = (
    CUTS_2J
    & DETA_TAUS
    )

CUTS_VBF_CR = (
    CUTS_2J
    & DETA_TAUS_CR
    )

# Boosted category cuts
CUTS_BOOSTED = (
    RESONANCE_PT
    & DETA_TAUS
    )

CUTS_BOOSTED_CR = (
    RESONANCE_PT
    & DETA_TAUS_CR
    )


class Category_Loose_Preselection(Category):
    name = 'loose_preselection'
    label = '#tau_{had}#tau_{had} Loose Preselection'
    common_cuts = (
        LEAD_TAU_35 & SUBLEAD_TAU_25
        & ID_MEDIUM)
    

class Category_Preselection_NO_MET_CENTRALITY(Category):
    name = 'preselection'
    label = '#tau_{had}#tau_{had} Preselection'
    common_cuts = PRESELECTION


class Category_Preselection(Category):
    name = 'preselection'
    label = '#tau_{had}#tau_{had} Preselection'
    common_cuts = (
        PRESELECTION
        & Cut(MET_CENTRALITY.format(pi / 4))
        )


class Category_Preselection_LH(Category):
    name = 'preselection'
    label = '#tau_{lep}#tau_{had} Preselection'

class Category_Preselection_DEta_Control(Category_Preselection):
    is_control = True
    name = 'preselection_deta_control'


class Category_1J_Inclusive(Category_Preselection):
    name = '1j_inclusive'
    label = '#tau_{had}#tau_{had} Inclusive 1-Jet'
    common_cuts = Category_Preselection.common_cuts
    cuts = AT_LEAST_1JET
    norm_category = Category_Preselection
