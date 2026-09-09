class EnglishGreeting:
    def greet(self):
        return "Hello"
class SpanishGreeting:
    def greet(self):
        return "Hola"

def send_greeting(greeter):
    print(greeter.greet())

send_greeting(EnglishGreeting())
send_greeting(SpanishGreeting())