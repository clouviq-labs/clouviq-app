from app import add, app


def test_add():
    assert add(2, 3) == 5


def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"
