from src.main import main

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert 'Hello' in captured.out

