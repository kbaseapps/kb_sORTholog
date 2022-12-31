/*
A KBase module: kb_sORTholog
*/

module kb_sORTholog {
    /*
    	Reference to a Pangenome object in the workspace
    	@id ws KBaseGenomes.Genome KBaseSearch.GenomeSet
    */
    typedef string genome_ref;
    
    typedef structure {
    	int workspace_id;
    	string workspace_name;
        list<genome_ref> genome_refs;
    } RunSORThologParams;
    
    typedef structure {
        string output_workspace;
        string report_name;
        string report_ref;
    } ReportResults;
    
    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_sORTholog(RunSORThologParams input) returns (ReportResults output) authentication required;

};
