# Import necessary libraries
import os
from huggingface_hub import hf_hub_download
import json
from rapidfuzz import process, fuzz
from huggingface_hub import list_models, HfApi
import subprocess
import sys

# Define your new classes or functions here
class ExampleNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "example_input": ("STRING", {"tooltip": "Enter an example input"}),
            },
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("example_output",)
    FUNCTION = "example_function"
    CATEGORY = "ExampleCategory"
    DESCRIPTION = "This is an example node"

    def example_function(self, example_input):
        # Example functionality
        return (f"Processed: {example_input}",)

class LoadVideoAudioNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "face_video": ("STRING", {"tooltip": "Enter the path to the face video file"}),
                "audio": ("STRING", {"tooltip": "Enter the path to the audio file"}),
                "output_filename": ("STRING", {"tooltip": "Enter the output file name"}),
            },
        }
    RETURN_TYPES = ("CLASS",)
    RETURN_NAMES = ("video_audio_data",)
    FUNCTION = "load_video_audio"
    CATEGORY = "LoadData"
    DESCRIPTION = "This node loads face video, audio, and output filename into a class"

    class VideoAudioData:
        def __init__(self, face_video, audio, output_filename):
            self.face_video = face_video
            self.audio = audio
            self.output_filename = output_filename

    def load_video_audio(self, face_video, audio, output_filename):
        # Create an instance of the VideoAudioData class with the provided inputs
        return (self.VideoAudioData(face_video, audio, output_filename),)

class RunInferenceNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "video_audio_data": ("CLASS", {"tooltip": "Provide the output of LoadVideoAudioNode"}),
            },
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_video_path",)
    FUNCTION = "run_inference"
    CATEGORY = "Inference"
    DESCRIPTION = "This node runs inference.py using the provided video, audio, and output filename"

    def run_inference(self, video_audio_data):
        # Extract inputs from the VideoAudioData class
        face_video = video_audio_data.face_video
        audio = video_audio_data.audio
        output_filename = video_audio_data.output_filename

        # Ensure the output folder exists
        output_folder = "output"
        os.makedirs(output_folder, exist_ok=True)

        # Construct the output file path
        output_video_path = os.path.join(output_folder, output_filename)

        # Construct the command to run inference.py
        command = [
            sys.executable,  # Use the current Python interpreter
            "inference.py",
            "--face", face_video,
            "--audio", audio,
            "--outfile", output_video_path,
        ]

        # Run the command
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Inference failed: {e}")

        # Return the path to the output video
        return (output_video_path,)


# Add your node mappings
NODE_CLASS_MAPPINGS = {
    "ExampleNode": ExampleNode,
    "LoadVideoAudioNode": LoadVideoAudioNode,
    "RunInferenceNode": RunInferenceNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExampleNode": "Example Node",
    "LoadVideoAudioNode": "Load Video and Audio Node",
    "RunInferenceNode": "Run Inference Node",
}
