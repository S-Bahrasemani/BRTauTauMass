import logging
import os

# rootpy/ROOT imports
import rootpy
from rootpy.extern.argparse import ArgumentParser
# setup the argument parser
parser = ArgumentParser()
parser.add_argument('--test_mode', type=str, default='VBF', choices=['VBF', 'gg', 'mix', 'Z'])
parser.add_argument('--test_level', type = str , default = 'reco', choices = ['truth', 'reco'])
parser.add_argument('--train_level', type = str , default = 'truth', choices = ['truth', 'reco'])
parser.add_argument('--train_id', type = str , default = '0000',)

parser.add_argument('--channel', type = str , default = 'hh', choices = ['hh','lh', 'll'])
parser.add_argument('--train_mode', type=str, default='VBF', choices=['VBF', 'gg', 'mix', 'Z'])
parser.add_argument('files', nargs='+', default=None)
args = parser.parse_args()

from datetime import date

my_datetime = date.today()
my_datetime = my_datetime.strftime("%m%d%Y")

MMC_VERSION = 1
MMC_MASS = "ditau_mmc_mlnu3p_m"#'mmc%d_resonance_m' % MMC_VERSION
MMC_PT = "ditau_mmc_mlnu3p_pt"#'mmc%d_resonance_pt' % MMC_VERSION
Coll_MASS = 'ditau_coll_approx_m'

DEFAULT_STUDENT = 'reco'
DEFAULT_TREE = 'Tree'
NTUPLE_PATH = 'ntuples/'
UNMERGED_NTUPLE_PATH = '/cluster/data03/sbahrase/BrtStudies/PracticeDesk/TRUTH_LEVEL_BRT/flat_ntuples/running'

import ROOT

log = logging.getLogger('brtautau')
if not os.environ.get("DEBUG", False):
    log.setLevel(logging.INFO)
rootpy.log.setLevel(logging.INFO)

ROOT.gROOT.SetBatch(True)

ATLAS_LABEL = os.getenv('ATLAS_LABEL', 'Internal').strip()
