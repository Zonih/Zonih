# REFNOS Service Run

Hello! In this walkthrough, we will outline the steps involved before, during, and after a service run to retrieve and systematize data from the field.

As you know, we have 70 Smart Solo Nodes deployed in a densely populated area. Since the batteries last approximately 28 days, it is essential to follow a systematic order for swapping the nodes (replacing old ones with new ones) and for downloading and uploading data to the servers.

#### Before the Service Run

Before heading out to the field, ensure you have all the necessary materials prepared:

1. <u>**Nodes:**</u> Ensure all the nodes are ready, programmed with the script, and have fully charged batteries. For assistance with setting up the node scripts, please refer to **README_NODES_PROSPECT**.

2. <u>**Field Sheets:**</u> Prepare all necessary field sheets, such as: ![Screenshot 2025-02-03 at 8 34 55 AM](https://github.com/user-attachments/assets/bb0e140a-ae3a-4313-a5bd-0ed50f1a643f)

3. <u>**Maps:**</u> Create and print a simple Google Earth map marking all field points. This will help visualize completed and pending tasks.

4. <u>**Navigation:**</u> Develop a Google Maps project with all field points for easy navigation.

5. <u>**Owners information:**</u> If your field points are on private properties, contact the owners in advance to confirm their availability. Print this information and bring it with you to the field.

6. <u>**Equipment:**</u>
    - Node magnets
    - GPS devices or smartphone for navigation
    - Nodes chargers
    - Harvesters
    - Cables
    - Power strips
    - Field computers (with sufficient storage space)
    - Compasses
    - Shovels
    - Sand (for proper node coupling with the ground)
    - Cloths and water (for cleaning the nodes)
    - Tape and markers (to identify used nodes from new ones)
    - Wrench
    - Gloves
    - Plastic bags (to cover the nodes)

#### During the Service Run

1. Navigate to the field point using the Google Maps project.

2. Locate the node and check if it is turned on, leveled and properly oriented.

3. If the node is on, turn it off using the Smart Solo magnet pattern. If it is off, gently pull it from the ground.

4. Record the serial numbers of the old node.

5. Prepare the new node by placing it in plastic bags and note its serial numbers.

6. Deploy the new node, ensuring it is leveled and oriented correctly.

7. Turn the new node on.

8. Wait until the indicator light flashes green.

9. Clean the old node and mark it with its site code.

10. Proceed to the next point and repeat the process.

#### After the Service Run

After completing the service run, follow these steps to ensure proper data management and systematization. This section is divided into three key tasks: Download, Upload, and Systematization.

##### Download
1. Unscrew the nodes.

2. Place the heads into the harvesters.

3. Insert the batteries into the chargers.

4. Connect the harvester to the field computer, but do not turn them on yet.

5. If you have more than one Harvester, make sure you are using the correct device configuration file. You can find these files in the _**deviceconfig**_ folder. <img width="512" alt="Screenshot 2025-02-18 074843" src="https://github.com/user-attachments/assets/b4ac095b-7a74-4b7f-8792-14795cca8a51" />

6. If the correct configuration file is incorrect, you can find alternative options in the _**DeviceConfigArchive**_ folder. Choose the appropriate file and copy it into the _**deviceconfig**_ folder. ![Screenshot 2025-02-18 074900](https://github.com/user-attachments/assets/62e2d240-6423-4893-8229-b2940540ce6a)

7. Open the _**SoloLite.exe**_ program.

8.  Open the project. Ensure you have already created a prospect using **README_NODES_PROSPECT**.![Screenshot 2025-02-03 095642](https://github.com/user-attachments/assets/41097a63-eb24-4674-840d-1b5912d66067)

9. Plug in the harvesters and chargers, then turn them on.

10. The data will download automatically, which may take a few minutes.

11. After the download is complete, you can find all raw data (in DLD format) in the _**DCCDATA**_ folder within the service run subfolder on the computer. ![Screenshot 2025-02-03 103149](https://github.com/user-attachments/assets/9b9bf01b-2ad0-40d2-9470-e3f878bf035b)

12. If the _**FIFOS**_ option is not enabled (see details in **README_NODES_PROSPECT**), you must set up the nodes with the script. Click on the _**Setup IGU-16**_ icon. 
![Screenshot 2025-02-03 162110](https://github.com/user-attachments/assets/95b568bd-fa74-4574-a247-6b534d2924d5)

13. A new window titled _**Device Setup**_ will appear. Check the following boxes: Select all, Format device, Retain configuration files, and Write script. Ensure you select the correct script for the last option.
![Screenshot 2025-02-03 162210](https://github.com/user-attachments/assets/515230d0-c179-4171-97dd-8d5a09d09b18)

14. Click the _**Apply**_ button and wait for the nodes to be set up.

15. To convert the data to MSEED or SAC format, follow these additional steps. If you have multiple service runs within a short time frame with repeating nodes, the SoloLite program may crash due to the large amount of data stored in the project history. It is recommended to create a new _**Prospect**_ with a new _**Project**_ for data conversion. Refer to **README_NODES_PROSPECT** for guidance.

16. Once you have a new _**Prospect**_, copy and paste the DLD files into the _**DCCDATA**_ folder of the new service run subfolder.

17. In the SoloLite program, click the _**Reanalyze seismic data**_ icon.
![Screenshot 2025-02-03 110734](https://github.com/user-attachments/assets/3ca684bc-37b2-42b6-bd79-4e0ed9d7bdd1)

18. A small window will pop up; select the option _**<img width="512" alt="Screenshot 2025-02-18 074843" src="https://github.com/user-attachments/assets/8f54752a-4540-4051-9bb0-e8d96441a040" />
Reanalyze All (Delete database record prior to analysis)**_. 

19. Click the _**Reanalysis button**_.

20. After this, the history panel should be filled up as shown in the following image:
![Screenshot 2025-02-03 111453](https://github.com/user-attachments/assets/57b0b5e1-270b-47dd-8d2f-d16cad3a9978)

21. Convert the data to MSEED or SAC format by clicking the _**Export Seismic Data**_ icon. 
![Screenshot 2025-02-03 103406](https://github.com/user-attachments/assets/675265c5-d691-42e2-870b-71d04c1c38c1)

22. A new window will appear; fill in the information as needed.
![Screenshot 2025-02-03 103741](https://github.com/user-attachments/assets/6584ce71-b9d5-4b23-b417-507502f1a00e)

23. Click the _**Prepare**_ button and then the _**Run**_ button.

21. Wait for the progress bar to complete.

23. All converted data will be stored in the _**SOLODATA**_ folder on the computer. ![Screenshot 2025-02-03 104505](https://github.com/user-attachments/assets/f21e76c6-b5a8-405e-803a-7196bcf0cadb)

24. Now you can close the SoloLite program.

25. Once the batteries are charged, screw the nodes back in.

##### Upload

1. To upload the data (both DLD and converted formats) to a server, use _**FileZilla Client**_. 
![Screenshot 2025-02-03 111852](https://github.com/user-attachments/assets/3015bec1-7f7a-468b-99c4-72ae0be32f63)

2. Enter the Host, Username, Password, and Port details.

3. Click the _**Quickconnect button**_.


4. In the _**Local site panel**_, navigate to the folder containing the files. 
![Screenshot 2025-02-03 112427](https://github.com/user-attachments/assets/d8e2a3e7-39c5-4df7-9a29-19ba9a08ded3)

5. In the _**Remote site panel**_, navigate to the destination folder where you want to upload the data.

6. Right-click on the data files you want to transfer and select _**Upload**_.

7. Wait until all files have been successfully uploaded.

8. Once the upload is complete, you can close the _**FileZilla**_ program.

#### Data Systematization

1. Create a text file in _**VS Code**_, with two columns and a header:
        - Site Code
        - Sensor SN (serial number)

2. _**Carefully enter the data from the Field Sheets**_, ensuring accuracy in the Site Code and Serial Numbers. Double-check to avoid mistakes.

3. Save the file in _**.dat format**_.

4. Scan the Field Sheets and upload them to a server or Google Drive for backup.

5. Upload the _**dat file**_ to the same server where the seismic data has been transferred. You can use _**FileZilla**_ or _**SFTP**_ for this step.

6. In our case, we need to convert the MSEED files to _**Antelope format**_. To do this, we use the _**dat file**_ along with a script that renames the MSEED files and organizes them into subfolders by Julian day, placing them inside a folder named after the current year.
```python
from obspy.core import read, UTCDateTime
from obspy.core.util.attribdict import AttribDict
import numpy as np 
import os
import glob
import datetime
import argparse


def format_file_name(var1, var2):

    if os.path.exists(var1) and os.path.exists(var2):
        print("The declared directory and input file exist....reading files and creating a list of data to be formated")
        
        node_code, head_id = np.loadtxt(var2, unpack=True, dtype='str', 
        			usecols=(0,1), skiprows=1)
        
        data_list = glob.glob(os.path.join(var1, "*miniseed"))
        
        if data_list:
            for i, waveform in enumerate(data_list):
            
                waveform_name = waveform.split("/")[1]
                head_id_field = waveform_name.split(".")[0]
                print(f"Working on: {waveform_name}")
                
                node_list = ['00000000']
                
                if head_id_field not in node_list:
                        lfn = np.nonzero(head_id == head_id_field)
                        print(lfn)
                        node_field = node_code[lfn][0]
                        print(f"The head id: {head_id_field} corresponds with node id: {node_field}")
                        st = read(waveform)
                        tr = st[0]
                        tr.stats.station = node_field
                        tr.stats.network = "OV"
                        tr.stats.location = " "
                        if tr.stats.channel == "DPN":
                                tr.stats.channel = "HHN"
                        elif tr.stats.channel == "DPZ":
                                tr.stats.channel = "HHZ"
                        elif tr.stats.channel == "DPE":
                                tr.stats.channel = "HHE"
                        time  = tr.stats.starttime
                        year = time.year
                        month = str(time.month)
                        day = str(time.day)
                        day_of_year = time.julday
                        if len(month) == 1:
                                month = f"0{month}"
                        if len(day) == 1:
                                day = f"0{day}"
                        destino_final = f"{year}/{day_of_year}"
                        if not os.path.exists(destino_final):
                                os.makedirs(f"{destino_final}")
                        else:
                                print(f"destino final: {destino_final} already exists....saving files now!")
                        file_output_name = f"i4.{node_field}.{tr.stats.channel}.{year}{day_of_year}_0+"
                        print(f"The miniseed file: {waveform_name} ** is formatted with: {file_output_name}")
                        path_out = os.path.join(destino_final, file_output_name)
                        print(path_out)
                        tr.write(path_out, format='MSEED')
                

        else: 
            print("SmartSolo miniseed files not found....")

    else: 
        print("Please check data path, it does not exists in current directory....")
        

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Please add the input variables: -D for directory with miniseed data to be formated and -D with the service run node ids")
	parser.add_argument('-D', '--var1', type=str, required=True, help='Input directory where files are located')
	parser.add_argument('-F', '--var2', type=str, required=True, help='Input File with nodes Ids')
	
	args = parser.parse_args()
	format_file_name(args.var1, args.var2)
	
```
7. To run the script, simple execute the following command in the terminal:
`python 0_convert_to_antelope.py -D MSEEDFolder -F servicerun.dat`

8. If you want to visualize your daily data storage in a plot, you first need to create another _**dat file**_ containing the storage usage (GB per day). You can generate this file using the following Bash command, where _**foldername**_ is the directory named after the year:
`du -h --max-depth=1 foldername | grep -v "foldername$" | awk '{gsub("foldername/", "", $2); print $1 "\t" $2}' | sort -k2n > mem_per_day.dat`

9. Once the file is created, you can plot the memory usage by running: `python plot_memory_used.py -F mem_per_day.dat` 
<u>**Note:**</u> Make sure to adjust the figure name in the following script if needed.

```python
import numpy as np 
import matplotlib.pyplot as plt
import argparse


def memory_used(var1): 

	mem, day = np.loadtxt(var1, unpack=True, dtype='str', usecols=(0,1))
	day = day.astype(int)
	
	gb=[]
	for i in mem:
		if 'M' in i:
			size = float(i.split('M')[0]) / 1024
			gb.append(size)
		if 'G' in i:
			size = float(i.split('G')[0])
			gb.append(size)

	days=[]
	for d in day:
		d= int(d)
		if d >=185:
			days.append(f"2024-{d}")
		else:
			days.append(f"2025-{d}")
			
	fig, ax = plt.subplots(1, 1, figsize=(10, 5))
	ax.plot(range(len(days)), gb, zorder=1, lw=1.5, color='k', alpha=1)
	
	ax.set_xticks(range(len(days))[::10])  # Show every 10th day to avoid overcrowding
	ax.set_xticklabels(days[::10], rotation=45, ha="right", fontsize=8)
	
	ax.set_ylabel("Data size, Gb", fontsize=14)
	ax.set_xlabel("Day of the year (2024-2025)", fontsize=14)
	ax.grid(True, lw=0.5, zorder=0, linestyle='--', color='grey')
	ax.set_title("REFNOS Daily Data Storage")
	
	plt.tight_layout()
	fig.savefig("Daily_Data_Storage_serv7.png", format='png', dpi=700)
	#plt.show()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Please include inputFile')
	parser.add_argument('-F', '--var1', type=str, required=True, help="memory file")
	
	args = parser.parse_args()
	memory_used(args.var1)

```
10. To check data availability per station and component, you can use _**obspy-scan**_. Keep in mind that the script takes approximately _**1 minute per folder with around 6.6 GB of data**_, so it is recommended to run the process in parallel for efficiency. 

```python
import os
import glob
import multiprocessing

mseed_files = glob.glob("2024/*/*") + glob.glob("2025/*/*")

def run_obspy_scan(file):
    """Runs obspy-scan on a given file and appends output to a single PDF."""
    os.system(f"obspy-scan --format MSEED --output obspyscan.pdf {file}")

if __name__ == "__main__":
    num_workers = 2  # cores

    with multiprocessing.Pool(processes=num_workers) as pool:
        pool.map(run_obspy_scan, mseed_files)

    print("Obspy-scan completed. Output saved in obspyscan.pdf.")
```
11. To run the code, simply type the following command in the terminal: `python obspyscan.py`.


##### What to do if a site is discontinued?
Sometimes, for various reasons, you may need to discontinue a site and establish a new one in a different location. Here's how to proceed:

1. Remove the node from the disconitued site and communicate with the landowners.

2. Record the serial numbers of the removed node.

3. If maintaining data continuity is important for your project, we recommend selecting a new location as close as possible to the disconitued site, preferably where the landowners have availability.

4. Choose an appropiate spot for the new deployment and dig the hole.

5. Record the new site details, including coordinates, landowner information, site code (new code), battery and head serial numbers, and any other relevant datails. You can use the _**Deployment Sheet**_ found in **README_DEPLOYMENT**.

6. Add the new site to both Google Earth and Google Maps.

7. Remove the disconitued site from Google Earth and Google Maps.
