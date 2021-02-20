from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import logging


if __name__ == "__main__":

    #Low confidence response example
    # Create a new instance of a ChatBot
    bot = ChatBot(
        'Example Bot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, but I do not understand.',
                'maximum_similarity_threshold': 0.90
            }
        ]
    )

    trainer = ListTrainer(bot)

    # Train the chat bot with a few responses
    trainer.train([
        'How can I help you?',
        'I want to create a chat bot',
        'Have you read the documentation?',
        'No, I have not',
        'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
    ])

    # Get a response for some unexpected input
    response = bot.get_response('How do I make an omelette?')
    print(response)

    """"
    #Specific response example
    # Create a new instance of a ChatBot
    bot = ChatBot(
        'Exact Response Example Bot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch'
            },
            {
                'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                'input_text': 'Help me!',
                'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
            }
        ]
    )

    # Get a response given the specific input
    response = bot.get_response('Help me!')
    print(response)
    """

    """
    #logging.basicConfig(level=logging.INFO)
    # Create a new instance of a ChatBot
    bot = ChatBot(
        'SQLMemoryTerminal',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri=None,
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter',
            'chatterbot.logic.BestMatch'
        ]
    )

    # Get a few responses from the bot
    response = bot.get_response('What time is it?')
    print(response)

    response = bot.get_response('What is 7 plus 7?')
    print(response)
    """

    """
    bot = ChatBot(
        'Math & Time Bot',
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter'
        ]
    )

    # Print an example of getting one math based response
    response = bot.get_response('What is 4 + 9?')
    print(response)

    # Print an example of getting one time based response
    response = bot.get_response('What time is it?')
    print(response)
    """

    """
    # Uncomment the following lines to enable verbose logging
    # import logging
    # logging.basicConfig(level=logging.INFO)

    # Create a new instance of a ChatBot
    bot = ChatBot(
        'Terminal',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter',
            'chatterbot.logic.BestMatch'
        ],
        database_uri='sqlite:///database.sqlite3'
    )

    print('Type something to begin...')

    # The following loop will execute each time the user enters input
    while True:
        try:
            user_input = input()

            bot_response = bot.get_response(user_input)

            print(bot_response)

        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
    """

    """
    # Create a new chat bot named Charlie
    chatbot = ChatBot('Charlie')

    trainer = ListTrainer(chatbot)

    trainer.train([
        "Hi, can I help you?",
        "Sure, I'd like to book a flight to Iceland.",
        "Your flight has been booked."
    ])

    # Get a response to the input text 'I would like to book a flight.'
    response = chatbot.get_response('I would like to book a flight.')

    print(response)
    """

    """
    chatbot = ChatBot('Ron Obvious')

    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot based on the english corpus
    trainer.train("chatterbot.corpus.english")

    # Get a response to an input statement
    res = chatbot.get_response("what are you doing")
    print(res)
    """

    """
    bot = ChatBot('Ron Obvious')
    # bot = ChatBot('Ron Obvious', read_only=True)
    while True:
        try:
            bot_input = bot.get_response(input())
            print(bot_input)

        except(KeyboardInterrupt, EOFError, SystemExit):
            break
    """
