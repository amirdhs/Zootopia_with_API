from data_fetcher import fetch_data


def generate_html(data, animal_name):
    html_content = "<html><body>\n"
    if data:
        if len(data) == 0:
            html_content += f"<h2>The animal '{animal_name}' doesn't exist.</h2>"
        else:
            for animal in data:
                html_content += f"<h2>{animal['name']}</h2>\n"
                html_content += "<ul>\n"
                html_content += f"<li>Taxonomy: {animal['taxonomy']}</li>\n"
                html_content += f"<li>Locations: {', '.join(animal['locations'])}</li>\n"
                html_content += f"<li>Characteristics: {animal['characteristics']}</li>\n"
                html_content += "</ul>\n"
    else:
        html_content += f"<h2>The animal '{animal_name}' doesn't exist.</h2>\n"
    html_content += "</body></html>"
    return html_content


animal_name = input("Enter a name of an animal: ")
data = fetch_data(animal_name)

# Write to animals.html
if data is not None:
    html_content = generate_html(data, animal_name)
    with open("animals.html", "w") as file:
        file.write(html_content)
    print("Website was successfully generated to the file animals.html.")