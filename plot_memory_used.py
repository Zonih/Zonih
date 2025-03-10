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


	
	
