top_dir = '/Volumes/disks/Will_George/Data/'
targ_name = 'DGTau'
tag = 'B4_hi'

vis = top_dir + targ_name + '/' + tag + '/' + targ_name + '_vis_' + tag + '.ms'

tclean(
    vis= vis,
    imagename= targ_name,
    field="",
    spw="",
    specmode="mfs",
    gridder="standard",
    deconvolver="hogbom",
    imsize=[250, 250],
    cell=["0.025arcsec"],
    weighting="briggs",
    threshold="0mJy",
    niter=5000,
    interactive=True,
)


