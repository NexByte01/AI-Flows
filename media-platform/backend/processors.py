"""Media processing functions for image, audio, and video."""

import os
import subprocess
from PIL import Image

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")

# Maximum characters to capture from FFmpeg stderr on error
MAX_ERROR_LENGTH = 1000


def ensure_dirs():
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)


# --------------- Image Processing ---------------

IMAGE_FORMATS = ["jpg", "png", "webp", "bmp", "gif", "tiff"]


def process_image(input_path, output_format, quality=85, operation="convert"):
    """Compress or convert an image file.

    Args:
        input_path: Path to the source image.
        output_format: Target format (jpg, png, webp, etc.).
        quality: Quality level 1-100 (used for lossy formats).
        operation: 'compress' or 'convert'.

    Returns:
        output_path: Path to the resulting file.
    """
    ensure_dirs()
    base = os.path.splitext(os.path.basename(input_path))[0]
    fmt = output_format.lower().strip(".")
    if fmt == "jpg":
        fmt = "jpeg"
    out_ext = "jpg" if fmt == "jpeg" else fmt
    output_path = os.path.join(OUTPUT_DIR, f"{base}_output.{out_ext}")

    img = Image.open(input_path)

    # Convert mode for formats that don't support alpha
    if fmt in ("jpeg", "bmp") and img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    save_kwargs = {}
    if fmt in ("jpeg", "webp"):
        save_kwargs["quality"] = quality
        save_kwargs["optimize"] = True
    elif fmt == "png":
        save_kwargs["optimize"] = True

    img.save(output_path, format=fmt.upper(), **save_kwargs)
    return output_path


# --------------- Audio Processing ---------------

AUDIO_FORMATS = ["mp3", "wav", "ogg", "aac", "flac", "m4a"]


def process_audio(input_path, output_format, bitrate="128k", operation="convert"):
    """Compress or convert an audio file using FFmpeg.

    Args:
        input_path: Path to the source audio.
        output_format: Target format (mp3, wav, ogg, etc.).
        bitrate: Audio bitrate (e.g., '128k', '64k').
        operation: 'compress' or 'convert'.

    Returns:
        output_path: Path to the resulting file.
    """
    ensure_dirs()
    base = os.path.splitext(os.path.basename(input_path))[0]
    fmt = output_format.lower().strip(".")
    output_path = os.path.join(OUTPUT_DIR, f"{base}_output.{fmt}")

    cmd = ["ffmpeg", "-y", "-i", input_path]

    if fmt == "mp3":
        cmd += ["-codec:a", "libmp3lame", "-b:a", bitrate]
    elif fmt == "ogg":
        cmd += ["-codec:a", "libvorbis", "-b:a", bitrate]
    elif fmt == "aac" or fmt == "m4a":
        cmd += ["-codec:a", "aac", "-b:a", bitrate]
    elif fmt == "flac":
        cmd += ["-codec:a", "flac"]
    elif fmt == "wav":
        cmd += ["-codec:a", "pcm_s16le"]
    else:
        cmd += ["-b:a", bitrate]

    cmd.append(output_path)

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg audio error: {result.stderr[:MAX_ERROR_LENGTH]}")

    return output_path


# --------------- Video Processing ---------------

VIDEO_FORMATS = ["mp4", "webm", "avi", "mkv", "mov", "flv"]


def process_video(input_path, output_format, crf=28, resolution=None, operation="convert"):
    """Compress or convert a video file using FFmpeg.

    Args:
        input_path: Path to the source video.
        output_format: Target format (mp4, webm, avi, etc.).
        crf: Constant Rate Factor for quality (lower = better, 0-51).
        resolution: Optional resolution like '1280x720'.
        operation: 'compress' or 'convert'.

    Returns:
        output_path: Path to the resulting file.
    """
    ensure_dirs()
    base = os.path.splitext(os.path.basename(input_path))[0]
    fmt = output_format.lower().strip(".")
    output_path = os.path.join(OUTPUT_DIR, f"{base}_output.{fmt}")

    cmd = ["ffmpeg", "-y", "-i", input_path]

    if fmt == "mp4":
        cmd += ["-codec:v", "libx264", "-crf", str(crf), "-codec:a", "aac"]
    elif fmt == "webm":
        cmd += ["-codec:v", "libvpx", "-crf", str(crf), "-b:v", "1M", "-codec:a", "libvorbis"]
    elif fmt == "avi":
        cmd += ["-codec:v", "mpeg4", "-q:v", str(max(1, crf // 5)), "-codec:a", "libmp3lame"]
    elif fmt == "mkv":
        cmd += ["-codec:v", "libx264", "-crf", str(crf), "-codec:a", "aac"]
    elif fmt == "mov":
        cmd += ["-codec:v", "libx264", "-crf", str(crf), "-codec:a", "aac"]
    elif fmt == "flv":
        cmd += ["-codec:v", "flv1", "-codec:a", "libmp3lame"]

    if resolution:
        w, h = resolution.split("x")
        cmd += ["-vf", f"scale={w}:{h}"]

    cmd.append(output_path)

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg video error: {result.stderr[:MAX_ERROR_LENGTH]}")

    return output_path
