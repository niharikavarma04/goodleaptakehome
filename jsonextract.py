# using requests library to make http/api call
import requests

# suggested github api url
GITHUB_API_URL = "https://api.github.com/repos/nodejs/node"
OUTPUT_FILE = "summary_output.txt"

# function to fetch data from api
def fetch_repo_data(url):
    try:
        # To make a GET request to the API with a 10-second timeout
        response = requests.get(url, timeout=10)
        # To raise an exception if the response code is not 200
        response.raise_for_status()
        # To parse and return the JSON data from the response
        return response.json()
    except requests.RequestException as e:
        # To print any error that occurs during the api call
        print(f"Error fetching data: {e}")
        return None

# Function to extract meaningful information
def summarize_repo_info(data):
    # If there is no data, it will return a default message
    if not data:
        return "No data to summarize."
    # To create a dictionary of fields
    summary = {
        "Repository Name": data.get("full_name"),
        "Description": data.get("description"),
        "Stars": data.get("stargazers_count"),
        "Forks": data.get("forks_count"),
        "Open Issues": data.get("open_issues_count"),
        "Watchers": data.get("watchers_count"),
        "License": data.get("license", {}).get("name", "None"),
        "Default Branch": data.get("default_branch"),
        "Last Updated": data.get("updated_at")
    }

    lines = ["\nGitHub Repository Summary:\n" + "-"*30]
    for key, value in summary.items():
        # To add each key-value pair to the list
        lines.append(f"{key}: {value}")
        # To join and return the lines as a single string
    return "\n".join(lines)

# Function to write the summary to a file
def write_to_file(content, filename):
    try:
        # To open the file in write mode
        with open(filename, "w") as f:
            # To write the content to the file
            f.write(content)
        print(f"\nSummary written to {filename}")
    except IOError as e:
        # To handle file I/O errors
        print(f"Failed to write to file: {e}")

# Heart of the script
def main():
    # To fetch the JSON data from GitHub
    data = fetch_repo_data(GITHUB_API_URL)
    # To create a human-readable summary from the JSON
    summary = summarize_repo_info(data)
    print(summary)
    # To save the summary to a file
    write_to_file(summary, OUTPUT_FILE)

# Will run the main function when this script is executed
if __name__ == "__main__":
    main()
