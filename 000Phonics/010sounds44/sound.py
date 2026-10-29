import os
import subprocess

output_mp3 = "all_merge_with_pause.mp3"
pause_sec = 0.5  # 每个单词之间停顿0.5秒

def main():
    mp3_files = sorted([f for f in os.listdir(os.getcwd()) if f.lower().endswith(".mp3")])
    if not mp3_files:
        print("❌ 没有找到mp3")
        input()
        return

    inputs = []
    filter_parts = []
    for i, f in enumerate(mp3_files):
        inputs += ["-i", f]
        filter_parts.append(f"[{i}:a]")

    filter_str = "".join(filter_parts) + f"concat=n={len(mp3_files)}:v=0:a=1,apad=pad_dur={pause_sec}"
    cmd = [
        "ffmpeg", "-y",
        *inputs,
        "-filter_complex", filter_str,
        "-c:a", "libmp3lame", "-b:a", "192k",
        output_mp3
    ]
    print("开始合并，带静音间隔...")
    subprocess.run(cmd, check=True)
    print("✅ 完成！")
    input()

if __name__ == "__main__":
    main()
