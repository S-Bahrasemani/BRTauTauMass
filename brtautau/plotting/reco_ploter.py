
import os
#import logging
import math
import datetime
#import shutil

#log = logging.getLogger(os.path.basename(__file__))

import ROOT

gg_LumiList=[1454.0,1619.3,1819.7,2080.3,2433.2,3912.1,3673.1,4802.9,6144.4,9468.1,14716.7]
Boosted_LumiList=[18813.9,19981.9,21451.0,23629.9,26676.8,47773.8,37606.8,47633.5,58468.3,88671.4,135924.5]
Total_Lumi=20.3
data12LumiList = [47773.8]


nPoints= 30
meanGraphs=[ROOT.TGraphErrors(nPoints) for i in range(3)]
rmsGraphs=[ROOT.TGraphErrors(nPoints) for i in range(3)]
resGraphs=[ROOT.TGraphErrors(nPoints) for i in range(3)]
meanlegend=ROOT.TLegend(0.2,0.7,0.4,0.9)
reslegend=ROOT.TLegend(0.2,0.7,0.4,0.9)
meanMultiGraph=ROOT.TMultiGraph()
rmsMultiGraph=ROOT.TMultiGraph()
resMultiGraph=ROOT.TMultiGraph()

dist_label_1=ROOT.TLatex(0.2,0.85,"#splitline{H#rightarrow#tau_{had}#tau_{had} #bf{Boosted}}{}")
dist_label_1.SetNDC()
dist_label_2=ROOT.TLatex(0.65,0.6,"#splitline{#it{#bf{ATLAS}}}{Work in Progress}")
dist_label_2.SetNDC()
reco_vs_truth_label=ROOT.TLatex(0.55,0.25,'#splitline{H#rightarrow#tau_{had}#tau_{had} #bf{Boosted} }{#it{#bf{ATLAS}} Work in Progress}')
reco_vs_truth_label.SetNDC()
rms_label=ROOT.TLatex(0.2,0.8,"#splitline{H#rightarrow#tau_{had}#tau_{had} #bf{Boosted} }{#it{#bf{ATLAS}} Work in Progress}")
rms_label.SetNDC()
roc_label=ROOT.TLatex(0.2,0.45,"#splitline{H#rightarrow#tau_{had}#tau_{had} #bf{Boosted} }{#it{#bf{ATLAS}} Work in Progress}")
roc_label.SetNDC()
dist_label_2=ROOT.TLatex(0.65,0.6,"#splitline{#it{#bf{ATLAS}}}{Work in Progress}")
dist_label_2.SetNDC()
reco_vs_truth_label=ROOT.TLatex(0.55,0.25,"#splitline{H#rightarrow#tau_{had}#tau_{had} #bf{Boosted}}{#it{#bf{ATLAS}} Work in Progress}")
reco_vs_truth_label.SetNDC()
rms_label=ROOT.TLatex(0.2,0.8,"#splitline{H#rightarrow#tau_{had}#tau_{had} #bf{Boosted} }{#it{#bf{ATLAS}} Work in Progress}")
rms_label.SetNDC()
roc_label=ROOT.TLatex(0.2,0.45,"#splitline{H#rightarrow#tau_{had}#tau_{had} #bf{Boosted}}{#it{#bf{ATLAS}} Work in Progress}")
roc_label.SetNDC()


