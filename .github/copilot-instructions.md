# Copilot instructions for clouviq-app

clouviq-app is a small Flask API. Tests use pytest.

## When you review a pull request
- Flag any SQL built with f-strings or string concatenation.
- Every new route needs a test in tests/.
- Point out secrets, tokens or account IDs in code or logs.

## When you write code
- Run `pytest -q` and make it pass before you finish.
- Keep changes small: one issue, one pull request.
- Pin every new action to a full commit SHA.
