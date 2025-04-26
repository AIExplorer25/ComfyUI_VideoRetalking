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

# Add your node mappings
NODE_CLASS_MAPPINGS = {
    "ExampleNode": ExampleNode,
    "LoadVideoAudioNode": LoadVideoAudioNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExampleNode": "Example Node",
    "LoadVideoAudioNode": "Load Video and Audio Node",
}