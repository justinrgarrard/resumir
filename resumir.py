"""
A wrapper over resume.py for managing multiple job applications.

- jrgarrar
"""

# Library Imports
import re
import os
import sys
import shutil
import pathlib
import requests
import argparse
import subprocess
from bs4 import BeautifulSoup

# Globals
PARENT_DIR = pathlib.Path(__file__).parent.absolute()
RESUME_TEMPLATE_PATH = os.path.join(PARENT_DIR, 'resume_template')
PYTHON = sys.executable


def parse_args():
    """
    Parse input arguments and return them as a dict-like object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "resume_name",
        help="An identifier used as the directory name for the new resume."
    )
    parser.add_argument(
        "-j",
        "--job_link",
        help="A web address of the job posting, to be scraped and saved."
    )
    args = parser.parse_args()
    return args


def update_resume_dir(target_path):
    """
    Update a resume directory.
    """
    cmd = f'{PYTHON} {target_path}/resume.py {target_path}/resume.md'
    print(subprocess.run(cmd, shell=True, check=True))


def yoink_job_page(target_path, job_link):
    """
    Collect and store web page data from a URL.
    """
    # Save the link in one file
    link_path = os.path.join(target_path, 'posting_link.txt')
    with open(link_path, 'w') as f:
        f.write(job_link)

    # Save the web page in another file
    page_data = requests.get(job_link).text
    raw_output_path = os.path.join(target_path, 'job_posting_raw.html')
    with open(raw_output_path, 'w') as f:
        f.write(page_data)

    # Attempt to extract text elements only from the page
    soup = BeautifulSoup(page_data, 'html.parser')
    page = soup.getText()
    page = re.sub(r'\n+', '\n', page)
    output_path = os.path.join(target_path, 'job_posting.txt')
    with open(output_path, 'w') as f:
        f.write(page)


def main(resume_name, job_link):
    """
    Create or update a resume directory.
    """
    # Check if the resume exists
    target_path = os.path.join(PARENT_DIR, resume_name)
    resume_exists = os.path.isdir(target_path)

    # Rebuild the resume if it exists
    if resume_exists:
        print('---Resume Exists | Updating Resume---')
        update_resume_dir(target_path)
        print('---Resume Updated---')

    # Copy the template directory if the resume doesn't exist
    else:
        print('---Resume Does Not Exist | Creating Resume---')
        shutil.copytree(RESUME_TEMPLATE_PATH, target_path)
        print('---Resume Created---')

    # If a job link is provided, yoink the web page and save it
    if job_link is not None:
        print('---Collecting Job Posting---')
        yoink_job_page(target_path, job_link)
        print('---Job Posting Collected---')


if __name__ == '__main__':
    args = parse_args()
    main(args.resume_name, args.job_link)
