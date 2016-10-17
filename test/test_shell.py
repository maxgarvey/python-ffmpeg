from source.shell import run

def test_run_method():
    return_value, output = run('echo "Hello"')
    assert return_value == 0
    assert output == ['Hello\n']
