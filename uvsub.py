from casatasks import uvsub, tclean

topdir = '/Volumes/disks/Will_George/Data/KPNO10'
tag = 'B4_hi'
vis_ms = topdir + '/' + tag + '/' + 'selfcal_2026-05-19' + '/' + 'KPNO10_B4_hi.contap1.ms'
model_image = topdir + '/residuals'

uvsub(vis=vis_ms)

tclean(vis=vis_ms,
       imagename=model_image,
       datacolumn='corrected',
       imsize=[250,250],
       cell='0.025arcsec',
       niter=0)
