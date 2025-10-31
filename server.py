#!/usr/bin/python3
import json, os

qs = os.environ.get("QUERY_STRING", "")
fname = ""
for part in qs.split("&"):
    if part.startswith("file="):
        fname = part.split("=", 1)[1]
        break
fname = fname.strip()

def header():
    print("Content-Type: text/html; charset=utf-8\n")

if not fname or "/" in fname or "\\" in fname or not fname.lower().endswith(".json"):
    header()
    print("<h3>Please enter a valid JSON filename (e.g., truckinglist.json).</h3>")
else:
    data_path = os.path.join("/var/www/html/data", os.path.basename(fname))
    if not os.path.isfile(data_path):
        header()
        print(f"<h3>File not found: {fname}</h3>")
    else:
        try:
            with open(data_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            header()
            print(f"<h3>Failed to parse JSON: {e}</h3>")
        else:
            try:
                headers = data["Mainline"]["Table"]["Header"]["Data"]
                rows    = data["Mainline"]["Table"]["Row"]
            except Exception:
                header()
                print("<h3>Unexpected JSON structure.</h3>")
            else:
                html = []
                html.append("<!DOCTYPE html><html><head><meta charset='utf-8'><title>Trucking Companies</title></head><body>")
                html.append("<table border=\"1\"><tr>")
                for h in headers:
                    html.append(f"<th>{h}</th>")
                html.append("</tr>")

                for company in rows:
                    html.append("<tr>")

                    # company
                    html.append(f"<td>{company.get('Company','')}</td>")

                    # services
                    html.append(f"<td>{company.get('Services','')}</td>")

                    # hubs
                    hubs_cell = ""
                    hubs = company.get("Hubs")
                    if isinstance(hubs, dict) and isinstance(hubs.get("Hub"), list):
                        items = []
                        for i, aHub in enumerate(hubs["Hub"]):
                            if i == 0:
                                items.append(f"<li><strong>{aHub}</strong></li>")
                            else:
                                items.append(f"<li>{aHub}</li>")
                        hubs_cell = "<ul>" + "".join(items) + "</ul>"
                    html.append(f"<td>{hubs_cell}</td>")

                    # revenue
                    html.append(f"<td>{company.get('Revenue','')}</td>")

                    # homePage
                    hp = company.get("HomePage")
                    if hp:
                        html.append(f"<td><a href=\"{hp}\" target=\"_blank\" rel=\"noopener noreferrer\">{hp}</a></td>")
                    else:
                        html.append("<td></td>")

                    # logo
                    logo = company.get("Logo")
                    if logo:
                        src = logo if logo.startswith("http") else "/" + logo.lstrip("/")
                        alt = company.get("Company","Logo")
                        html.append(f"<td><img src=\"{src}\" alt=\"{alt} Logo\" width=\"50\" /></td>")
                    else:
                        html.append("<td></td>")

                    html.append("</tr>")

                html.append("</table></body></html>")

                header()
                print("".join(html))
