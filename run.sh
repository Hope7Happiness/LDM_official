# CUDA_VISIBLE_DEVICES=0 python main.py --base configs/latent-diffusion/celebahq-ldm-vq-4.yaml -t --gpus 0, \
#  2>&1 | tee main.log

# python main.py --base configs/latent-diffusion/ffhq-ldm-vq-4.yaml -t --gpus 0,1,2,3,4,5,6,7 \
# 	2>&1 | tee main.log

CUDA_VISIBLE_DEVICES=1,2,3,4,5,6,7 python main.py --base configs/latent-diffusion/ffhq-ldm-vq-4.yaml -t --gpus 0,1,2,3,4,5,6 \
	2>&1 | tee main.log