def draw_calib_curve(estimators_dict, mean_dict, meanerror_dict, rms_dict, rmserror_dict, masses='masses',
                     date='mydate', level='levels', mode='mode' ,channel= 'channel',train_id = 'id', *args, **kwargs):
    

    npoints = 30
    nBins = 30
    colors = [4, 3,2]
    names = ["brt_h_hist", "mmc_h_hist", "mosaic_h_hist"]
    legends =['BRT mass', 'MMC mass', 'Mosaic mass']
       
    canvas = ROOT.TCanvas()
    canvas.SetFillColor(18)
   
    for mass in masses:
        Hstack=ROOT.THStack()
        Hlegend=ROOT.TLegend(0.75,0.75,0.95,0.95)
        for i, color, name, legend in zip (range(3), colors, names, legends):
            estimators_dict[mass][i].SetLineColor(color)
            estimators_dict[mass][i].SetFillColor(color)
            estimators_dict[mass][i].SetFillStyle("/")
            estimators_dict[mass][i].SetLineWidth(1)

            Hstack.Add(estimators_dict[mass][i])#.Rebin(npoints/nBins,name))
            Hlegend.AddEntry(estimators_dict[mass][i],legend,'l')
        Hstack.Draw("NOSTACK HIST")
        Hlegend.Draw()                
        Hstack.SetTitle('Reconstructed H('+str(mass)+') Mass Distribution')
        Hstack.GetXaxis().SetTitle('Reconstructed H({0}) Mass (GeV)'.format(mass))
        Hstack.GetYaxis().SetTitle('Events / 5 GeV')
        canvas.SaveAs('./plots/'+str(channel)+'/reco/'+str(train_id)+'-H_Mass_'+str(mass)+'_{0}_{1}.png'.format(mode, channel))
        canvas.Clear()
    
    for i, color, legend in zip (range(3), colors, legends):
        meanGraphs[i].SetMarkerColor(color)
        meanGraphs[i].SetLineColor(color)
        meanGraphs[i].SetLineWidth(3)
        meanGraphs[i].SetMarkerStyle(21)
        
        rmsGraphs[i].SetMarkerStyle(8)
        rmsGraphs[i].SetMarkerColor(color)
        resGraphs[i].SetMarkerColor(color)
        resGraphs[i].SetMarkerStyle(8)
        
        meanlegend.AddEntry(meanGraphs[i],legend,'P')
        reslegend.AddEntry(resGraphs[i],legend,'P')
        
    for p, mass in zip (range(len(masses)), masses):
        for i, offset in zip (range(3), [0,1, -1]):
            meanGraphs[i].SetPoint(p, float (mass+offset), mean_dict[mass][i])
            meanGraphs[i].SetPointError(p, 0, rms_dict[mass][i])
            rmsGraphs[i].SetPoint(p,mass, rms_dict[mass][i])
            rmsGraphs[i].SetPointError(p,0, rmserror_dict[mass][i])
            resGraphs[i].SetPoint(p,mass, rms_dict[mass][i]/float(mass))
            resGraphs[i].SetPointError(p,0,math.sqrt(pow(rmserror_dict[mass][i]/mean_dict[mass][i],2)+pow(rms_dict[mass][i]/(mean_dict[mass][i]*mean_dict[mass][i])*meanerror_dict[mass][i],2)))

            meanMultiGraph.Add(meanGraphs[i])
            rmsMultiGraph.Add(rmsGraphs[i])
            resMultiGraph.Add(resGraphs[i])
                
    
    graphs = ["meanMultiGraph", "rmsMultiGraph", 'resMultiGraph']
    titles = ['Reconstructed Mass vs. Truth Mass', 'Reconstructed Mass RMS vs. Truth Mass', 'Reconstructed Mass Resolution vs. Truth Mass']
    xtitle = 'Truth Mass (GeV)'
    ytitles= ['Reconstructed Mass (GeV)', 'Reco Mass RMS (GeV)', 'Reco Mass Resolution']
    legends= [meanlegend, Hlegend, Hlegend]
    labels = [reco_vs_truth_label, rms_label, rms_label]
    for graph,label,  title, ytitle , legend in zip(graphs,labels, titles, ytitles, legends):
        
        if graph=="meanMultiGraph":
            meanMultiGraph.Draw('AP')
            legend.Draw('same')
            legend.SetTextSize(0.0375)
            label.Draw('same')
            print meanMultiGraph.GetXaxis().GetXmin(), meanMultiGraph.GetXaxis().GetXmax()
            line = ROOT.TLine(90,90, 160, 160)
            line.SetLineWidth(3)
            meanlegend.AddEntry(line,"m_{Reco} = m_{True}",'L')
            line.Draw('same')

            meanMultiGraph.GetXaxis().SetTitle(xtitle)
            meanMultiGraph.GetYaxis().SetTitle(ytitle)
            meanMultiGraph.GetXaxis().SetLimits(70, 190)
            meanMultiGraph.SetMinimum(70)
            meanMultiGraph.SetMaximum(190)
            canvas.SaveAs('./plots/'+str(channel)+'/reco/{0}-{1}_{2}_mean_vs_true_mass.png'.format(train_id, level, mode))
            canvas.Clear()
            
        elif graph == "rmsMultiGraph":   
            rmsMultiGraph.Draw('AP')
            legend.Draw('same')
            legend.SetTextSize(0.0375)
            label.Draw('same')
            rmsMultiGraph.GetXaxis().SetTitle(xtitle)
            rmsMultiGraph.GetYaxis().SetTitle(ytitle)
            rmsMultiGraph.GetXaxis().SetLimits(masses[0]-10, masses[-1] + 10)
            rmsMultiGraph.SetMinimum(0.)
            rmsMultiGraph.SetMaximum(50.)    
            canvas.SaveAs('./plots/'+str(channel)+'/reco/{0}-{1}_{2}_rms_vs_true_mass.png'.format(train_id, level, mode))
            canvas.Clear()
        else:
            resMultiGraph.Draw('AP')
            legend.Draw('same')
            legend.SetTextSize(0.0375)
            label.Draw('same')
            resMultiGraph.GetXaxis().SetTitle(xtitle)
            resMultiGraph.GetYaxis().SetTitle(ytitle)
            resMultiGraph.GetXaxis().SetLimits(masses[0]-10, masses[-1] + 10)
            resMultiGraph.SetMinimum(0.)
            resMultiGraph.SetMaximum(0.5)
            canvas.SaveAs('./plots/'+str(channel)+'/reco/{0}-{1}_{2}_res_vs_true_mass.png'.format(train_id, level, mode))
            canvas.Clear()

