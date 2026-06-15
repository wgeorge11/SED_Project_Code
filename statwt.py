import os, sys
import numpy as np
from datetime import date

top_dir = '/Volumes/disks/Will_George/Data/' #this is where the data lives
targ_name = 'DGTau'
tag = 'B4_hi'
input_ms_name = 'DGTau_B4_hi.contap1.ms' # name of measurement set to be copied

data_dir = top_dir + targ_name + '/' # eg. this would give /Volumes/disks/Will_George/Data/DGTau/
source_ms = data_dir + tag + '/selfcal_2026-05-18/' + targ_name + '_' + tag + '.contap1.ms' # So, this will output: /Volumes/disks/Will_George/Data/DGTau/B4_hi/selfcal_2026-05-18

out_fol = data_dir + 'statwt_' + str(date.today()) + '/' # output folder where copied .ms will go, eg. /Volumes/disks/Will_George/Data/DGTau/statwt_2026-06-15/
mscpy = out_fol + targ_name + '_' + tag + '.contap1' + '_wtfx.ms'

print('Original MS:')
print(source_ms)

print('Copied/statwt MS:')
print(mscpy)

if not os.path.exists(source_ms):
    raise RuntimeError('Source MS does not exist.')

if os.path.exists(mscpy):
    raise RuntimeError('Copied MS already exists.')

os.system('mkdir -p ' + out_fol)
os.system('cp -r ' + source_ms + ' ' + mscpy)

statwt(vis=mscpy) #run statwt on the copied .ms

print('Complete! statwt was run on: ')
print(mscpy)
