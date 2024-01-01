from diffusers import AutoPipelineForText2Image
import torch

pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
# pipe.to("cuda")
pipe.to("mps")

# prompt = "A cinematic shot of a baby racoon wearing an intricate italian priest robe."
# prompt = "a photo of an astronaut riding a horse on mars"
# prompt = "A lazy idiot is riding a pig"
prompt = "A beautiful golden gradient cat wearing red clothes"

image = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]

# 写到本地
image.save("output.png")
