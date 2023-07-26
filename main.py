import tkinter as tk
from pytube import YouTube
from threading import *


def destroy_window(window):
    for widget in window.winfo_children():
        widget.destroy()


def main_window():
    destroy_window(window)

    # Setting up main window
    button_frame = tk.Frame(window, width=50, height=100)
    button_frame.config(relief="raised", border=2, bg="#313232")
    button_frame.pack(expand=True, fill="both", padx=50, pady=50, anchor="center")

    main_tittle = tk.Label(window, text="YOUTUBE VIDEO DOWNLOADER")
    main_tittle.config(
        font=("roboto", 12, "bold"),
        bg="grey",
        fg="white",
        relief="raised",
        border=0.5,
        padx=10,
        pady=10,
    )

    button_mp3 = tk.Button(
        button_frame, text="MP3 Downloader", command=mp3_downloader_ui
    )
    button_mp3.config(font=("roboto", 12, "bold"), width=25, height=3, anchor="center")

    button_mp4 = tk.Button(
        button_frame, text="Video Downloader", command=video_downloader_ui
    )
    button_mp4.config(font=("roboto", 12, "bold"), width=25, height=3, anchor="center")

    # Packing itens
    main_tittle.pack(pady=20, side="top", anchor="n")
    button_mp3.pack(pady=30)
    button_mp4.pack(pady=25)

    window.mainloop()


def video_downloader_ui():
    def threading_video():
        # Call work function
        t2 = Thread(target=download_youtube_video)
        t2.start()

    # Download from youtube function
    def download_youtube_video():
        try:
            # Getting URL from textbox
            url = linkbox.get()
            yt = YouTube(
                url,
                use_oauth=True,
                allow_oauth_cache=True,
                # on_progress_callback=progress_func, can be used to make a progress bar...
                # on_complete_callback=complete_func, can be used to notify when it's complete
            )

            # Getting Channel name by URL
            channel_name_index = url.rfind("=")

            # Putting file extension after name
            output_file = url[channel_name_index::] + "_" + "video.mp4"

            # Setting resolution and downloading
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path="video", filename=output_file.replace("=", ""))

            # Remaking the window to prevent double status
            video_downloader_ui()

        except Exception as error:
            # Print the error in terminal for better understandment
            print(error)

            # Remaking the window to prevent double status
            video_downloader_ui()

            # Showing status
            status = tk.Label(window, text="Download Fail")
            status.config(font=("roboto", 10, "bold"), fg="red", bg="#313232")
            status.pack(anchor="center", side="top", pady=10)

    # Deleting things that are on the screen
    destroy_window(window)

    # main page frame
    main_frame = tk.Frame(window, width=50, height=100)
    main_frame.config(relief="raised", border=2, bg="#313232")
    main_frame.pack(expand=True, fill="both", padx=50, pady=20, anchor="center")

    # Creating main menu
    tittle = tk.Label(main_frame, text="YOUTUBE VIDEO DOWNLOADER")
    tittle.config(
        font=("roboto", 12, "bold"),
        bg="grey",
        fg="white",
        relief="raised",
        border=0.5,
        padx=10,
        pady=10,
    )

    # Url label
    insertlink = tk.Label(main_frame, text="Insert your link from youtube:")
    insertlink.config(
        font=("roboto", 10, "bold"),
        bg="grey",
        fg="white",
        relief="raised",
        border=0.5,
        padx=10,
        pady=10,
    )

    # URL box
    linkbox = tk.Entry(main_frame, width=40)

    # On click download
    button = tk.Button(main_frame, text="Download", command=threading_video)
    button.config(
        width=15,
        height=1,
        pady=5,
        fg="green",
        bg="white",
        relief="raised",
        border=5,
        font=("montserrat", 10, "bold"),
    )

    # Return Button
    button_return = tk.Button(window, text="Return", command=main_window)
    button_return.config(
        width=13,
        height=1,
        pady=5,
        fg="black",
        bg="white",
        relief="raised",
        borderwidth=5,
        border=5,
        font=("montserrat", 9, "bold"),
    )

    # Credits Label
    creator = tk.Label(window, text="By Gustavo Gorges")
    creator.config(
        font=("montserrat", 8, "bold"),
        bg="#313232",
        fg="white",
        relief="sunken",
        border=0.5,
        padx=10,
        pady=10,
    )

    # Packing itens
    tittle.pack(pady=20)
    insertlink.pack(pady=10)
    linkbox.pack(pady=10)
    button.pack()
    creator.pack(side="bottom", pady=8)
    button_return.pack(side="bottom", pady=8)


