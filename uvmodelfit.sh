import os

top_dir = '/Volumes/disks/Will_George/Data/'
targ_name = 'DGTau'
shape = 'G' # G or D based on Gaussian or Disk 
tag = 'B4_hi'
cf_date = '2026-06-15' # date of the casa_fit

data_dir = top_dir + targ_name + '/'
cl_dir = data_dir + 'casa_fit_' + cf_date + '/' # Folder containing .cl directories
band_dir = data_dir + tag +'/' # band directory where .ms directory lives

os.system('mkdir -p ' + cl_dir)

vis = band_dir + targ_name + '_vis_' + tag + '.ms'
outfile = cl_dir + targ_name + '_complist_' + shape + '.cl'

os.system('rm -rf ' + outfile) # delete the old version of the .cl directory before rerunning uvmodelfit

uvmodelfit(
vis= vis,
field='',
comptype=shape,
sourcepar=[0.0961951,0,0,0.536163,0.761718,48.8723],
outfile= outfile
)
