from ffmpeg.convert import ConvertAudioException
from lib import convert_audio
from utils import compare_files, clean_output, file_exists

# binary location
ffmpeg_binary = '/usr/local/bin/ffmpeg'

# argument defaults
# files
input_file = 'test/integration/inputs/basic_loop.m4a'
output_file = 'test/integration/outputs/basic_loop.wav'
expected_file = 'test/integration/expected/basic_loop.wav'

# format
desired_format = 'wav'

def test_convert_audio_success():
	convert_audio(ffmpeg_binary, input_file, desired_format, output_file)

	same_file = compare_files(output_file, expected_file)
		
	assert same_file
	clean_output()

def test_convert_audio_failure():
	desired_format = 'ttt'

	try:
		convert_audio(ffmpeg_binary, input_file, desired_format, output_file)
	except ConvertAudioException:
		pass

	new_file_exists = file_exists(output_file)
	assert (new_file_exists == False)
