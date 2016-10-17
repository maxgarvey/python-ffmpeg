from source.shell import run, join_command

def test_run_method():
    return_value, output = run('echo "Hello"')
    assert return_value == 0
    assert output == ['Hello\n']

def test_bad_run_method():
    return_value, output = run('not-a-real-binary')
    assert return_value == 127
    assert output == ['/bin/sh: 1: not-a-real-binary: not found\n']

def test_join():
    command_elements = ['ls', '-lah', 'dir_name']
    command = join_command(command_elements)
    assert command == 'ls -lah dir_name'
