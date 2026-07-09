top_dir = '/Volumes/disks/Will_George/Data/'
targ_name = 'MHO6'
tag = 'B4_hi'

vis = top_dir + targ_name + '/'  + targ_name + '_vis_B4_hi_copyD.ms'

output = top_dir + targ_name + '/' + tag + '/' + targ_name + '_model_D.ms'

split(vis=vis,
      outputvis=output,
      datacolumn='model',
      keepflags= False)


