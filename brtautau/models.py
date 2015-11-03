## general
import math
from ROOT import TLorentzVector
## rootpy
from rootpy.tree import TreeModel, FloatCol, IntCol, BoolCol, CharCol
from rootpy.vector import LorentzRotation, LorentzVector, Vector3, Vector2
from rootpy.extern.hep import pdg
from rootpy import log
## local
from flat import eventshapes
from flat.mass import collinearmass
from variables import *


ignore_warning = log['/ROOT.TVector3.PseudoRapidity'].ignore(
    '.*transvers momentum.*')

Vars = VARIABLES

def deltaPhi(phi1,phi2):
    dPhi=abs(phi1-phi2)
    while dPhi>math.pi:
        dPhi=dPhi-2*math.pi
    return abs(dPhi)

class EventModel(TreeModel):
    runnumber = IntCol()
    evtnumber = IntCol()
    weight = FloatCol()
    hadhad = IntCol() # 1 or 0
    lephad = IntCol() # 1 or 0
    leplep = IntCol() # 1 or 0
    
class FourMomentum(TreeModel):
    pt = FloatCol()
    p = FloatCol()
    et = FloatCol()
    e = FloatCol()
    eta = FloatCol(default=-1111)
    phi = FloatCol(default=-1111)
    m = FloatCol()

    p = FloatCol()
    px = FloatCol()
    py = FloatCol()
    pz = FloatCol()
    
    @classmethod
    def set(cls, this, other):
        if isinstance(other, TLorentzVector):
            vect = other
        else:
            vect = other.fourvect

        this.e = vect.E()
        this.m = vect.M()
        this.et = vect.Et()
                
        this.pt = vect.Pt()
        this.p = vect.P()
        this.px = vect.Px()
        this.py = vect.Py()
        this.pz = vect.Pz()
        
        with ignore_warning:
            this.phi = vect.Phi()
            this.eta = vect.Eta()

class TrueMet(FourMomentum):
    @classmethod
    def set(cls, this, MISS):
        FourMomentum.set(this, MISS)

class Met(TreeModel):
    et = FloatCol(default=-1111)
    phi = FloatCol(default=-1111)
    etx = FloatCol(default=-1111)
    ety = FloatCol(default=-1111)
    
    @classmethod
    def set(cls, this, other):
        this.et = other.Mod()
        this.phi = other.Phi()
        this.etx = other.X()
        this.ety = other.Y()

class TrueTau(FourMomentum + FourMomentum.prefix('full_')):
    nProng = IntCol(default=-1111)
    nPi0 = IntCol(default=-1111)
    charge = IntCol(default=-1111)
    flavor = CharCol()
    pdgId = IntCol(default=-1111)
    index = IntCol(default=-1111)
    
    # n_tracks = IntCol(default=-1111)
    # n_wide_tracks = IntCol(default= -1111)
    # jet_bdt_loose= IntCol(default=-1111)
    # jet_bdt_medium= IntCol(default=-1111)
    # jet_bdt_tight= IntCol(default=-1111)
    # jet_bdt_score = IntCol(default=-1111)
    # jet_bdt_eff_sf= IntCol(default=-1111)

    # ele_bdt_loose= IntCol(default=-1111)
    # ele_bdt_medium= IntCol(default=-1111)
    # ele_bdt_tight= IntCol(default=-1111)
    # ele_bdt_score = IntCol(default=-1111)
    # ele_bdt_eff_sf= IntCol(default=-1111)
  
    eta_centrality = FloatCol() 
    collinear_momentum_fraction= FloatCol() 

    @classmethod
    def set_full(cls, this, other):
        if isinstance(other, TLorentzVector):
            vect = other
        else:
            vect = other.fourvect
        this.full_pt = vect.Pt()
        this.full_p = vect.P()
        this.full_et = vect.Et()
        this.full_e = vect.E()
        this.full_m = vect.M()
        with ignore_warning:
            this.full_phi = vect.Phi()
            this.full_eta = vect.Eta()

