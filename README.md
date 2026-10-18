# clouviq-app

The demo app of the GitHub Masterclass: a tiny Flask service with tests, a Dockerfile and a feature flag.

| Endpoint | Returns |
|---|---|
| `/` | page with the version (`APP_VERSION`); `FEATURE_NEW_UI=true` switches the title |
| `/health` | `{"status": "ok", "version": ...}` |

```bash
pip install -r requirements.txt
pytest -q
python app.py   # http://localhost:8080
```
Questions? Open an issue on GitHub.

Found a bug? Add a failing test first.
Check it: curl localhost:8080/health
Run in Docker: docker build -t clouviq-app . && docker run -p 8080:8080 clouviq-app
Run the tests: pytest -q
Prefer the terminal? Open a pull request with: gh pr create
