#!/usr/bin/env python3

#IMPORTS
import sys
sys.path.append("/home/bschroed/Documents/projects/PyGromosTools")
from pygromos.simulations.hpc_queuing.job_scheduling.schedulers.simulation_scheduler import do

#VARIABLES: 
#Generate Gromos_System
from pygromos.files.gromos_system.gromos_system import Gromos_System as Gromos_System_obj
in_simSystem = Gromos_System_obj(work_folder="/home/bschroed/Documents/projects/PyGromosTools_release3/examples/example_files/Hvap_files/hvap/test_gas/1_emin/simulation/1_emin_1/example_files/Hvap_files/hvap/test_gas/1_emin/input", system_name="1_emin")
in_simSystem.imd = "/home/bschroed/Documents/projects/PyGromosTools_release3/examples/example_files/Hvap_files/hvap/test_gas/1_emin/simulation/1_emin_1/example_files/Hvap_files/hvap/test_gas/1_emin/input/Hvap_test.imd"
in_simSystem.top = "/home/bschroed/Documents/projects/PyGromosTools_release3/examples/example_files/Hvap_files/hvap/test_gas/1_emin/simulation/1_emin_1/example_files/Hvap_files/hvap/test_gas/1_emin/input/Hvap_test.top"
in_simSystem.cnf = "/home/bschroed/Documents/projects/PyGromosTools_release3/examples/example_files/Hvap_files/hvap/test_gas/1_emin/simulation/1_emin_1/example_files/Hvap_files/hvap/test_gas/1_emin/input/Hvap_test.cnf"

out_dir_path = "/home/bschroed/Documents/projects/PyGromosTools_release3/examples/example_files/Hvap_files/hvap/test_gas/1_emin/simulation/1_emin_1/example_files/Hvap_files/hvap/test_gas/1_emin/simulation"
simulation_run_num = 1
equilibration_run_num = 0
analysis_script_path = "/home/bschroed/Documents/projects/PyGromosTools_release3/examples/example_files/Hvap_files/hvap/test_gas/1_emin/simulation/1_emin_1/example_files/Hvap_files/hvap/test_gas/1_emin/job_analysis.py"
#Generate LOCAL
from pygromos.simulations.hpc_queuing.submission_systems.local import LOCAL as LOCAL_obj
submission_system = LOCAL_obj(submission=True, verbose=False, nmpi=1, nomp=1, job_duration="24:00")

verbose = True
verbose_lvl = 1



#DO
do(in_simSystem=in_simSystem, out_dir_path=out_dir_path, simulation_run_num=simulation_run_num, equilibration_run_num=equilibration_run_num, analysis_script_path=analysis_script_path, submission_system=submission_system, verbose=verbose, verbose_lvl=verbose_lvl, )
exit(0)


