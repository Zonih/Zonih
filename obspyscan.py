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