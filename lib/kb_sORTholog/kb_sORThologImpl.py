# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
import sys
sys.path.append("/deps/KBBaseModules/")
import sys
import json
from os.path import exists
from installed_clients.KBaseReportClient import KBaseReport
from installed_clients.WorkspaceClient import Workspace
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.cb_annotation_ontology_apiClient import cb_annotation_ontology_api
from kb_sORTholog.sorthologmodule import sORThologModule
#END_HEADER


class kb_sORTholog:
    '''
    Module Name:
    kb_sORTholog

    Module Description:
    A KBase module: kb_sORTholog
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    def save_report_to_kbase(self,output):
        report_shock_id = self.dfu.file_to_shock({'file_path': output["file_path"],'pack': 'zip'})['shock_id']
        output["report_params"]["html_links"][0]["shock_id"] = report_shock_id
        repout = self.kbreport.create_extended_report(output["report_params"])
        return {"report_name":output["report_params"]["report_object_name"],"report_ref":repout["ref"],'workspace_name':self.api.ws_name}
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config["version"] = self.VERSION
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.token = os.environ['KB_AUTH_TOKEN']
        self.wsclient = Workspace(self.config["workspace-url"], token=self.token)
        self.kbreport = KBaseReport(self.callback_url,token=self.token)
        self.anno_api = cb_annotation_ontology_api(self.callback_url,token=self.token)
        self.dfu = DataFileUtil(self.callback_url,token=self.token)
        self.api = sORThologModule("kb_sORTholog",self.wsclient,self.anno_api,config['scratch'],self.config)
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def run_sORTholog(self, ctx, input):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param input: instance of type "RunSORThologParams" -> structure:
           parameter "genomes" of list of type "genome_ref" (Reference to a
           Pangenome object in the workspace @id ws KBaseGenomes.Genome
           KBaseSearch.GenomeSet)
        :returns: instance of type "ReportResults" -> structure: parameter
           "output_workspace" of String, parameter "report_name" of String,
           parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_sORTholog
        api_output = self.api.PDBAnnotation(params)            
        output = self.save_report_to_kbase(api_output,)
        self.api.transfer_outputs(output,api_output,["data"])
        #END run_sORTholog

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_sORTholog return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
