from ffmpeg.convert import (convert_audio_command,
                            verify_audio_input_format,
                            verify_audio_output_format)

def test_verify_audio_input_format_good():
    result = verify_audio_input_format('mp3')
    assert result == True

def test_verify_audio_input_format_bad():
    result = verify_audio_input_format('no_such_format')
    assert result == False

def test_verify_audio_output_format_good():
    result = verify_audio_input_format('mp3')
    assert result == True

def test_verify_audio_output_format_bad():
    result = verify_audio_input_format('no_such_format')
    assert result == False

def test_convert_audio_command():
	command = convert_audio_command(
		'ffmpeg', 'soundfile.wav', 'mp3', 'soundfile.mp3')
	assert command == 'ffmpeg -i soundfile.wav -f mp3 soundfile.mp3'

