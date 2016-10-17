import subprocess

def run(command):
    # execute command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    # collect output
    process_output = []
    for output_line in process.stdout.readlines():
        process_output.append(output_line)

    # wait for job to complete
    return_value = process.wait()

    return return_value, process_output

