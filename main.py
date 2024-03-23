from pyrogram import Client, idle, filters
from pyrogram.types import Message

# Create a Pyrogram Client
API_ID = os.environ.get("API_ID", "10581465")
API_HASH = os.environ.get("API_HASH", "9494a2ca550339e41a37556344e5c60e")
STRING_SESSION = os.environ.get("STRING_SESSION", "BQC366Hiz_hUxNUfpO9YIoo7hxa3533JrHsBKcomxCrjmmBVdGIEKpQSJ3DBxMeez3xsoPUtCH26ThySKX6V4K9QnNgYdsKIdLsNlpgx5jk9EAsMPsIsKD_FRAROCz-0RUTaY6J3AHDcHGQp1t-Xy7jzeldBP_vg6YWqRmhIpl_x5BN3TcAwbYl15XxUxfmxMcFtlSvz4G9Pvk7W2NNoZ3-t19NNB4maeyhXGnY7zjNbL4DSiUn9NNYGR1qrxCbP75oXuZssYcDWmbVGs1fCT1BHLHUdHUxdsjrvheLT_NbyA43E7LVkw0ReHr9bYFArMAdM9G6XISCG5rfjcmumKCgtAAAAAWZ24XgA")

app = Client(
    "JessicaBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    session_string = STRING_SESSION
)

# Define the source and destination channels
source_channel_id = -1002145521457  # Replace with the source channel ID
destination_channel_id = -1002076736985  # Replace with the destination channel ID

# Define a function to download and forward all videos
async def download_and_forward_all_videos():
    async for message in app.iter_history(chat_id=source_channel_id, filter="video"):
        if message.video:
            video = message.video
            file_id = video.file_id

            # Download the video
            file_path = await app.download_media(file_id)

            # Forward the video to the destination channel
            await app.send_video(destination_channel_id, video=file_path)

# Define a command handler to initiate the process
@app.on_message()
async def start(client, message: Message):
    if message.text == "/download_all":
        await download_and_forward_all_videos()

# Start the bot
app.run()
idle() 
