from shell import join_command, run
from ffmpeg.convert import convert_audio_command, ConvertAudioException

def convert_audio(ffmpeg_binary, input_file, output_format, output_file):
	command_pieces = convert_audio_command(
		ffmpeg_binary, input_file, output_format, output_file)
	command = join_command(command_pieces)
	return_value, return_output = run(command)
	if return_value == 0:
		print(
			'convert_audio::success: {output}'.format(
				output=return_output,
			)
		)
	else:
		raise ConvertAudioException(
			'error converting audio:\n{error}\n'.format(
				error=return_output,
			)
		)
