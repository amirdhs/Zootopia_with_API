from data_fetcher import fetch_data


def generate_html(data, animal_name):
    html_content = """ 
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                margin: 20px;
                padding: 20px;
            }
            h2 {
                color: #4CAF50;
                border-bottom: 2px solid #4CAF50;
                padding-bottom: 5px;
            }
            ul {
                list-style-type: none;
                padding: 10px;
                background-color: white;
                border-radius : 10px;
            }
            li {
                margin-bottom: 10px;
            }
            .not-found {
                color: red;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
    """
    if data:
        if len(data) == 0:
            html_content += f"<h2 class='not-found'>The animal '{animal_name}' doesn't exist.</h2>"
        else:
            for animal in data:
                html_content += f"<h2>{animal['name']}</h2>"
                html_content += "<ul>"
                html_content += f"<li><strong>Taxonomy:</strong> {animal['taxonomy']}</li>"
                html_content += f"<li><strong>Locations:</strong> {', '.join(animal['locations'])}</li>"
                html_content += f"<li><strong>Characteristics:</strong> {animal['characteristics']}</li>"
                html_content += "</ul>"
    else:
        html_content += f"<h2 class='not-found'>The animal '{animal_name}' doesn't exist.</h2>"
    html_content += """
    </body>
    </html>
    """
    return html_content


animal_name = input("Enter a name of an animal: ")
data = fetch_data(animal_name)

# Write to animals.html
if data is not None:
    html_content = generate_html(data, animal_name)
    with open("animals.html", "w") as file:
        file.write(html_content)
    print("Website was successfully generated to the file animals.html.")