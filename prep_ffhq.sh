FATHER="/srv/mingyang/ffhq-sqa/images1024x1024"
for folder in {0..69999}; do
    # get subfolder: 0~999 -> 00000, 1000-1999 -> 01000, ... (this is a rounding operation)
    subfolder=$(printf "%05d" $((folder/1000*1000)))
    name=$(printf "%05d" $folder)
    # echo "Processing $subfolder"
    file="$FATHER/$subfolder/$name.png"
    # assert file exists
    if [ -f "$file" ]; then

        # if the destination image exists, skip
        if [ -f "./data/ffhq/$name.png" ]; then
            continue
        fi
        echo "Processing $file"
        ln -s $file ./data/ffhq/$name.png
    else
        echo "File $file does not exist"
        # return 1
    fi  
done