def mp3_downloader_ui():
    def threading_music():
        # Call work function
        t1 = Thread(target=download_mp3youtube)
        t1.start()

    # Download from youtube function
    def download_mp3youtube():
        try:
            # Getting URL from textbox
            url = linkbox.get()

            # Getting Channel name by URL
            channel_name_index = url.rfind("=")

            # Putting file extension after name
            output_file = url[channel_name_index::] + "_" + "audio.mp3"

            yt = YouTube(url)

            # Setting resolution and downloading

            stream = yt.streams.get_audio_only()
            stream.download(output_path="music", filename=output_file.replace("=", ""))

            # Preventing double status
            mp3_downloader_ui()

            # Showing status
            status = tk.Label(window, text="Download Complete")
            status.config(font=("roboto", 10, "bold"), fg="green", bg="#313232")
            status.pack(anchor="center", side="top", pady=10)

        except Exception as error:
            print(error)

            # Preventing double status
            mp3_downloader_ui()

            # Preventing double status
            status = tk.Label(window, text="Download Fail")
            status.config(font=("roboto", 10, "bold"), fg="red", bg="#313232")
            status.pack(anchor="center", side="top", pady=10)

    # Deleting things that are on the screen
    destroy_window(window)

    # main page frame
    main_frame = tk.Frame(window, width=50, height=100)
    main_frame.config(relief="raised", border=2, bg="#313232")
    main_frame.pack(expand=True, fill="both", padx=50, pady=20, anchor="center")

    # Creating main menu
    tittle = tk.Label(main_frame, text="YOUTUBE MUSIC DOWNLOADER")
    tittle.config(
        font=("roboto", 12, "bold"),
        bg="grey",
        fg="white",
        relief="raised",
        border=0.5,
        padx=10,
        pady=10,
    )

    # Url label
    insertlink = tk.Label(main_frame, text="Insert your link from youtube:")
    insertlink.config(
        font=("roboto", 10, "bold"),
        bg="grey",
        fg="white",
        relief="raised",
        border=0.5,
        padx=10,
        pady=10,
    )

    # URL box
    linkbox = tk.Entry(main_frame, width=40)

    # On click download
    button = tk.Button(main_frame, text="Download", command=threading_music)
    button.config(
        width=15,
        height=1,
        pady=5,
        fg="green",
        bg="white",
        relief="raised",
        border=5,
        font=("montserrat", 10, "bold"),
    )

    # Return Button
    button_return = tk.Button(window, text="Return", command=main_window)
    button_return.config(
        width=13,
        height=1,
        pady=5,
        fg="black",
        bg="white",
        relief="raised",
        borderwidth=5,
        border=5,
        font=("montserrat", 9, "bold"),
    )

    # Credits Label
    creator = tk.Label(window, text="By Gustavo Gorges")
    creator.config(
        font=("montserrat", 8, "bold"),
        bg="#313232",
        fg="white",
        relief="sunken",
        border=0.5,
        padx=10,
        pady=10,
    )

    # Packing itens
    tittle.pack(pady=20)
    insertlink.pack(pady=10)
    linkbox.pack(pady=10)
    button.pack()
    creator.pack(side="bottom", pady=8)
    button_return.pack(side="bottom", pady=8)


# Setting up the window
window = tk.Tk()
window.config(background="#101111")
window.title("Youtube video downloader")
window.geometry("400x450")
#

main_window()
