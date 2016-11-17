"""
    Custom Burp Extension to fuzz web applications
"""

from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator
from java.util import List, ArrayList

# Extender class Burp uses as a skeleton
class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.registerIntruderPayloadGeneratorFactory(self)

    def getGeneratorName(self):
        return "Lit Payload Generator"

    def createNewInstance(self, attack):
        return LitFuzzer(self, attack)

# Our actual fuzzer to modify the payloads
class LitFuzzer(IIntruderPayloadGenerator):
    def __init__(self, extender, attack):
        self._extender = extender
        self._helpers = extender._helpers
        self._attack = attack
        self.max_payloads = 1
        self.num_iterations = 0

    def hasMorePayloads(self):
        if self.num_iterations == self.max_payloads:
            return False
        else:
            return True

    def getNextPayload(self, current_payload):
        payload = "".join(chr(x) for x in current_payload)
        payload = self.mutate_payload(payload)
        self.num_iterations += 1
        return payload

    def reset(self):
        self.num_iterations = 0

    def mutate_payload(self, payload):
        return ""
