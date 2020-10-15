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