# Example Walkthrough

1. ***Create a Resume***

```
$ python resumir.py hadoop_developer_general_motors -j https://www.somelink.com
---Job App Does Not Exist | Creating Job App---
---Job App Created---
---Job App Exists | Updating Job App---
Wrote /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.html
Found Chrome or Chromium at /usr/bin/google-chrome
Wrote /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.pdf
CompletedProcess(args='/usr/bin/python3 /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.py /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.md', returncode=0)
Wrote /home/roy/vcs/resumir/hadoop_developer_general_motors/cover_letter.html
Found Chrome or Chromium at /usr/bin/google-chrome
Wrote /home/roy/vcs/resumir/hadoop_developer_general_motors/cover_letter.pdf
CompletedProcess(args='/usr/bin/python3 /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.py /home/roy/vcs/resumir/hadoop_developer_general_motors/cover_letter.md', returncode=0)
---Job App Updated---
---Collecting Job Posting---
---Job Posting Collected---
```

2. ***Tweak the [Resume](resume_template/README.md)***

```
$ cd applications/hadoop_developer_general_motors
.
├── cover_letter.css        EDIT THIS to change cover letter styling
├── cover_letter.md         EDIT THIS to change cover letter contents
├── job_posting.html   
├── posting_link.txt     
├── LICENSE
├── README.md
├── resume.css              EDIT THIS to change resume styling
├── resume.html
├── resume.md               EDIT THIS to change resume contents
├── resume.pdf
├── resume.png
└── resume.py
```

3. ***Regenerate the PDF's***

```
$ python resumir.py hadoop_general_motors

---Job App Exists | Updating Job App---
Wrote /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.html
Found Chrome or Chromium at /usr/bin/google-chrome
Wrote /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.pdf
CompletedProcess(args='/usr/bin/python3 /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.py /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.md', returncode=0)
Wrote /home/roy/vcs/resumir/hadoop_developer_general_motors/cover_letter.html
Found Chrome or Chromium at /usr/bin/google-chrome
Wrote /home/roy/vcs/resumir/hadoop_developer_general_motors/cover_letter.pdf
CompletedProcess(args='/usr/bin/python3 /home/roy/vcs/resumir/hadoop_developer_general_motors/resume.py /home/roy/vcs/resumir/hadoop_developer_general_motors/cover_letter.md', returncode=0)
---Job App Updated---
```