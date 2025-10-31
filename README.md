#  Trucking Companies JSON Viewer

This simple web app lets you **fetch and display trucking company data**
from a JSON file in a new pop-up window. It dynamically builds a
formatted HTML table with company info, including logos, services, hubs,
and links.

##  Live Usage (AWS EC2 Link)

To use the app, visit your AWS-hosted page:

**<http://ec2-18-207-143-97.compute-1.amazonaws.com>**

## Instructions

1.  Open the link above in your browser.\
2.  In the input field, **enter a valid JSON file URL**
    (e.g. `truckinglist.json`).\
3.  Click **Submit Query**.\
4.  The trucking companies will appear in a new pop-up window as a
    formatted table.

> ⚠️ **Note:** If you enter an invalid or blank URL, you'll see an error
> message saying:\
> "Please enter a valid JSON file URL."

##  Features

-   Fetches data dynamically from a provided JSON URL\
-   Displays data in a scrollable pop-up table\
-   Handles invalid or blank URLs gracefully\
-   Supports clickable company links and embedded logos