def draw_mass_lineshapes(H_Hists = 'Normalized H Hists Dictionary', Z_Hist = 'Z hists', channel ='channel', mode ='mode',date ='date',train_id = 'id',H_Pt = 'h pt', **kwargs):
    
    #### Draw Z Hists
    npoints = 100
    nBins = 100
    colors = [2, 3, 4]
    names = ["BRT", "MMC", 'MOSAIC']
    legends =['BRT: ', 'MMC: ', 'Mosaic: ']

    canvas = ROOT.TCanvas()
    canvas.SetFillColor(18)
    #canvas.SetGrid()

    Zstack=ROOT.THStack()
    Zlegend=ROOT.TLegend(0.65,0.75,0.95,0.95)

    for i, color, name, legend in zip (range(3), colors, names, legends):
        Z_Hist[i].SetLineColor(color)
        Z_Hist[i].SetFillColor(color)
        Z_Hist[i].SetFillStyle("/")
        
        Z_Hist[i].SetLineWidth(1)
        Zstack.Add(Z_Hist[i])#.Rebin(npoints/nBins,name))
        Zlegend.AddEntry(Z_Hist[i], legend + "Mean = %.2f, RMS=%.2f" % (Z_Hist[i].GetMean(), Z_Hist[i].GetRMS()),'l')
        
    Zstack.Draw("NOSTACK HIST")
    Zlegend.Draw()
    Zstack.SetTitle('Reconstructed Z Mass Distribution')
    Zstack.GetXaxis().SetTitle('Reconstructed Z Mass (GeV)')
    Zstack.GetYaxis().SetTitle('Events / 5 GeV')
    canvas.SaveAs('./plots/'+str(channel)+'/reco/'+str(train_id)+'-Z_Mass_{0}_{1}.png'.format(mode, channel))
    canvas.Clear()

    ### Draw  Z - H125 Mass plots
    H125_Hist = H_Hists[125]

    canvas = ROOT.TCanvas()
    canvas.SetFillColor(18)
    
    for i, color, name, tag in zip (range(3), colors, names, ['BRT', 'MMC', 'Mosaic']):  
        ZHstack=ROOT.THStack()
        Zlegend=ROOT.TLegend(0.70,0.80,0.95,0.90)
        Zlegend.SetFillColor(38)
        Z_Hist[i].SetLineColor(color)
        Z_Hist[i].SetFillColor(color)
        Z_Hist[i].SetFillStyle("/")
        
        H125_Hist[i].SetLineColor(color+1)
        H125_Hist[i].SetFillColor(color+1)
        H125_Hist[i].SetFillStyle("/")
        
        Zlegend.AddEntry(Z_Hist[i], name + ": Z-Mean = %.2f, Z-RMS=%.2f" % (Z_Hist[i].GetMean(), Z_Hist[i].GetRMS()),'l')
        Zlegend.AddEntry(H125_Hist[i],name+ ": H-Mean = %.2f, H-RMS=%.2f" % (H125_Hist[i].GetMean(), H125_Hist[i].GetRMS()),'l')
        
        ZHstack.Add(Z_Hist[i])#.Rebin(npoints/nBins,name))
        ZHstack.Add(H125_Hist[i])#.Rebin(npoints/nBins,name))

        ZHstack.Draw("NOSTACK HIST")
        Zlegend.Draw()
        ZHstack.SetTitle('Reconstructed H125 - Z  Mass Distribution')
        ZHstack.GetXaxis().SetTitle('Reconstructed Z-H125 Mass (GeV)')
        ZHstack.GetYaxis().SetTitle('Events / 5 GeV')
        lat = ROOT.TLatex(0.2, 0.8, "Truth matched")
        #lat0 = ROOT.TLatex(0.2, 0.7, "TauID: M-T")
        lat1 = ROOT.TLatex(0.2, 0.73, "H_{pt} > %i" % H_Pt)
        lat.SetNDC(True)
        lat.Draw()
       # lat0.SetNDC(True)
       # lat0.Draw()
        
        lat1.SetNDC(True)
        lat1.Draw()
        canvas.SaveAs('./plots/'+str(channel)+'/reco/'+str(train_id)+'-{2}_H125-Z_Mass_{0}_{1}_{3}.png'.format(mode, channel, tag, H_Pt))
        canvas.Clear()
