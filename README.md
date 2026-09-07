# SuperHub — Where Stories Live

A Wattpad-style story platform built with pure Django + MongoDB.
Dark Gold theme inspired by "My Jannah" by Muhammad Mubarak Ahmed.

## Stack
- Python 3.11
- Django 4.2
- MongoDB via mongoengine
- Django sessions (no JWT needed)
- Tailwind CSS CDN
- HTMX CDN

## Quick Start

### 1. Prerequisites
- Python 3.11+
- MongoDB running on localhost:27017

### 2. Setup

```bash
cd superhub_django

# Create virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Copy env file
copy .env.example .env
```

### 3. Seed the database (My Jannah + author account)

```bash
python seed_myjannah.py
```

This creates:
- Author account: `mubarak@superhub.com` / `MyJannah2024!`
- Full "My Jannah" story with all 30 chapters

### 4. Run the server

```bash
python manage.py runserver
```

Open: http://localhost:8000

## Pages

| URL | Page |
|---|---|
| `/` | Home |
| `/browse/` | Browse all stories |
| `/auth/login/` | Login |
| `/auth/register/` | Register |
| `/stories/<id>/` | Story detail |
| `/stories/<id>/read/<chapter>/` | Read chapter |
| `/stories/create/` | Create story |
| `/stories/mine/` | My stories |
| `/auth/profile/<username>/` | User profile |
| `/interactions/reading-list/` | Reading list |

## Features
- Browse & search stories by title and genre
- Publish multi-chapter stories
- Beautiful reader with light sepia background
- Like stories (HTMX — no page reload)
- Comment on stories (HTMX)
- Save to reading list
- Follow/unfollow authors
- Full "My Jannah" book seeded and readable

## Featured Content
**My Jannah: The Story of Hauwa and Me**
by Muhammad Mubarak Ahmed (Mubarak Ahmed Alibaba)
*"A True Story. A Pure Love. A Beautiful Journey."*
30 chapters — fully readable on the platform.
