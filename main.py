import tkinter
import customtkinter
from pytube import YouTube


# Download video function
def start_download_video():
    try:
        yt_link = url_var.get()
        ytObject = YouTube(yt_link)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title)
        downloaded.configure(text="")
        video.download()
        print("Download started")
    except:
        downloaded.configure(text="Download error", text_color="red")

    downloaded.configure(text="Download complete")
    print("Download complete")


# Download audio function
def start_download_audio():
    try:
        yt_link = url_var.get()
        ytObject = YouTube(yt_link)
        audio = ytObject.streams.get_audio_only()

        title.configure(text=ytObject.title)
        downloaded.configure(text="")
        audio.download()
        print("Download started")

    except:
        downloaded.configure(text="Download error", text_color="red")

    downloaded.configure(text="Download complete")
    print("Download complete")


# Set the appearance mode and default color theme
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# Create the main window
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Dowloaded label
downloaded = customtkinter.CTkLabel(app, text="")
downloaded.pack()


# Download video button
download_video = customtkinter.CTkButton(
    app, text="Download", command=start_download_video
)
download_video.pack(padx=10, pady=10)

# Download audio button
download_audio = customtkinter.CTkButton(
    app, text="Download audio", command=start_download_audio
)
download_audio.pack(padx=10, pady=10)


# Run the main window
app.mainloop()
