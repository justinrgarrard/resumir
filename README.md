# Resumir

A wrapper script that extends [resume.md](https://github.com/mikepqr/resume.md) to manage multiple job applications.


### Details and Features

Resumir makes a new directory for each job saved.

* **Tailor resumes** to each job application
* **Use a resume template** to save time
* **Save job postings** to remember what you applied for and what resume you used
* **Store resumes in version control** as a convenient backup
* **Barebones and file-based**; no web apps, no subscriptions, and searchable with `grep`


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


### Usage

***Create/Update a Resume***

`$ python resumir.py <resume_dir_name>`

***Create/Update a Resume + Save a Copy of the Job Posting***

`$ python resumir.py <resume_dir_name> -j <job_posting_link>`

See the [walkthrough](walkthrough.md) for a step-by-step explanation.
