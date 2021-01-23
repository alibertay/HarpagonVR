from chatterbot import ChatBot



'''
This is an example showing how to train a chat bot using the
ChatterBot ListTrainer.
'''

chatbot = ChatBot('Cimri')

chatbot = ChatBot(
    'SQLMemoryTerminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri=None,
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ]
)

from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.cimri"
)

while True:
    a = input()
    response = chatbot.get_response(a)
    print(response)
