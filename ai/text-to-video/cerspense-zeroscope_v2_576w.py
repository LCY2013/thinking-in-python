import torch
from PIL import Image
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

pipe = DiffusionPipeline.from_pretrained("cerspense/zeroscope_v2_576w", torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
# pipe.to("cuda")
pipe.to("mps")

prompt = "spiderman running in the desert"
video_frames = pipe(prompt, num_inference_steps=40, height=320, width=576, num_frames=24).frames
# safe low-res video
video_path = export_to_video(video_frames, output_video_path="./video_576_spiderman.mp4")

# let's offload the text-to-image model
pipe.to("cpu")

# and load the image-to-image model
pipe = DiffusionPipeline.from_pretrained(
    "cerspense/zeroscope_v2_XL", torch_dtype=torch.float16, revision="refs/pr/15"
)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()

# The VAE consumes A LOT of memory, let's make sure we run it in sliced mode
pipe.vae.enable_slicing()

# now let's upscale it
video = [Image.fromarray(frame).resize((1024, 576)) for frame in video_frames]

# and denoise it
video_frames = pipe(prompt, video=video, strength=0.6).frames
video_path = export_to_video(video_frames, output_video_path="./video_1024_spiderman.mp4")
video_path