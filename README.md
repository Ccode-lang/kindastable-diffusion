# kinda stable diffusion
Just some optimized stable diffusion scripts I made.

# calling from cmd
```bash
python <generator that you want to use>.py <prompt> <steps> [<seed>]
```

# PC specs needed
 * 8GB vram.
 * Cuda capable GPU.
 * Windows 10 or more.

# setting up
1. Install Cuda 11.7 or more
2. Install python 3 (I use 3.10)
3. Install PyTorch.
3. Run `pip install -r requirements.txt`
4. You are ready to go! (On first run (of each generator) it takes a while to start up because it downloads the model that it needs (if you want to uninstall these they are contained within the `.config` folder inside your home folder under transformers.))