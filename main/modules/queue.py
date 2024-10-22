from abc import ABC, abstractmethod


class IQueue(ABC):
    @abstractmethod
    def add_(self, item: object) -> None: pass

    @abstractmethod
    def get_(self) -> object: pass



class Queue(IQueue, list):
    def add_(self, item):
        self.append(item)

    def get_(self):
        return self.pop(0)


class AdvancedQueue(IQueue, dict):
    def add_(self, item: dict):
        self.update(item)

    def get_(self):
        key = self.getKeys()[0]
        value = self.pop(key)
        return key, value

    def getKeys(self):
        return list(self.keys())