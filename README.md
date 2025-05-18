
# Hacker News Crawler

A functional‑first Python web crawler that scrapes the top 30 posts from [Hacker News](https://news.ycombinator.com), lets you filter them by title length, and logs every run for basic usage analytics using a file-based SQLite database.

---

## Project Structure

```

hackernews\_crawler/
├── hn\_crawler/
│   ├── crawler.py
│   ├── filterer.py
│   ├── logger.py          # logs to SQLite
│   ├── models.py          # SQLAlchemy model
│   ├── db.py              # engine/session for SQLite
│   └── main.py
├── usage.db               # auto‑created SQLite file (excluded via .gitignore)
├── requirements.txt
├── env.tpl                # environment variable template
├── .env                   # symlink or copy of env.tpl (git-ignored)
└── README.md

````

---

## Features

| Feature          | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Scraping**     | Pulls rank, title, points, and comment count for the first 30 HN items.     |
| **Two filters**  | • `filter1` – titles **more than 5 words**, ordered by **comments** (desc)  <br> • `filter2` – titles **≤ 5 words**, ordered by **points** (desc) |
| **Usage logging**| Logs timestamp, filter type, runtime, and result count to an SQLite file.   |
| **Functional core** | Pure, testable functions with wrapper classes for clarity.               |

---

## Requirements

- **Python 3.9+**
- **[Pipenv](https://pipenv.pypa.io/en/latest/)** (recommended)

> 💡 Prefer `pip` + venv? Install from `requirements.txt` and activate the virtual environment normally.

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/hackernews-crawler.git
cd hackernews-crawler
````

### 2. Install Pipenv (if needed)

```bash
pip install --user pipenv
```

### 3. Create your local environment file

```bash
cp env.tpl env.dev
ln -s env.dev .env       # Optional but recommended
```

This sets the SQLite database path and other environment variables. If `.env` is missing, the crawler will still default to `./usage.db`.

### 4. Install dependencies and enter the environment

```bash
pipenv install
pipenv shell
```

> Use `exit` or `deactivate` to leave the environment.

---

##  Running the Crawler

```bash
# Filter 1 – titles with >5 words, ordered by comments
python -m hn_crawler.main filter1

# Filter 2 – titles with ≤5 words, ordered by points
python -m hn_crawler.main filter2
```

✅ Each execution logs metadata to `usage.db`, automatically creating the file and tables if they don’t exist.

---

## 🧪 Running Tests (if present)

If you’ve written tests with `pytest`:

```bash
pytest
```

---

## Roadmap / Future Improvements

| Feature           | Status     | Notes                                                |
| ----------------- | ---------- | ---------------------------------------------------- |
| Dockerize app     | 🚧 Planned | Add Dockerfile & Compose support                     |
| REST API          | 🚧 Planned | Use FastAPI to expose a `/filter` endpoint           |
| Job scheduler     | 🚧 Planned | Run crawler periodically via APScheduler             |
| CLI upgrade       | 🚧 Planned | Improve UX with `click` or `typer`                   |
| Analytics command | 🚧 Planned | CLI to query `usage.db` stats                        |
| CI/CD pipeline    | 🚧 Planned | GitHub Actions for linting, testing, and image build |

---

## Contributing

1. Fork the repo & create a branch:
   `git checkout -b feature/my-feature`
2. Commit your changes:
   `git commit -m 'Add feature X'`
3. Push to GitHub:
   `git push origin feature/my-feature`
4. Open a pull request

---

## License

MIT © 2025 Elijah Hunt

