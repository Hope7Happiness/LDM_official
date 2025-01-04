CUDA_VISIBLE_DEVICES=0 python main.py --base configs/latent-diffusion/celebahq-ldm-vq-4.yaml -t --gpus 0, \
 2>&1 | tee main.log