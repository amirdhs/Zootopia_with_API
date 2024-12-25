# Animals Web Generator

This Python program generates a website displaying information about animals fetched from an API. The website is dynamically created based on user input, providing details about the specified animal.

---

## Features

1. **Fetch Animal Information from API**  
   Fetches detailed information about animals using the [API Ninjas Animals API](https://api-ninjas.com/api/animals).

2. **Dynamic Website Generation**  
   Creates a custom HTML website containing the animal's name, taxonomy, locations, and characteristics.

3. **User Interaction**  
   Prompts the user to enter an animal name to generate specific content for that animal.

4. **Error Handling**  
   Displays a friendly message on the website if the animal doesn’t exist or if no results are returned by the API.

---

## How to Run

### Prerequisites
1. **Python**: Ensure Python 3.6+ is installed.
2. **Dependencies**: Install the required Python libraries.
   ```bash
   pip install requests python-dotenv