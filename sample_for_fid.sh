mkdir -p ./eval_fid
CUDA_VISIBLE_DEVICES=0 python scripts/sample_diffusion.py -r models/ldm/celeba256/model.ckpt -l ./eval_fid -n 50000 --batch_size 24 -c 200 -e 0.0