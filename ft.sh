top_dir = '/Volumes/disks/Will_George/Data/'
targ_name = 'MHO6'
tag = 'B4_hi'

vis = top_dir + targ_name + '/' + tag + '/' + targ_name + '_vis_' + tag + '.ms'

complist = top_dir + targ_name + '/' +'casa_fit_2026-06-29' + '/' + targ_name + '_complist_D.cl'

ft(
  vis= vis,
  field= '',
  spw= "",
  complist= complist,
  usescratch=True
)
