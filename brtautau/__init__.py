import logging
import os
import rootpy

DEFAULT_STUDENT = 'flat'
DEFAULT_TREE = 'Tree'
NTUPLE_PATH = 'ntuples'
UNMERGED_NTUPLE_PATH = '/cluster/data03/sbahrase/BrtStudies/PracticeDesk/TRUTH_LEVEL_BRT/flat_ntuples/running'

import ROOT

log = logging.getLogger('brtautau')
if not os.environ.get("DEBUG", False):
    log.setLevel(logging.INFO)
rootpy.log.setLevel(logging.INFO)

ROOT.gROOT.SetBatch(True)

ATLAS_LABEL = os.getenv('ATLAS_LABEL', 'Internal').strip()
