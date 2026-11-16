# Week 12 answers

## Exercise 1
1. The messages the customer typed:
 - I want to change my shipping address, order A102, 9 Pine Street, Tampa
2. How many tool requests were refused, and why: 
- 2 with it being order A100 and then the request to change shipping address, A100 to 123 Main St, Anytown AN 12345
3. If the customer now types "thanks", how many messages does Ollama receive on the next call? 
- 14 messages, the system message, the 6 user and assistant response and, 2 for each of the 3 tool entries, and the new message.
4. Why does "Do you sell gift cards?" still go to a person, and why is that acceptable?
- Because the rule is looking for any card in the message. It is acceptable because a payment question will put the card details in front of the model.

## Exercise 3
Type a message, or type quit to stop.
You: I want to change my shipping address
Sunny: Your request to change the shipping address has been submitted and will require staff approval.
You: quit
Messages in this conversation: 3
Staff review
Request 1: A100 to 123 Main St, Anytown, AN 12345
Approve? yes or no: no
Request 1 rejected.
A100 14 Bay Road
A101 3 Gull Lane
A102 88 Pier Street