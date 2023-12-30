from diffusers import StableDiffusionInpaintPipeline
import PIL
import requests
import torch
from io import BytesIO

pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-inpainting",
    torch_dtype=torch.float16,
)
# pipe.to("cuda")
pipe.to("mps")

def download_image(url):
    response = requests.get(url)
    return PIL.Image.open(BytesIO(response.content)).convert("RGB")


img_url = "https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png"
mask_url = "https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png"


init_image = download_image(img_url).resize((512, 512))
mask_image = download_image(mask_url).resize((512, 512))


prompt = "Face of a yellow cat, high resolution, sitting on a park bench"
#image and mask_image should be PIL images.
#The mask structure is white for inpainting and black for keeping as is
image = pipe(prompt=prompt, image=init_image, mask_image=mask_image).images[0]
image.save("./yellow_cat_on_park_bench.png")
