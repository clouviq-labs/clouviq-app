from app import app


def test_ping():
    r = app.test_client().get("/ping")
    assert r.status_code == 200
    assert r.data == b"pong"
