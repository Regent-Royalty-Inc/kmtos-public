#!/usr/bin/env python3

# KmtOS Operator Registry — Initial Skeleton

class OperatorRegistry:
    def __init__(self):
        self.operators = {}

    def register(self, name, func):
        self.operators[name] = func

    def call(self, name, *args, **kwargs):
        if name in self.operators:
            return self.operators[name](*args, **kwargs)
        return f"Unknown operator: {name}"

