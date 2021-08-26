""" 
Author:		 Muhammad Tahir Rafique
Date:		 2021-08-26 12:05:59
Description: Provide a function to crop the svs file.
"""
import os
import argparse
import cv2

from includes.dzi_crop import get_crop_from_dz

def get_svs_image_crop_from_dzi(dzi_dir, bounding_box):
    """Croping svs file using dzi."""

    # 1. GETTING DZI FILE DIR
    dzi_file_dir = dzi_dir + '_files'

    # 2. GETTING DZI INFO FILE PATH
    root_dir, file_name = os.path.split(dzi_dir)
    dzi_info_path = os.path.join(root_dir, f'{file_name}.dzi')

    # 3. GETTING CROP
    crop = get_crop_from_dz(dzi_file_dir, dzi_info_path, bounding_box)

    return crop


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Getting crop of svs file using dzi.')

    parser.add_argument(
        '-i', '--input',
        type=str,
        help='path to dzi directory containg images directory and file.dzi',
        required=True
    )

    parser.add_argument(
        '-o', '--output',
        type=str,
        help='path to image',
        required=True
    )

    parser.add_argument(
        '-c', '--coordinate',
        nargs="+",
        help='list of cordinates eg: xmin ymin xmax ymax',
        required=True,
        type=int
    )

    args = parser.parse_args()
    crop = get_svs_image_crop_from_dzi(args.input, args.coordinate)

    # SAVING CROP
    cv2.imwrite(args.output, crop)
