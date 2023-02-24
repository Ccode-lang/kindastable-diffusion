import sys
import os
import torch
from diffusers import StableDiffusionPipeline

model_id = "stabilityai/stable-diffusion-2-1"

pipe = StableDiffusionPipeline.from_pretrained(model_id, revision="fp16", torch_dtype=torch.float16)
pipe = pipe.to("cuda")
pipe.enable_attention_slicing()
try:
    generator = torch.Generator("cuda").manual_seed(int(sys.argv[3]))
except:
    generator = torch.Generator("cuda")
prompt = sys.argv[1]
image = pipe(prompt, num_inference_steps=int(sys.argv[2]), generator=generator).images[0]

if not os.path.isdir("samples"):
    os.mkdir("samples")

image.save(os.path.join("samples", "'" + prompt + "'.png"))
