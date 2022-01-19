#!/usr/bin/env python3

#IMPORTS
import sys
sys.path.append("/home/bschroed/Documents/projects/PyGromosTools")
from pygromos.simulations.hpc_queuing.job_scheduling.workers.analysis_workers.simulation_analysis import do

#VARIABLES: 
in_simulation_dir = "/home/bschroed/Documents/projects/PyGromosTools_release3/examples/example_files/Hvap_files/hvap/test_gas/1_emin/simulation/1_emin_1/example_files/Hvap_files/hvap/test_gas/1_emin/simulation"
out_analysis_dir = "/home/bschroed/Documents/projects/PyGromosTools_release3/examples/example_files/Hvap_files/hvap/test_gas/1_emin/simulation/1_emin_1/example_files/Hvap_files/hvap/test_gas/1_emin/analysis"
sim_prefix = "1_emin"
gromosPP_bin_dir = ""
n_processes = 1
control_dict = {
	"concat": {"do":True,
		"sub": {
			"cp_cnf": True,
			"repair_NaN": True,
			"cp_omd": True,
			"cat_trc": True,
			"cat_tre": True,
			"cat_trg": False,
			"convert_trcs": False,
			},
		 },
	"simulation_folder": {"do":True,
		"sub": {
			"tar": True,
			"remove": False,
			},
		 },
}
verbose = True



#DO
do(in_simulation_dir=in_simulation_dir, out_analysis_dir=out_analysis_dir, sim_prefix=sim_prefix, gromosPP_bin_dir=gromosPP_bin_dir, n_processes=n_processes, control_dict=control_dict, verbose=verbose, )
exit(0)


