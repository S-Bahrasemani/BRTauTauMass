import math
def get_label(variable):
    label = variable['root']
    if 'units' in variable.keys():
        label += ' [{0}]'.format(variable['units'])
    return label


VARIABLES = {
    'resonance_m': {
        'name': 'resonance_m',
        'root': 'm_{H}',
        'type': 'f',
        'units': 'GeV',
        'scale': 0.001,
        'bins': 30,
        'range': (50, 200)
        },

    'mass_vis_tau1_tau2' : {
        'name': 'mass_vis_tau1_tau2',
        'root': 'm_{#tau #tau}',
        'type': 'f',
        'units': 'GeV',
        'scale': 0.001,
        'bins': 30,
        'range': (50, 200)
        },


    'mass_collinear_tau1_tau2' : {
        'name': 'mass_collinear_tau1_tau2',
        'root': 'm_{coll}',
        'type': 'f',
        'units': 'GeV',
        'scale': 0.001,
        'bins': 30,
        'range': (50, 200)
        },


    'tau1_pt': {
        'name': 'tau1_pt',
        'root': 'Leading tau p_{T}',
        'type': 'f',
        'units': 'GeV',
        'scale': 0.001,
        'bins': 20,
        'range': (20, 120)
        },

    'tau2_pt': {
        'name': 'tau2_pt',
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

    'tau1_eta': {
        'name': 'tau1_eta',
        'root': 'Leading tau #eta',
        'type': 'f',
        'bins': 20,
        'range': (-2.5, 2.5)
        },

    'tau2_eta': {
        'name': 'tau2_eta',
        'root': 'Subleading tau #eta',
        'type': 'f',
        'bins': 20,
        'range': (-2.5, 2.5)
        },
 
    'dPhi_tau1_MET': {
        'name': 'dPhi_tau1_MET', 
        'root': '#Delta #phi(Leading #tau, MET)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'dPhi_tau2_MET': {
        'name': 'dPhi_tau2_MET', 
        'root': '#Delta #phi(Subleading #tau, MET)',
        'type': 'f',
        'units' : 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'dPhi_tau1_tau2': {
        'name': 'dPhi_tau1_tau2', 
        'root': '#Delta #phi (#tau1, #tau2)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'dPhi_tau1_tau2_MET': {
        'name': 'dPhi_tau1_tau2_MET', 
        'root': '#Delta #phi (#tau1 #tau2, MET)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'dR_tau1_tau2': {
        'name': 'dR_tau1_tau2',
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

    'cos_theta_tau1_tau2': {
        'name': 'cos_theta_tau1_tau2',
        'root': '#cos(#theta)_{#tau1 #tau2}',
        'type':'f',
        'bins' : 20,
        'range' : (-1.2 , 1.2)
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

     
    'MET_et': {    
        'name': 'MET_et' ,
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



    'tau_pt_ratio': {
        'name': 'tau_pt_ratio' ,
        'root': 'P_{T #tau 1} / P^{T #tau 2} ',
        'type': 'f',
        'bins': 20,
        'range': (0. , 30)
        },

    
    'sum_pt_tau1_tau2': {
       'name': 'sum_pt_tau1_tau2' ,
        'root': 'P_{T} Sum (#tau1, #tau2)',
        'type': 'f',
       'units' : 'GeV',
       'scale': 0.001,
        'bins': 30,
        'range': (0. , 1000.)
        },

    'sum_pt_tau1_tau2_met': {
        'name': 'sum_pt_tau1_tau2_met' ,
        'root': 'P_{T} Sum (#tau1, #tau2, MET)',
        'type': 'f',
        'units' : 'GeV',
        'scale': 0.001,
        'bins': 30,
        'range': (0. , 1000.)
        },


    'tau1_eta_centrality': {
       'name': 'tau1_eta_centrality' ,
        'root': '#tau 1 #eta -Centrality',
        'type': 'f',
        'bins':20,  
        'range': (0. , 1.5)
        },

    'tau2_eta_centrality': {
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
        'name': 'transverse_mass_tau2_met' ,
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
        'root': 'vector_sum_pt_tau1_tau2_MET',
        'type': 'f',
        'units' : 'GeV',
        'scale': 0.001,
        'bins': 40,
        'range': (0. , 700.)
        },

    'sum_pt_full': {
        'name': 'sum_pt_full', 
        'root': 'Sum P_{T} Full',
        'type': 'f',
        'units' : 'GeV',
        'scale': 0.001,
        'bins': 30,
        'range': (0. , 1200.)
        },


    'vector_sum_pt_full': {
        'name': 'vector_sum_pt_full', 
        'root': 'Vector Sum P_{T} Full',
        'type': 'f',
        'units' : 'GeV',
        'scale': 0.001,
        'bins': 30,
        'range': (0. , 1200.)
        },

}




