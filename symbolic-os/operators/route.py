#!/usr/bin/env python3

def route(signal):
    # Internal signals are always "heartbeat"
    if signal == "heartbeat":
        return ("echo", signal)

    # External signals with digits → store
    if any(ch.isdigit() for ch in signal):
        return ("store", signal)

    # External signals with letters → reverse
    if any(ch.isalpha() for ch in signal):
        return ("reverse", signal)

    # Fallback
    return ("echo", signal)

