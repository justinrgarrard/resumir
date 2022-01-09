# Example Walkthrough

1. ***Create a Resume***

```
$ python resumir.py hadoop_developer_general_motors -j https://www.somelink.com
---Resume Does Not Exist | Creating Resume---
---Resume Created---
---Collecting Job Posting---
---Job Posting Collected---
```

2. ***Tweak the [Resume](resume_template/README.md)***

```
$ cd hadoop_developer_general_motors

.
├── job_posting.html        
├── LICENSE
├── posting_link.txt        
├── README.md
├── resume.css              EDIT THIS: The style of the resume.
├── resume.html
├── resume.md               EDIT THIS: The body of the resume.
├── resume.pdf
├── resume.png
└── resume.py
```

3. ***Regenerate the PDF***

```
$ python resumir.py hadoop_general_motors

---Resume Exists | Updating Resume---
Wrote /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.html
Found Chrome or Chromium at /usr/bin/google-chrome
Wrote /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.pdf
CompletedProcess(args='/usr/bin/python3 /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.py /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.md', returncode=0)
---Resume Updated---
```