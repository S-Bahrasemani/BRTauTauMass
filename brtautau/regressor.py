# python imports
import os
# ROOT/rootpy
import ROOT
from ROOT import TMVA
from rootpy.io import root_open
from rootpy.tree import Cut
from datetime import datetime
# local imports

from .variables import VARIABLES
from samples import Higgs
from samples.db import get_file
from . import *
relative_path = "TrainingBRT"

class Regressor(TMVA.Factory):
    """
    """
    def __init__(self,
                 output_name,
                 features,
                 factory_name='TMVARegression',
                 verbose='V:!Silent:Color:DrawProgressBar',
                 ):

        self.output = root_open(output_name, 'recreate')

        TMVA.Factory.__init__(
            self, factory_name, self.output, verbose)
        self.factory_name = factory_name
        self.features = features

    def set_variables(self):
        """
        Set TMVA formated variables
        from the VARIABLES dict (see variables.py)
        """
        for varName in self.features:
            var = VARIABLES[varName]
            self.AddVariable(
                var['name'], 
                var['root'], 
                var['units'] if 'units' in var.keys() else '',
                var['type'])

    def book_brt(self,
                 ntrees=200,#80
                 node_size=0.2,#0.2
                 depth=16):#8
        """
        Book the BRT method (set all the parameters)
        """
        params = ["SeparationType=RegressionVariance"]
        params += ["BoostType=AdaBoost"]
        params += ["AdaBoostBeta=0.2"] # 0.2
        params += ["MaxDepth={0}".format(depth)]
        params += ["MinNodeSize={0}%".format(node_size)]
        params += ["NTrees={0}".format(ntrees)]
        # Do we need those or not ?
        # params += ["PruneMethod=NoPruning"]
        # params += ["UseYesNoLeaf=False"]
        # params += ["DoBoostMonitor"]
        # params += ["nCuts={0}".format(nCuts)]
        # params += ["NNodesMax={0}".format(NNodesMax)]
        # DEPRECATED DEPRECATED
        # params += ["nEventsMin={0}".format(nEventsMin)]
        log.info(params)
        method_name =   "BRT_HiggsMass-" + str(my_datetime)+'_' + str(args.train_level)+'_' +str(args.train_mode)+'_'+ str(args.channel) 
        params_string = "!H:V"
        for param in params:
            params_string+= ":"+param
        self.BookMethod(
            TMVA.Types.kBDT,
            method_name,
            params_string)


        

    def train(self, mode='gg',level='reco', **kwargs):
        """
        Run, Run !
        """
        log.info("Training BRT")
        self.set_variables()
        training_samples = []

        if args.train_mode == 'Z':
            z_array= Higgs(tree_name= 'Tree', mode=args.train_mode, level=level, masses=[90], suffix='_train')
            training_samples.append(z_array.components)
            training_samples= sum(training_samples, [])
        elif args.train_mode == 'mix':
            higgs_array_gg=  Higgs(tree_name= 'Tree', mode="gg", level=level, masses=Higgs.MASSES, suffix='_train')
            higgs_array_vbf= Higgs(tree_name= 'Tree', mode="VBF", level=level, masses=Higgs.MASSES, suffix='_train')
            training_samples.append(higgs_array_gg.components)
            training_samples.append(higgs_array_vbf.components)
            training_samples= sum(training_samples, [])

        else:    
            higgs_array=  Higgs(tree_name= 'Tree', mode=args.train_mode, level=level, masses=Higgs.MASSES, suffix='_train')
            training_samples.append(higgs_array.components)
            training_samples= sum(training_samples, [])

        params = ['nTrain_Regression=0']
        params += ['nTest_Regression=1']
        #params = ['SplitMode=Random']
        params += ['NormMode=NumEvents']
        params += ['!V']
        params = ':'.join(params)
      
     
        masses =  []
        for s in training_samples:
            rfile = get_file(ntuple_path=s.ntuple_path+ relative_path, file_name = None,
                             student=s.student, hdf=False, suffix='_train' , force_reopen=False)
            tree = rfile[s.tree_name]
            n = tree.GetEntries()
            masses.append(n)
            ## weight input samples
            self.AddRegressionTree(tree, 1./n)

        #### be careful preselection cuts must be applied after adding regression trees        
        cut = Cut("ditau_tau1_matched_isHadTau==1") & Cut("ditau_tau0_matched_isHadTau==1")
        self.PrepareTrainingAndTestTree(cut, params)
        self.AddRegressionTarget('parent_m')
        # Could reweight samples 
        # self.AddWeightExpression("my_expression")

        # Actual training
        self.book_brt(**kwargs)
        self.TrainAllMethods()
     
        ## draw sample distribution curve
        # mass_dists = ROOT.TGraph(len(masses))
        # canvas = ROOT.TCanvas()
        # canvas.SetFillStyle(18)
        # i = 0
        # m = 60
        # masses = [0.001 * x for x in masses]
        # for n in masses:
        #     mass_dists.SetPoint (i, m , n)
        #     i += 1
        #     m += 5
        # mass_dists.Draw("ALP")
        # mass_dists.GetXaxis().SetTitle("Mass (%s ) " % args.train_mode)
        # mass_dists.GetYaxis().SetTitle("# of events(/k)")
        # mass_dists.GetXaxis().SetLimits(40, 220)
        # mass_dists.GetYaxis().SetLimits(0, 20)

        # mass_dists.SetMarkerColor(2)
        # mass_dists.SetLineColor(4)
        # mass_dists.SetLineWidth(3)
        # mass_dists.SetMarkerStyle(20)
        
        # canvas.SaveAs("./plots/input_samples_distribution_%s.png"% args.train_mode)
        # canvas.Clear()
