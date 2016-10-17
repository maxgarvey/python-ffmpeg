from source.shell import run

def test_run_method():
    return_value, output = run('echo "Hello"')
    assert return_value == 0
    assert output == ['Hello\n']

def test_bad_run_method():
    return_value, output = run('not-a-real-binary')
    assert return_value == 127
    assert output == ['/bin/sh: 1: not-a-real-binary: not found\n']
