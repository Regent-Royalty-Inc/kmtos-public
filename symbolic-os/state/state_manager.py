#!/usr/bin/env python3

# KmtOS State Manager — Initial Skeleton

class StateManager:
    def __init__(self):
        self.memory = {}

    def get(self, key, default=None):
        return self.memory.get(key, default)

    def set(self, key, value):
        self.memory[key] = value

    def all(self):
        return self.memory

