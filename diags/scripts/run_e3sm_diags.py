import os
from acme_diags.parameter.core_parameter import CoreParameter
from acme_diags.run import runner

param = CoreParameter()

param.reference_data_path = '/compyfs/e3sm_diags_data/obs_for_e3sm_diags/climatology/'
param.test_data_path = '/compyfs/e3sm_diags_data/test_model_data_for_acme_diags/climatology/'
param.test_name = '20161118.beta0.FC5COSP.ne30_ne30.edison'
param.seasons = ["ANN"]   #all seasons ["ANN","DJF", "MAM", "JJA", "SON"] will run,if comment out"

prefix = '/compyfs/www/coop558/doc_examples/'
param.results_dir = os.path.join(prefix, 'lat_lon_demo')
# Use the following if running in parallel:
#param.multiprocessing = True
#param.num_workers = 32

# Use below to run all core sets of diags:
#runner.sets_to_run = ['lat_lon','zonal_mean_xy', 'zonal_mean_2d', 'polar', 'cosp_histogram', 'meridional_mean_2d']
# Use below to run lat_lon map only:
runner.sets_to_run = ['lat_lon']
runner.run_diags([param])

# notes on where to pick up. I need to copy the script above to my compy directory and then pick up on the tutorial at step 2. Config and run
scp /Users/coop558/e3sm/diags/scripts/run_e3sm_diags.py coop558@compy.pnl.gov:/test/

#############################

import outlook calendar to cisco
outlook on iphone
constant request to sign in to outlook
time billing
microsoft authenticator


source /share/apps/E3SM/conda_envs/load_latest_e3sm_unified.sh


E3SM source code:
https://github.com/Arctic-InteRFACE/E3SM/tree/master/components
Or
https://github.com/E3SM-Project/E3SM/tree/master/components

E3SM diagnostics:
https://github.com/E3SM-Project/e3sm_diags


# I am following the guide here: https://e3sm-project.github.io/e3sm_diags/docs/html/quickguides/quick-guide-compy.html



<activation_command>: source /share/apps/E3SM/conda_envs/load_latest_e3sm_unified.sh

<obs_path>: /compyfs/e3sm_diags_data/obs_for_e3sm_diags/

<test_data_path>: /compyfs/e3sm_diags_data/test_model_data_for_acme_diags/

<html_path>: /compyfs/www/<username>/

<web_address>: https://compy-dtn.pnl.gov/<username>/

https://compy-dtn.pnl.gov/coop558

#######################################################################


[#]
# What sets to run this diagnostics on
sets = ['lat_lon']

# Diagnostics results are saved in a folder named after the case_id
case_id = "lat_lon_MERRA"

# variables, ref_name, and season are keywords for obs file searching
variables = ["T"]
ref_name = "MERRA"
seasons = ["ANN", "JJA"]

# Name of the observation that will appear on the output plot
reference_name = "MERRA Analysis 1979-2013 NASA"

# User-specified pressure levels
plevs = [200.0, 850.0]

# User-defined regions, the default region is "global" if region is empty
# Find default_regions.py in this repo for a list of all possible regions
regions = ["land", "ocean_TROPICS"]