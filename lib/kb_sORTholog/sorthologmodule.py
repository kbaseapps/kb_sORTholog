from __future__ import absolute_import

import os
import sys
import uuid
import logging
import json
import pandas as pd
from Bio import SeqIO
from kbbasemodules.basemodule import BaseModule

logger = logging.getLogger(__name__)

class sORThologModule(BaseModule):
    def __init__(self,name,wsclient,anno_api,working_dir,module_dir,config):
        BaseModule.__init__(self,name,wsclient,working_dir,config)
        self.module_dir = module_dir
        self.anno_api = anno_api
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
    
    def run_sORTholog(self,params):
        #Initializes and preserves provenance information essential for functions that save objects to KBase
        self.initialize_call("run_sORTholog",params,True)
        #Function ensures required arguments are provided and optional arguments have default values
        params = self.validate_args(params,["genome_refs"],{})
        output = {"data":{}}
        return output 