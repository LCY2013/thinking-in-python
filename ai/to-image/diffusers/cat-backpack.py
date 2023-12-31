from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"
# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("mps")

pipe.load_textual_inversion("sd-concepts-library/cat-toy")

# prompt = "A <cat-toy> backpack"
prompt = "A beautiful golden gradient cat wearing red clothes"

image = pipe(prompt, num_inference_steps=50).images[0]
image.save("cat-backpack.png")
