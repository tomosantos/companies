# COMPANIES DATA VISUALIZATION
### Video Demo:  https://www.youtube.com/watch?v=c6OVJMzM7iI&ab_channel=WellintonOliveira
### Description:
    This python script retrieves information about the largest companies in the United States by revenue from a Wikipedia page, converts it into a structured DataFrame, and visualizes the data in a PDF table. Moreover, the code generates a .csv file and print the DataFrame in a table format in the terminal window at the end.

### Overview:
    The script performs the following tasks:
    1. Data Retrieval:
        • Utilizes the BeautifulSoup to scrape data from the Wikipedia page List of largest companies in the United States by revenue.
        • Extracts the relevant table data and column titles.

    2. DataFrame Creation:
        • Constructs a Pandas DataFrame using the extracted data.
        • Converts the DataFrame into a CSV file ('companies.csv') for further analysis or reference.

    3. Data Visualization:
        • Utilizes the Matplotlib library to create a visually appealing PDF table.
        • The generated PDF, named 'companies.pdf', includes a table formatted columns and centered text.

### Usage:
    1. Ensure that the required libraries ('BeautifulSoup', 'tabulate', 'matplotlib', 'requests', 'pandas') are installed.
    2. Run the script using the command: 'python project.py'
    3. Review the printed table in the console and find the generated CSV file ('companies.csv') for detailed datad.
    4. Acess the visual representation in the PDF file ('companies.pdf')

### Libraries used:
    • BeautifulSoup → for web scraping and HTML parsing
    • Tabulate → to format the DataFrame as a table in the console
    • Matplotlib → to create visualization, specifically a PDF table
    • Requests → to retrieve content from a URL
    • Pandas → for data manipulation and CSV file creation

### Notes:
    This script provides a simple yet effective way to fetch, organize and visualize tabular data from a webpage. Feel free to customize it further based on your needs or use it as a foundation for similar projects.
