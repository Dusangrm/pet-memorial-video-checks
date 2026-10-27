import json, os, re, subprocess, sys
probe = subprocess.run([
    os.environ.get("FFMPEG_PATH", "ffmpeg"), "-hide_banner", "-i", sys.argv[1]
], capture_output=True, text=True).stderr
size = re.search(r"Video:[^\n]*? (\d{2,5})x(\d{2,5})", probe)
duration = re.search(r"Duration: (\d+):(\d+):([\d.]+)", probe)
if not size or not duration:
    raise SystemExit("No readable video metadata")
hours, minutes, seconds = map(float, duration.groups())
print(json.dumps({"width": int(size[1]), "height": int(size[2]),
    "duration_seconds": hours * 3600 + minutes * 60 + seconds,
    "has_audio": "Audio:" in probe}))
