# Resumir

A wrapper script that extends [resume.md](https://github.com/mikepqr/resume.md) to manage multiple job applications.

```
usage: resumir.py [-h] [-j JOB_LINK] resume_name

positional arguments:
  resume_name           An identifier used as the directory name for the new resume.

optional arguments:
  -h, --help            show this help message and exit
  -j JOB_LINK, --job_link JOB_LINK
                        A web address of the job posting, to be scraped and saved.
```

`$ python resumir.py software_developer_texas -j https://www.somejob.com`

### Details and Features

Resumir makes a new directory for each job saved.

* **Tailor resumes** to each job application
* **Use a resume template** to save time
* **Save job postings** to remember what you applied for and what resume you used
* **Store resumes in version control** as a convenient backup
* **Barebones and file-based**; no web apps, no subscriptions, and searchable with `grep`

See the [walkthrough](walkthrough.md) for a step-by-step explanation.

### Setup

1. **Install Python Packages**

`$ pip install -r requirements.txt`

2. **Write Your [Resume](resume_template/README.md) Template**

```
$ cd resume_template

.
├── LICENSE
├── README.md
├── resume.css              EDIT THIS: The style of the resume.
├── resume.html
├── resume.md               EDIT THIS: The body of the resume.
├── resume.pdf
├── resume.png
└── resume.py
```
