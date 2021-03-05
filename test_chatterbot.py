from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    ''' 
    #This is an example showing how to create an export file from an existing chat bot that can then be used to train other bots.
    

    chatbot = ChatBot('Export Example Bot')

    # First, lets train our bot with some data
    trainer = ChatterBotCorpusTrainer(chatbot)

    trainer.train('chatterbot.corpus.english')

    # Now we can export the data to a file
    trainer.export_for_training('./my_export.json')
    '''

    """
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
    """

    """
    # ??? 执行不符合预期
    #Specific response example
    # Create a new instance of a ChatBot
    bot = ChatBot(
        'Exact Response Example Bot1',
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
        database_uri='sqlite:///time_and_math.sqlite3',
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

    '''
    # A:你喝酒吗
    # B:我的大脑不需要任何饮料。
    chatbot = ChatBot(
        'xiaojuzi',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///xiaojuzi.sqlite3'
    )
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.chinese") # Training xxx.yml ...
    res = chatbot.get_response("你喝酒吗")
    print(res)
    '''

    chatbot = ChatBot(
        'my_conv',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///my_conv.sqlite3'
    )
    trainer = ListTrainer(chatbot)
    trainer.train([
        '吃了么',
        '吃过了',
        '你吃了么',
        '我也刚吃',
        '要不要来根烟',
        '谢了',
    ])
    res = chatbot.get_response("要不要来根烟")
    print(res)
