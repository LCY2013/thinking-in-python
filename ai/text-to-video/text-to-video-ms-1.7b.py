import torch
from diffusers import DiffusionPipeline
from diffusers.utils import export_to_video

pipe = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
# pipe = DiffusionPipeline.from_pretrained("CompVis/ldm-text2im-large-256")
# pipe = pipe.to("cuda")
pipe = pipe.to("mps")

prompt = "Spiderman is surfing"
video_frames = pipe(prompt).frames
video_path = export_to_video(video_frames)
video_path
