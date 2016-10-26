from lib import convert_audio
from utils import compare_files

def test_convert_audio_success():
	convert_audio(
		'/usr/local/bin/ffmpeg', 'test/integration/inputs/basic_loop.m4a',
		'wav', 'test/integration/outputs/basic_loop.wav',
	)
	same_file = compare_files(
		'test/integration/outputs/basic_loop.wav',
		'test/integration/expected/basic_loop.wav',
	)
	assert same_file
