import os

with open('celebahq_map.txt', 'rt') as file:
    lines = [line.split() for line in file]
    fields = dict()
    for idx, field in enumerate(lines[0]):
        type = int if field.endswith('idx') else str
        fields[field] = [type(line[idx]) for line in lines[1:]]

# print(fields.keys())
for file in ['celebahqtrain', 'celebahqvalidation']:
    orig_file = open(f'{file}_orig.txt').readlines()
    datas = []
    for line in orig_file:
        # print('done with', line)
        idx = int(line.replace('.npy','').replace('imgHQ',''))
        orig_file_row = fields['idx'].index(idx)
        orig_file_name = fields['orig_file'][orig_file_row].replace('jpg','npy')
        datas.append(orig_file_name+'\n')
        # print(line)
    with open(f'{file}.txt', 'w') as new_file:
        new_file.writelines(datas)
