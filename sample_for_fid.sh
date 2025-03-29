mkdir -p ./eval_fid
# CUDA_VISIBLE_DEVICES=0 python scripts/sample_diffusion.py -r models/ldm/ffhq256/model.ckpt -l ./eval_fid -n 50000 --batch_size 90 -c 200 -e 0.0

# fid-5k for fast debugging
CUDA_VISIBLE_DEVICES=0 python scripts/sample_diffusion.py -r models/ldm/ffhq256/model.ckpt -l ./eval_fid -n 5000 --batch_size 90 -c 200 -e 0.0