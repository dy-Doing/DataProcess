# import re
import os


def Fix(path):
    with open(path, 'rb+') as file:
        file.seek(128, 0)
        file_type = file.read(4)
        if file_type == b'DICM':
            file.seek(0, 0)
            file_txt = file.read()
            location = b"\x18\x00\x88\x00"
            bias_between_location_to_zero = 8
            # print("re.findall()的返回值: ", re.findall(need, all))
            print('index(18 00 88 00):', file_txt.index(location))
            i = file_txt.index(location) + bias_between_location_to_zero
            print('seek(i):', i)
            file.seek(i, 0)
            key = file.read(1)
            print('i.value:', key)
            if key == b'0':
                file.seek(i, 0)
                file.write(b'5')


your_dir_path = r'C:\Users\18\Desktop\data'

for root, dirs, files in os.walk(your_dir_path):
    if files:
        for item in files:
            dcm_path = os.path.join(root, item)
            print('current_file:', dcm_path)
            try:
                Fix(dcm_path)
            except Exception as e:
                print(e)