class TrueTauBlock(TrueTau.prefix('ditau_tau0_') + TrueTau.prefix('ditau_tau1_') + TrueMet.prefix('met_')):
    
    ditau_dr = FloatCol()
    ditau_deta = FloatCol()
    ditau_dphi = FloatCol()    
    ditau_dpt = FloatCol()
    ditau_met_pz = FloatCol()
    met_et= FloatCol(default=-1111)
    ditau_scal_sum_pt= FloatCol(default=-1111)
    ditau_vect_sum_pt= FloatCol(default=-1111)
    ditau_mt_lep0_met= FloatCol(default=-1111)
    ditau_mt_lep1_met= FloatCol(default=-1111)
    ditau_mt= FloatCol(default=-1111)

    ditau_dpt= FloatCol(default=-1111)
    ditau_vis_mass= FloatCol(default=-1111)
    ditau_dphi= FloatCol(default=-1111)
    ditau_tau0_pt= FloatCol(default=-1111)
    ditau_tau1_pt= FloatCol(default=-1111)
    ditau_met_min_dphi= FloatCol(default=-1111)
    ditau_met_lep0_cos_dphi= FloatCol(default=-1111)
    ditau_met_lep1_cos_dphi= FloatCol(default=-1111)

    @classmethod 
    def set(cls, tree,event,MET, tau1, tau2, jet1=None, jet2=None):
        ## set the 4momenta of the tuas's visible decays
        TrueTau.set(tree.tau1, tau1)
        TrueTau.set(tree.tau2, tau2)
        TrueMet.set(tree.met, MET)
        tree.tau1.charge = event.true_tau_0_q
        tree.tau2.charge = event.true_tau_1_q
        
        ## di-tau kinematics
        tree.ditau_dphi = event.true_ditau_vis_dphi
        tree.ditau_deta = event.true_ditau_vis_deta
        tree.ditau_dr = event.true_ditau_vis_dr
        tree.ditau_dpt = tree.ditau_tau0_pt - tree.ditau_tau1_pt
        tree.ditau_pz = tree.true_ditau_tau1_pz + tree.true_ditau_tau0_pz + tree.true_met_pz
        tree.ditau_vect_sum_pt = event.true_ditau_vis_vect_sum_pt
        tree.ditau_scal_sum_pt = event.true_ditau_vis_scal_sum_pt
        
        ## it's actually dphi just to consistent with xTau --FixMe
        tree.ditau_met_lep0_cos_dphi = deltaPhi(tau1.Phi(), MET.Phi())
        tree.ditau_met_lep1_cos_dphi = deltaPhi(tau2.Phi(), MET.Phi())

        tree.ditau_vis_mass = event.true_ditau_vis_mass
        tree.ditau_met_min_dphi = min (deltaPhi(tau1.Phi(), MET.Phi()), deltaPhi(tau2.Phi(), MET.Phi())) 
    
        tree.ditau_mt_lep0_met = math.sqrt((2* tree.ditau_tau0_pt * tree.met_et) * (1- math.cos(tree.ditau_met_lep0_cos_dphi)))
        tree.ditau_mt_lep1_met = math.sqrt((2* tree.ditau_tau1_pt * tree.met_et) * (1- math.cos(tree.ditau_met_lep1_cos_dphi)))
        tree.ditau_mt          = math.sqrt((2* tree.ditau_tau0_pt * tree.ditau_tau1_pt) * (1- math.cos(tree.ditau_dphi)))
        tree.hadhad = 1
        
class TrueJet(FourMomentum):
    index = IntCol(default = -1)
    # jvf = FloatCol()
    # mvx = FloatCol()
    # jvt = FloatCol()
    # mvx_sf = FloatCol()
    # mvx_ineff_sf = FloatCol()
    # jvfloose = FloatCol()

class TrueJetBlock(TrueJet.prefix('jet1_') + TrueJet.prefix('jet2_')):
    
    dEta_jets = FloatCol(default = -9999)
    eta_product_jets = FloatCol(default = -9999)
    eta_product_jets_boosted = FloatCol(default = -9999)
    mass_jet1_jet2 = FloatCol(default = -9999) 
     
    jet_beta = Vector3
    numJets = IntCol(default=-1111)
    #nonisolatedjet=IntCol()
    #num_true_jets_no_overlap =IntCol()


    @classmethod 
    def set(cls, tree,event, jet1, jet2):
        if jet1 is not None:
            FourMomentum.set(tree.jet1, jet1)

        if jet2 is not None:
            FourMomentum.set(tree.jet2, jet2)
            
            tree.dEta_jets = abs(jet1.Eta() - jet2.Eta())
            tree.eta_product_jets = jet1.Eta() * jet2.Eta()
            #tree.eta_product_jets_boosted = (jet1.fourvect_boosted.Eta() * jet2.fourvect_boosted.Eta())
            tree.mass_jet1_jet2 = (jet1 + jet2).M()


def get_model():
    model = EventModel + TrueTauBlock + FourMomentum.prefix('parent_') + TrueJetBlock
    return model
