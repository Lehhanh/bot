# OptiBot Mini-Clone

A daily job that scrapes the OptiSigns Help Center, converts each article to clean Markdown, and syncs them into an OpenAI vector store — powering a `file_search`-based support assistant that answers questions with cited article URLs.

**Pipeline:** `scraper.py` (Zendesk API → Markdown) → `uploader.py` (upload delta to vector store) → `ask.py` (query with citations). `main.py` chains scrape + upload for the daily job.

## Setup

1. **Configure environment** — copy the sample and fill in real values:
   ```bash
   cp .env.sample .env
   ```
   | Variable | Required | Description |
   |---|---|---|
   | `OPENAI_API_KEY` | yes | Used to create the vector store and upload articles |
   | `ZENDESK_LOCALE` | no | Help Center locale, default `en-us` |
   | `SCRAPE_LIMIT` | no | Max articles to scrape, default `30` |
   | `VECTOR_STORE_NAME` | no | Vector store name on first creation, default `optisigns-support-docs` |
   | `OPENAI_MODEL` | no | Model used by `ask.py`, default `gpt-5.6` |
   | `GEMINI_API_KEY` / `GEMINI_FILE_SEARCH_STORE_NAME` | no | Reserved for a Gemini-based store (extra credit) |

2. **Build the Docker image:**
   ```bash
   docker build -t optibot .
   ```

## How to run locally

Run the daily job (scrape → upload delta) in a container, mounting `articles/` so the manifest and vector-store id persist between runs:

```bash
docker run --rm --env-file .env -v "$(pwd)/articles:/app/articles" optibot
```

On PowerShell, replace `$(pwd)` with `${PWD}`.

Ask the assistant a question using the same image:

```bash
docker run --rm --env-file .env -v "$(pwd)/articles:/app/articles" \
  optibot python ask.py "How do I connect a Zoom Room to OptiSigns?"
```

## Daily job logs

Scheduled once per day via GitHub Actions (`.github/workflows/daily-job.yml`). Each run builds the image, runs the job (exits 0), then commits the updated state (`manifest.json` + vector-store id) back to the repo so the next run only uploads what changed.

**Logs:** `https://github.com/<user>/<repo>/actions/workflows/daily-job.yml`

> Setup: add `OPENAI_API_KEY` under **Settings → Secrets and variables → Actions**. The `SCRAPE_LIMIT`, `VECTOR_STORE_NAME`, and `OPENAI_MODEL` values are set inline in the workflow.

## Sample question screenshot

![Assistant answering a sample question with cited URLs](docs/sample-question.png)

*(Run the `ask.py` command above and drop a screenshot of the answer + cited sources at `docs/sample-question.png`.)*
