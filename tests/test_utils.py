from cubao_python.utils import sample1, sample2


def test_sample1():
    assert sample1() == 'sample1'

def test_sample2():
    assert sample2() == 'sample2'

def pytest_main(dir: str, *, test_file: str = None):
    import pytest
    # pytest test_cli.py
    # pytest --capture=tee-sys test_cli.py
    np.set_printoptions(suppress=True)
    os.chdir(dir)
    # https://docs.pytest.org/en/6.2.x/usage.html#calling-pytest-from-python-code
    sys.exit(
        pytest.main([
            dir,
            *(['-k', test_file] if test_file else []),
            '--capture',
            'tee-sys',
            '-vv',
            '-x',
        ]))  

if __name__ == "__main__":
    pytest_main()