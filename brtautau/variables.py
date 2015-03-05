import math
def get_label(variable):
    label = variable['root']
    if 'units' in variable.keys():
        label += ' [{0}]'.format(variable['units'])
    return label


VARIABLES = {
    'higgs_m': {
        'name': 'higgs_m',
        'root': 'm_{H}',
        'type': 'f',
        'units': 'GeV',
        'scale': 0.001,
        'bins': 30,
        'range': (50, 200)
        },
 
    'tau1_vis_pt': {
        'name': 'tau1_vis_pt',
        'root': 'Leading tau p_{T}',
        'type': 'f',
        'units': 'GeV',
        'scale': 0.001,
        'bins': 20,
        'range': (20, 120)
        },

    'tau2_vis_pt': {
        'name': 'tau2_vis_pt',
        'root': 'Subleading tau p_{T}',
        'type': 'f',
        'units': 'GeV',
        'scale': 0.001,
        'bins': 20,
        'range': (20, 120)
        },

    'pt_diff_tau1_tau2': {

       'name': 'pt_diff_tau1_tau2',
        'root': '#Delta P_{T} (#tau1, #tau2)',
        'type': 'f',
        'bins': 20,
        'range': (0., 1.2)
        },

    'tau1_vis_eta': {
        'name': 'tau1_vis_eta',
        'root': 'Leading tau #eta',
        'type': 'f',
        'bins': 20,
        'range': (-2.5, 2.5)
        },

    'tau2_vis_eta': {
        'name': 'tau2_vis_eta',
        'root': 'Subleading tau #eta',
        'type': 'f',
        'bins': 20,
        'range': (-2.5, 2.5)
        },
 
    'dPhi_tau1_met': {
        'name': 'dPhi_tau1_met', 
        'root': '#Delta #phi(Leading #tau, MET)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'dPhi_tau2_met': {
        'name': 'dPhi_tau2_met', 
        'root': '#Delta #phi(Subleading #tau, MET)',
        'type': 'f',
        'units' : 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'dPhi_taus': {
        'name': 'dPhi_taus', 
        'root': '#Delta #phi (#tau, #tau)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'dPhi_taus_met': {
        'name': 'dPhi_taus_met', 
        'root': '#Delta #phi (#tau  #tau, MET)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'dR_taus': {
        'name': 'dR_taus',
        'root': '#Delta R(#tau, #tau)',
        'type': 'f',
        'bins': 20,
        'range': (0, 4)
        },
 
    'eta_product_jets': {
        'name': 'eta_product_jets', 
        'root': '#eta_{jet_{1}} #times #eta_{jet_{2}}',
        'type': 'f',
        'bins': 20,
        'range': (-20. , 20. )
        },



    'mass_jet1_jet2': {
        'name': 'mass_jet1_jet2', 
        'root': 'm_{jj}',
        'type': 'f',
        'units': 'GeV',
        'scale' : 0.001,
        'bins': 30,
        'range': (0. , 2000. )
        },


    'mass_tau1_tau2_jet1': {
        'name': 'mass_tau1_tau2_jet1' ,
        'root': 'm_{#tau #tau j}',
        'type': 'f',
        'units': 'GeV',
        'scale': 0.001, 
        'bins': 30,
        'range': (0. , 1200.)
        },

     
    'met_et': {    
        'name': 'met_et' ,
        'root': 'E_{T}',
        'type': 'f',
        'units': 'GeV',
        'scale': 0.001, 
        'bins': 50,
        'range': (0. , 1000.)
        },



    'met_phi_centrality': {    
        'name': 'met_phi_centrality', 
        'root': 'MET_phi_centrality',
        'type': 'f',
        'bins': 20,
        'range': (-3. , 3.)
        },



    'pt_ratio_tau1_tau2': {
        'name': 'pt_ratio_tau1_tau2' ,
        'root': 'P^{T}_{#tau 1} / P^{T}_{#tau 2} ',
        'type': 'f',
        'bins': 20,
        'range': (0. , 30)
        },

    
    'sum_pt_tau1_tau2': {
       'name': 'sum_pt_tau1_tau2' ,
        'root': 'P^{T Sum}_{#tau #tau}',
        'type': 'f',
       'units' : 'GeV',
       'scale': 0.001,
        'bins': 40,
        'range': (0. , 1000.)
        },

    'sum_pt_tau1_tau2_met': {
        'name': 'sum_pt_tau1_tau2' ,
        'root': 'Pt^{sum}_{#tau #tau, MET}',
        'type': 'f',
        'units' : 'GeV',
        'scale': 0.001,
        'bins': 40,
        'range': (0. , 1000.)
        },


    'tau1_eta_centrality': {
       'name': 'tau1_eta_centrality' ,
        'root': '#tau 1 #eta -Centrality',
        'type': 'f',
        'bins':20,  
        'range': (0. , 1.5)
        },

    'tau1_eta_centrality': {
        'name': 'tau2_eta_centrality' ,
        'root': '#tau 2 #eta -Centrality',
        'type': 'f',
        'bins':20,  
        'range': (0. , 1.5)
        },


    'transverse_mass_tau1_met': {
        'name': 'transverse_mass_tau1_met' ,
        'root': 'm^{T}_{#tau1 MET}',
        'type': 'f',
        'units' : 'GeV',
        'scale': 0.001,
        'bins': 50,
        'range': (0. , 1000.)
        },

    'transverse_mass_tau2_met': {
        'name': 'transverse_mass_tau1_met' ,
        'root': 'm^{T}_{#tau_{2} MET}',
        'type': 'f',
        'units' : 'GeV',
        'scale': 0.001,
        'bins': 50,
        'range': (0. , 1000.)
        },



    'transverse_mass_tau1_tau2': {
        'name': 'transverse_mass_tau1_tau2' ,
        'root': 'm^{T}_{#tau_{1} #tau_{2}}',
        'type': 'f',
        'units' : 'GeV',
        'scale': 0.001,
        'bins': 50,
        'range': (0. , 1000.)
        },

    'vector_sum_pt_tau1_tau2': {
        'name': 'vector_sum_pt_tau1_tau2',
        'root' : 'vector_sum_pt_tau1_tau2',
        'type': 'f',
        'units' : 'GeV',
        'scale': 0.001,
        'bins': 40,
        'range': (0. , 500.)
        },
        

    'vector_sum_pt_tau1_tau2_met': {
        'name': 'vector_sum_pt_tau1_tau2_met', 
        'root': 'vector_sum_pt_tau1_tau2_met',
        'type': 'f',
        'units' : 'GeV',
        'scale': 0.001,
        'bins': 40,
        'range': (0. , 700.)
        },

}




