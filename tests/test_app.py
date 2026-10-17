from app import add, app


def test_add():
    assert add(2, 3) == 5


def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_home_flag_off(monkeypatch):
    monkeypatch.delenv("FEATURE_NEW_UI", raising=False)
    assert b"new look" not in app.test_client().get("/").data
