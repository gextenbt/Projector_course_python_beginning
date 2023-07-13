import requests
import telebot
import dotenv
import os
dotenv.load_dotenv()


# Giphy
giphy_url = "http://api.giphy.com/v1/{type}"  # https://developers.giphy.com/docs/api/endpoint
giphy_token = os.getenv("GIPHY_TOKEN")  # https://developers.giphy.com/dashboard/
# Telegram
telegram_token = os.getenv("TELEGRAM_TOKEN") 


def return_gif_link(prompt):
    limit = 1
    resp = requests.get(
        giphy_url.format(type="gifs/search"),
        params={
            "q": prompt,
            "api_key": giphy_token,
            "limit": limit, 
        })

    # print(resp.status_code)
    # print(resp.text)
    resp_data = resp.json()["data"]
    
    if resp.status_code == 200:
        if resp_data:
            return resp_data[limit-1]["images"]["original"]["url"]
        elif not resp_data:
            raise Exception("Image is not found")
    else:
        raise Exception(f"Failed to retrieve GIF from Giphy. Status code: {str(resp.status_code)}")

def telegram_bot(telegram_token):

    bot = telebot.TeleBot(telegram_token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(
            message.chat.id,
            "Hello comrade! Write something to start GIF search"
            )

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        try:
            gif_link = return_gif_link(message.text)
            bot.send_document(message.chat.id, gif_link)
            bot.send_message(
                message.chat.id,
                "The image is found!")                           
        except Exception as ex:
            bot.send_message(
                message.chat.id,
                ex
                )
        
    bot.polling()


if __name__ == "__main__":
    # pass
    # print(return_gif_link(""))
    telegram_bot(telegram_token)


# Useful links
# # Code Example - https://developers.giphy.com/docs/resource/#code-examples
# # API Explorer - to test API on website - https://developers.giphy.com/explorer/
