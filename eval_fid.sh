fidelity --gpu 0 --fid --input2 ./eval_fid/celeba256_ref --input1 ./eval_fid/celeba256/samples/00490000/2025-01-03-23-37-26/img

# sanity check
# fidelity --gpu 0 --fid --input2 ./eval_fid/celeba256_ref --input1 ./eval_fid/celeba256_ref_valid_sanity
# this sanity check should give ~3.5 FID