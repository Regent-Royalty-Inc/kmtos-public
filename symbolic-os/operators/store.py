#!/usr/bin/env python3

def store(signal, state):
    state.set("last_input", signal)
    return f"stored:{signal}"

