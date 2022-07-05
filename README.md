# Google Fit consolidate data export
This script combines Google Fit data from the "Daily activity metrics" folder of a [Google Takeout](https://takeout.google.com/settings/takeout) export into a single CSV for further analysis or other uses. The main intent was using the [Health CSV Importer](https://apps.apple.com/app/health-csv-importer/id1275959806) app for iOS, which will import CSV data into Apple Health, allowing someone to export Google Fit data into Apple Health.

# Acknowledgements
Thanks to [Ben](https://apple.stackexchange.com/users/297377/ben) on Stack Exchange for the initial script.

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

# Formats supported by Health CSV Importer
As of my conversations with Lionheart Software on November 8, 2021, below are the currently supported date and time formats which can then be used in combination with each other e.g. yyyy-MM-dd HH:mm:ss.SSSZ

I have made recommendations to the developers to include timezone separators like +/- to more closely align with the ISO 8601 standard as this would alleviate some import issues with the format Google currently uses.

## Date formats:
* MM-dd-yyyy (e.g. 04-16-2020)
* dd-MM-yyyy (e.g. 16-04-2020)
* yyyy-MM-dd (e.g. 2020-04-16)
* yyyy-dd-MM (e.g. 2020-16-04)
* yyyyMMddHHmmssZ
* MMMM d, yyyy (e.g. April 16, 2020)

## Time formats:
* HH:mm
* hh:mm a
* HH:mm:ss
* hh:mm:ss a
* HH:mm:ss Z
* hh:mm:ss a Z
* HH:mm:ssZ
* HH:mm:ss.SSSZ
