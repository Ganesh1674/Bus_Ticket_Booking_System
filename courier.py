# Install Courier SDK: pip install trycourier
from trycourier import Courier

client = Courier(auth_token="pk_prod_KCEXWA8KYTMBXWN6AQRWHTQ0QVCT")

resp = client.send_message(
message={
    "to": {
    "email": "ganeshmahajan1674@gmail.com"
    },
    "content": {
    "title": "Welcome to Courier!",
    "body": "Want to hear a joke? {{joke}}"
    },
    "data":{
    "joke": "Why does Python live on land? Because it is above C level"
    }
}
)