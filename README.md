# GoodLeap SRE take home Assignment

## ✅ Overview

This script parses json response from the GitHub API for the `nodejs/node` repo and summarizes it for observability and reliability analysis.

---

## 🛠️ How to Run (Python 3)

   1. Create virtual environment
      python3 -m venv venv
      source venv/bin/activate 
   
   2. Install dependencies 
       pip3 install requests

   3. Run the script
       python3 github_repo_summary.py

   4. View saved output
       cat summary_output.txt

🐳 Docker commands to run the containerized script
   1. On the root directory of the application run the command below
      docker build -t github-summary .
   
   2. Once the image is built to run the container run the command below
      docker run github-summary

   3. To run and remove the container after run the command below
      docker run --rm github-summary

   4. To mount a local folder to get output file run the command below
      docker run --rm -v "$PWD":/app github-summary

## Unit Tests
   1. To run unit tests, run the below command
      python3 -m unittest jsonextract_tests

## API Used
    GitHub Repository Endpoint:
      https://api.github.com/repos/nodejs/node

## Assumptions
    1. API does not require authentication or exceed rate limits.

    2. Network access is available.

    3. Python 3+ environment is used.

    4. Docker is currently installed and running on your machine