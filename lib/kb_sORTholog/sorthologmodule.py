from __future__ import absolute_import

import os
import sys
import uuid
import logging
import json
import pandas as pd
from Bio import SeqIO
from .basemodule import BaseModule

warnings.filterwarnings("ignore")

logger = logging.getLogger(__name__)

class sORThologModule(BaseModule):
    def __init__(self,name,working_dir,module_dir,config):
        BaseModule.__init__(self,name,None,working_dir,config)
        self.module_dir = module_dir
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
    
    def run_sORTholog(self,params):
        #Initializes and preserves provenance information essential for functions that save objects to KBase
        self.initialize_call("run_sORTholog",params,True)
        #Function ensures required arguments are provided and optional arguments have default values
        params = self.validate_args(params,[],{
            "p_threshold":0.5,     # If the probability of an EC number is greater than or equal this threshold return the EC number.
            "proteins":None,
            "fasta_file":None,
            "file_output":True
        })
        output = {"annotation":{}}
        return output 