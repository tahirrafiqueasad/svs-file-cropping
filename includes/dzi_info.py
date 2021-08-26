""" 
Author:		 Muhammad Tahir Rafique
Date:		 2021-08-26 12:08:38
Description: Provide a function to read the configuration of dzi files.
"""


# ===============================================
#       DEEP ZOOM IMAGE FILE INFO
# ===============================================
def read_dzi_file_info(file_path):
    """Reading dzi file configuration strored in .dzi file."""
    # 1. TAGES TO READ
    needed_tag_info = ['Overlap', 'TileSize', 'Height', 'Width']

    # 2. OPENING FILE
    with open(file_path) as f:
        content = f.readlines()

    # 3. FILTERING DATA
    info = {}
    for line in content:
        raw_tag = line.strip()
        for tag in needed_tag_info:
            if tag in raw_tag:
                value = int(raw_tag.split('=')[-1][1:-1])
                info[tag] = value
                break
    return info