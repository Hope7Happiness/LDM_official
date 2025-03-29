# read data/ffhqtrain.txt, separate by line
files=$(cat data/ffhqtrain.txt)
for file in $files
do
    ln -s $(readlink data/ffhq/$file) eval_fid/ffhq_ref/
done