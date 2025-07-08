import comfy.sd
import comfy.model_management
import nodes
import torch

class EmptyChromaLatentImage:
    def __init__(self):
        self.device = comfy.model_management.intermediate_device()

    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "width": ("INT", {"default": 1024, "min": 64, "max": nodes.MAX_RESOLUTION, "step": 64}),
                              "height": ("INT", {"default": 1024, "min": 64, "max": nodes.MAX_RESOLUTION, "step": 64}),
                              "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096})}}
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "generate"

    CATEGORY = "latent/sd3"

    def generate(self, width, height, batch_size=1):
        latent = torch.zeros([batch_size, 16, height // 32, width // 32], device=self.device)
        return ({"samples":latent}, )



NODE_CLASS_MAPPINGS = {
    "EmptyChromaLatentImage": EmptyChromaLatentImage,
}
