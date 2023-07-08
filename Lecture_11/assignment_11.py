import requests
import auth_variables
import telebot


# Giphy
giphy_url = "http://api.giphy.com/v1/{type}"  # https://developers.giphy.com/docs/api/endpoint
giphy_token = auth_variables.giphy_token  # https://developers.giphy.com/dashboard/
# Telegram
telegram_token = auth_variables.telegram_token  

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
    
    if resp_data:
        return resp_data[limit-1]["images"]["original"]["url"]
    else:
        return False

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
            if gif_link:
                bot.send_document(message.chat.id, gif_link)
                bot.send_message(
                    message.chat.id,
                    "The image is found!")
            elif not gif_link:
                bot.send_message(
                    message.chat.id,
                    "The image is not found")                             
        except Exception as ex:
            print(ex)
            bot.send_message(
                message.chat.id,
                "Something went wrong")

    bot.polling()


if __name__ == "__main__":
    # print(return_gif_link("snake"))
    telegram_bot(telegram_token)


# Useful links
# # Code Example - https://developers.giphy.com/docs/resource/#code-examples
# # API Explorer - to test API on website - https://developers.giphy.com/explorer/
