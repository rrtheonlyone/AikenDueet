import Queue

def checkMessage(messages):

	openQty = 0
	buyQueue = Queue.PriorityQueue()
	sellQueue = Queue.PriorityQueue()

	#loops through every message
	for message in messages:

		#message validation
		messageType = message["SOD"]
	
		if(!validate(message, messageType)):
			continue



def validate(message, messageType):

	if(messageType == "SOD"):
		if "closeprice" not in message:
			return False
			
	elif(messageType == "NEW"):
		



{
  "messageId": 1,
  "messageType": "SOD",
  "closePrice": {
    "0005.HK": 75
  }
},
{
  "messageId": 2,
  "messageType": "NEW",
  "orderId": "order-1",
  "quantity": 500,
  "symbol": "0005.HK",
  "side": "S",
  "orderType": "LMT",
  "price": 74.9
},
{
  "messageId": 3,
  "messageType": "NEW",
  "orderId": "order-2",
  "quantity": 500,
  "symbol": "0005.HK",
  "side": "S",
  "orderType": "LMT",
  "price": 74.8
},
{
  "messageId": 4,
  "messageType": "NEW",
  "orderId": "order-3",
  "quantity": 1000,
  "symbol": "0005.HK",
  "side": "B",
  "orderType": "LMT",
  "price": 75
},
{
  "messageId": 5,
  "messageType": "EOD"
}