#========== Z vs. H125 ROC ==========

def roccurve(hist1,hist2):
    nBins=hist1.GetNbinsX()
    if not(nBins==hist2.GetNbinsX()):
        raise Exception ("Error, uneven histogram bin numbers.")

    hist1_temp=hist1.Clone('hist1')
    hist2_temp=hist2.Clone('hist2')
    hist1_temp.Scale(1./hist1_temp.Integral())
    hist2_temp.Scale(1./hist2_temp.Integral())
    roc_curve =ROOT.TGraph(nBins+2)
    hist1_passing=1.
    hist2_passing=1.

    for i in xrange(nBins+2):
        roc_curve.SetPoint(i,hist1_passing,1.-hist2_passing)
        hist1_passing-=hist1_temp.GetBinContent(i)
        hist2_passing-=hist2_temp.GetBinContent(i)    
    return roc_curve

def draw_roc_curve (H1= 'Hist one hists list ', H2 ='Hist two hists list', H1_tag = 'Higgs or Z', H2_tag = 'Higgs or Z', H1_mass = 'Higgs mass',
                    H2_mass =' Higgs or Z mass', channel ='channel', mode ='mode',date ='date', train_id = 'id', H_Pt = 'h pt'):

    roc_curves_H1_H2=[roccurve(H1[i],H2[i]) for i in range(3)]   
    roc_legend=ROOT.TLegend(0.2,0.2,0.4,0.4)
    roc_label=ROOT.TLatex(0.2,0.45,"#splitline{H #rightarrow#tau_{h}#tau_{h} }{#it{#bf{ATLAS}} Work in Progress}")
    roc_label.SetNDC()
    c1 = ROOT.TCanvas()
    c1.SetFillColor(18)
        #c1.SetGrid()
    colors =[2, 4, 6]
    labels = ['BRT', 'MMC', 'Mosaic']
    
    for n, color, label in zip(range(3), colors, labels ):
        
        #roc_curves_H1_H2[n].SetLineWidth(2)
        roc_curves_H1_H2[n].SetMarkerSize(1.7)
        roc_curves_H1_H2[n].SetLineWidth(3)
        roc_curves_H1_H2[n].SetLineColor(color)
        roc_curves_H1_H2[n].SetMarkerStyle(18)
        roc_curves_H1_H2[n].SetMarkerColor(color)
        roc_legend.AddEntry(roc_curves_H1_H2[n],label, 'P')
            
        for i in range(3):
            if i==0:      
                roc_curves_H1_H2[i].Draw('APL')
                roc_curves_H1_H2[i].GetXaxis().SetRangeUser(0.,1.)
                roc_curves_H1_H2[i].GetYaxis().SetRangeUser(0.,1.)
                roc_curves_H1_H2[i].SetTitle('{0}({1}) vs {2}({3}) ROC Curve'.format(H1_tag, H1_mass, H2_tag, H2_mass))
                roc_curves_H1_H2[i].GetXaxis().SetTitle('{0}({1}) Acceptance'.format(H2_tag, H2_mass))
                roc_curves_H1_H2[i].GetYaxis().SetTitle('{0}({1}) Rejection'.format(H1_tag, H1_mass))
          
            elif i == 1:
                roc_curves_H1_H2[i].Draw('PL')
                c1.Update()
                roc_legend.Draw('same')
                roc_label.Draw('same')
            else:
                roc_curves_H1_H2[i].Draw('PL')
                c1.Update()
                roc_legend.Draw('same')
                roc_label.Draw('same')
          
    lat = ROOT.TLatex(0.2, 0.8, "Truth matched")
    #lat0 = ROOT.TLatex(0.2, 0.7, "TauID: M-T")
    lat1 = ROOT.TLatex(0.2, 0.73, "H_{pt} > %i" % H_Pt)
    lat.SetNDC(True)
    lat.Draw()
    #lat0.SetNDC(True)
    #lat0.Draw()
     
    lat1.SetNDC(True)
    lat1.Draw()
 
    c1.SaveAs('./plots/{0}/reco/{1}-roc_{H1_tag}{H1_mass}_{H2_tag}{H2_mass}_{2}_{0}_{3}.png'
              .format(channel,train_id, mode,H_Pt, H1_tag = H1_tag, H1_mass = H1_mass, H2_tag = H2_tag, H2_mass = H2_mass))
    c1.Clear()
