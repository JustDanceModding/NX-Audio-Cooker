import os

os.makedirs("input/", exist_ok=True)
os.makedirs("output/", exist_ok=True)

print("Audio Encoder for NX by JustDanceModding (Tool By Sen)\nDISCLAMER: This Data Structure is wrong. The audio will work anyways, but it wont be as optimized as an Eliott's one from UbiArtPY.\nThis tool was last modified on: 11 July 2023 at 1:33:25 PM")

for audio in os.listdir("input/"):
    print(audio)
    os.makedirs("temp", exist_ok=True)
    ckd = audio.split(".")[0] + ".wav.ckd"
    os.system(F'ffmpeg.exe -i "input\\{audio}" -f wav -bitexact -acodec pcm_s16le -ar 48000 -ac 2 -loglevel quiet "temp/temp.wav"')

    with open(f"output/{ckd}", "wb") as output:
        with open(f"temp/temp.wav", "rb") as wav:
            wav.seek(0x10)
            output.write(b'RAKI\x0B\x00\x00\x00Nx  pcm \x5A\x00\x00\x00\x60\x00\x00\x00\x03\x00\x00\x00\x03\x00\x00\x00fmt \x44\x00\x00\x00\x12\x00\x00\x00AdIn\x56\x00\x00\x00\x04\x00\x00\x00data\x60\x00\x00\x00' + wav.read())
