import time
from membrane.membrane import Membrane
from engine.engine import Engine

membrane = Membrane()
engine = Engine()

toggle = True

while True:
    if toggle:
        signal = membrane.receive()
    else:
        signal = membrane.receive_external()

    toggle = not toggle

    if signal is None:
        continue

    result = engine.process(signal)
    membrane.transmit(result)

    time.sleep(1)

