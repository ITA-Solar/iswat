# ISWAT Webpage Setup

This repository contains the webpage structure for the ISWAT Action Team meeting.

## Editable Document Link
Here is the link to the editable Google Doc for the meeting schedule/programme:
- [Google Doc Programme](https://docs.google.com/document/d/1T1GFa1yjDoFuYuN3eXoAWU8-zD8ygieP03vuQOjJiSE/edit?usp=sharing)

---

## Quick Guide: How to Maintain & Update the Webpage

### 1. Make Content Edits
* All text files live inside the `docs/` directory. 
* Edit [index.md](docs/index.md), [schedule.md](docs/schedule.md), or [venue.md](docs/venue.md) directly using standard Markdown.
* To edit general titles or navigation paths, open [mkdocs.yml](mkdocs.yml).

### 2. Test Your Changes Locally
Start a temporary visualization container to proofread edits:
```bash
mkdocs serve
```
Go to **`http://127.0.0.1:8000`** in any web viewport. 

### 3. Push Upstream & Deploy
Once you approve of the changes:
```bash
# Stage your work
git add .

# Save with descriptions
git commit -m "Summarize adjustments here"

# Sync cloud servers
git push origin main

# Publish directly to GitHub Pages
mkdocs gh-deploy
```
