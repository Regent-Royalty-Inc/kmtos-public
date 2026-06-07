#!/usr/bin/env python3

class Membrane:
    def receive(self):
        # Internal signal generator
        return "heartbeat"

    def receive_external(self):
        # External input from user
        try:
            return input("External input: ")
        except EOFError:
            return None

    def transmit(self, data):
        # Output to console
        print(f"Membrane output: {data}")

