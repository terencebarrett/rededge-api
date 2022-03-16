import re
import csv

import click


# TODO: Read and write with pandas instead of the csv library, to make robust to
#  changes in number of spaces between columns in input file
# TODO: Determine band count (and image count, to check against lat/long records)
#  by surveying the images folder

@click.group()
def main():
    pass


@main.command()
@click.option('--input_path', default=None, help='Path of file to have flight image numbers inserted (original file is kept unmodified')
@click.option('--output_path', default=None, help='Path to save new file output with image numbers inserted')
@click.option('--band_count', default=10, help='Number of band images')
def create_image_location_file(input_path, output_path, band_count):
    img_counter = 0
    with open(input_path, 'r') as f:
        text_reader = csv.reader(f, delimiter=' ')
        with open(output_path, 'w', newline='') as g:
            text_writer = csv.writer(g, delimiter=',')
            text_writer.writerow(['Image', 'latitude', 'longitude', 'altitude',
                                  'omega', 'phi', 'kappa', 'Accuracy_XY', 'Accuracy_Z'])
            for row in text_reader:
                date_to_img = re.match('\d{4}.\d{2}.\d{2}', row[0])
                if date_to_img:
                    latitude = row[4]
                    longitude = row[6]
                    altitude = row[10]
                    omega = 0  # TODO: Read this when becomes available
                    phi = 0  # TODO: Read this when becomes available
                    kappa = 0  # TODO: Read this when becomes available
                    accuracy_xy = max([float(row[19]), float(row[22])])
                    accuracy_z = row[25]
                    for n in range(1, band_count+1):
                        image = 'IMG_%04d_%d.tif' % (img_counter, n)
                        text_writer.writerow([image, latitude, longitude, altitude,
                                              omega, phi, kappa, accuracy_xy, accuracy_z])
                    img_counter += 1


if __name__ == "__main__":
    main()
