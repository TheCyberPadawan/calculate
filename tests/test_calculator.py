import calculator.calculator as app

def test_search_pappers(monkeypatch, capsys):
    """Teste la fonction search_pappers sans appeler l'API réelle."""
    def fake_get(url, params=None, headers=None):
        class FakeResponse:
            status_code = 200
            def json(self):
                return {"resultats": [{"nom": "Fake Company"}]}
        return FakeResponse()
    
    # On patch l'objet requests importé dans le module app
    monkeypatch.setattr(app.requests, "get", fake_get)

    # On appelle la fonction
    app.search_pappers("fake")

    # On capture la sortie standard
    captured = capsys.readouterr()
    assert "Fake Company" in captured.out

def test_ascii_art_in_output(capsys, monkeypatch):
    """Vérifie que l'ASCII art est affiché au lancement."""
    monkeypatch.setattr("builtins.input", lambda _: "quit")

    app.main()
    captured = capsys.readouterr()
    assert "/$$$$$$$" in captured.out
    assert "Bienvenue sur Papers CLI" in captured.out
