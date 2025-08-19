import os
import torch
from huggingface_hub import login
from diffusers import FluxPipeline
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

login(token=os.getenv("HF_API_KEY"))

class FluxModel:
    def __init__(self, name: str, save_path: str, model: str):
        self.name = name
        self.save_path = save_path
        self.model = model
    
    def save_model(self):
        pipe = FluxPipeline.from_pretrained(self.name, torch_dtype=torch.bfloat16)
        pipe.save_pretrained(self.save_path)
        print(f"Model saved to {self.save_path}")
    
    def load_model(self):
        pipe = FluxPipeline.from_pretrained(self.save_path, torch_dtype=torch.bfloat16)
        return pipe
    
    def generate_image(self, prompt: str, file_name: str):
        pipe=self.load_model()
        image=  pipe(
            prompt, # the prompt to generate the image
            height=1024, # height of the generated image
            width=1024, # Width of the generated image
            guidance_scale=3.5,# how closely the image generation follows the prompt
            num_inference_steps=50, # Number of inference steps, larger the number better the image but will take more time
            max_sequence_length=512, # Max sequence length for the prompt
            generator=torch.Generator("cpu").manual_seed(0) # Seed for reproducibility
        ).images[0]
        image.save(f'./Images/{file_name}.png')
        