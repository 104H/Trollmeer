from typing import Annotated

from langchain.chat_models import init_chat_model
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


# the state of our llm
# the state here is in the context of a state machine
# as in theory of computation
class State(TypedDict):
    messages: Annotated[list, add_messages]


class ChatBot:
    # the graph builder
    graph_builder = StateGraph(State)

    # the model we will use
    llm = init_chat_model("openai:gpt-4.1")

    def __init__(self):
        # chatbot recieves a new state at every call
        # the state holds a message in it
        def query(state: State):
            return {"messages": [self.llm.invoke(state["messages"])]}

        # first arg is the name of the bot
        # second arg is the function to be called
        self.graph_builder.add_node("chatbot", query)

        # Start point connects to the chatbot
        self.graph_builder.add_edge(START, "chatbot")

        # node chatbot connects to the end othe graph
        self.graph_builder.add_edge("chatbot", END)

        # compile the graph
        self.graph = self.graph_builder.compile()

    # interactive graph streamer
    def stream_graph_updates(self, user_input: str):
        # a graph stream is given a dictionary with user role
        # and the message the user sent
        self.graph_input = {"messages": [{"role": "user", "content": user_input}]}

        # send input to the graph
        for event in self.graph.stream(self.graph_input):
            for value in event.values():
                print("Assistant:", value["messages"][-1].content)

    def interactor(self):
        # infinite loop for recieving input
        while True:
            print("Type quit or q to close the conversation.")
            # recieve typed input
            user_input = input("Your message: ")

            # enter on the these options to end the conversation
            if user_input.lower() in ["quit", "q"]:
                print("Until next time!")
                break

            # if the conversation was not ended, input the text to the model
            self.stream_graph_updates(user_input)
