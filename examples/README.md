Setup
-----
1. Install [Miniconda3](https://docs.conda.io/en/latest/miniconda.html)
2. Download code repo to local machine from the [SAL fork](https://github.com/terencebarrett/rededge-api/tree/gh-pages) of the vendor's repo
   - Click green "Code" button and "download zip"
     - We'll save the preferable "cloning" method for another time; "download zip" is ok for now
3. `> cd` to `examples` folder of local repo
4. Create and activate python environment to run code in
   - `> conda env create environment.yml`
   - `> conda activate rededge`
     - The activated python environment will now be shown to the left of the cursor: `(rededge) >`
5. Example run to "associate image files and update event geotag information" - with three options for how to specify Windows paths
   - `(rededge) > python gps_image_insert.py create-image-location-file --input_path L:\\Temp\\Emlid_Micasense_Integration\\03_ppk-events\\Reach-rover_raw_202203081558_events.pos --output_path L:\\Temp\\Emlid_Micasense_Integration\\04_exif-csv\\pix4d_geolocation_format.csv`
   - `(rededge) > python gps_image_insert.py create-image-location-file --input_path "L:\Temp\Emlid_Micasense_Integration\03_ppk-events\Reach-rover_raw_202203081558_events.pos" --output_path "L:\Temp\Emlid_Micasense_Integration\04_exif-csv\pix4d_geolocation_format.csv"`
   - `(rededge) > python gps_image_insert.py create-image-location-file --input_path L:\Temp\Emlid_Micasense_Integration\03_ppk-events\Reach-rover_raw_202203081558_events.pos --output_path L:\Temp\Emlid_Micasense_Integration\04_exif-csv\pix4d_geolocation_format.csv`
   - Result is a file named `pix4d_geolocation_format.csv` at `L:\Temp\Emlid_Micasense_Integration\04_exif-csv`