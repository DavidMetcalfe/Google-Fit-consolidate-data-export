import os, sys, csv

# Thanks to Ben on Stack Exchange for the initial script.
# Source URL: https://apple.stackexchange.com/a/428313/2319
# Modified by David Metcalfe on October 22, 2021


# The following Google Fit CSV columns are provided by Google Takeout as of September 30, 2021:
# ------------------------------------------------------------------------------------
# Start time, End time, Move Minutes count, Calories (kcal), Distance (m), Heart Points, 
# Heart Minutes, Average heart rate (bpm), Max heart rate (bpm), Min heart rate (bpm), 
# Low latitude (deg), Low longitude (deg), High latitude (deg), High longitude (deg), 
# Average speed (m/s), Max speed (m/s), Min speed (m/s), Step count, 
# Average weight (kg), Max weight (kg), Min weight (kg)
# ------------------------------------------------------------------------------------

# CSV columns to be extracted.
COLUMNS_TO_KEEP = [
    "Start time",
    "End time",
    "Distance (m)",
    "Average heart rate (bpm)",
    "Step count",
    "Average weight (kg)"
]
data = [] # Container for storing all CSV data.

# Path check and error handling
input_path = sys.argv[1]
if not os.path.isdir(input_path):
    print("%s is not a valid directory" % input_path)
    sys.exit(1)
else: 
    input_path = os.path.abspath(input_path)

def clean_input_file_list(path):
    # Get file list and remove Daily activity metrics file and any hidden files.

    print("--------------------------")
    print("Cleaning Input File list.")
    counter = 0
    activity_metrics_files = sorted(os.listdir(path))
    start_file_count =  len(activity_metrics_files)

    # Try to remove "daily activity metrics.csv" from activity_metrics_files
    # list so it's not erroneously processed with the other files.
    try: 
        activity_metrics_files.remove("Daily activity metrics.csv")
    except:
        pass
    
    for f in activity_metrics_files:
        if f.startswith('.'):
            activity_metrics_files.pop(counter)
            counter += 1
            continue
        counter += 1
    end_file_count = len(activity_metrics_files)
    if start_file_count - end_file_count > 0:
        print(f"{start_file_count - end_file_count} files removed from Input File list.")
    print("Cleaning complete.")
    print("--------------------------")
    return activity_metrics_files


for f in clean_input_file_list(input_path):
    with open(os.path.join(input_path, f)) as infile:
        date = os.path.splitext(f)[0] # Extract filename from extension. 
        reader = csv.reader(infile)
        columns = []
        for row in reader:
            if columns == []:
                columns = row
                continue
            tmp = []
            for pos, cell in enumerate(row):
                if columns[pos] in COLUMNS_TO_KEEP:
                    if "time" in columns[pos]:
                        cell = f"{date} {cell}"
                    tmp.append(cell)
            if any(tmp[2:]): # Only append data if any of the value columns have a value
                data.append(tmp)


outpath = os.path.join(input_path, "consolidated_fit_data.csv")

with open(outpath, "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(COLUMNS_TO_KEEP)
    writer.writerows(data)