# Google Fit consolidate data export
This script combines Google Fit data from a Google Takeout export into a single CSV for further analysis or other uses. The main intent was using the [Health CSV Importer](https://apps.apple.com/app/health-csv-importer/id1275959806) app for iOS, which will import CSV data into Apple Health, allowing someone to export Google Fit data into Apple Health.

# Acknowledgements
Thanks to Ben on Stack Exchange for the initial script.
Source URL: https://apple.stackexchange.com/a/428313/2319

# Structure
The following Google Fit CSV columns are provided by Google Takeout as of September 30, 2021, and can be added or removed from the included script depending on the user's preference for data to be included.

* Start time
* End time
* Move Minutes count
* Calories (kcal)
* Distance (m)
* Heart Points 
* Heart Minutes
* Average heart rate (bpm)
* Max heart rate (bpm)
* Min heart rate (bpm)
* Low latitude (deg)
* Low longitude (deg)
* High latitude (deg)
* High longitude (deg)
* Average speed (m/s)
* Max speed (m/s)
* Min speed (m/s)
* Step count
* Average weight (kg)
* Max weight (kg)
* Min weight (kg)
