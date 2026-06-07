#!/usr/bin/env python3

# KmtOS Engine Core — With Operator Registry + State Manager

from operators.registry import OperatorRegistry
from operators.echo import echo
from operators.reverse import reverse
from operators.route import route
from operators.store import store
from state.state_manager import StateManager

class Engine:
    def __init__(self):
        self.state = StateManager()
        self.registry = OperatorRegistry()

        # Register operators
        self.registry.register("echo", echo)
        self.registry.register("reverse", reverse)
        self.registry.register("route", route)
        self.registry.register("store", store)

    def process(self, signal):
        # Increment heartbeat count
        count = self.state.get("heartbeat_count", 0) + 1
        self.state.set("heartbeat_count", count)

        # First: route the signal
        op_name, routed_signal = self.registry.call("route", signal)

        # If operator is 'store', pass state as second argument
        if op_name == "store":
            result = store(routed_signal, self.state)
        else:
            result = self.registry.call(op_name, routed_signal)

        return f"{result} | count={count} | op={op_name}"

