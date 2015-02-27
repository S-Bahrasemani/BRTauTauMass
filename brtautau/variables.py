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
        'bins': 100,
        'range': (50, 200)
        },
    'tau1_vis_pt': {
        'name': 'tau1_vis_pt',
        'root': 'Leading tau p_{T}',
        'type': 'f',
        'units': 'GeV',
        'scale': 0.001,
        'bins': 100,
        'range': (20, 120)
        },


    # 'dPhi_tau1_met': {},

    # 'dPhi_tau2_met': {},

    # 'dPhi_taus': {},

    # 'dPhi_taus_met': {},

    # 'dR_taus': {},

    # 'eta_product_jets': {},
    
    # 'mass_jet1_jet2': {},

    # 'mass_tau1_tau2_jet1': {},
    
    # 'met_et': {},

    # 'met_phi_centrality': {},

    # 'pt_ratio_tau1_tau2': {},

    # 'sum_pt_tau1_tau2': {},

    # 'sum_pt_tau1_tau2_met': {},

    # 'tau1_eta_centrality': {},

    # 'tau1_vis_eta': {},
    
    # 'tau1_vis_pt': {},

    # 'tau2_eta_centrality': {},

    # 'tau2_vis_eta': {},

    # 'tau2_vis_pt': {},

    # 'transverse_mass_tau1_met': {},

    # 'transverse_mass_tau1_tau2': {},

    # 'transverse_mass_tau2_met': {},

    # 'vector_sum_pt_tau1_tau2': {},

    # 'vector_sum_pt_tau1_tau2_met': {}
}




