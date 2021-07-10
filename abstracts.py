import abc


class AbstractPopulation(abc.ABC):
    @abc.abstractclassmethod
    def crossover(self):
        return NotImplementedError

    @abc.abstractclassmethod
    def mutation(self):
        return NotImplementedError

    @abc.abstractclassmethod
    def parent_selection(self):
        return NotImplementedError

    @abc.abstractclassmethod
    def breed_childern(self):
        return NotImplementedError


class AbstractedDecidor(abc.ABC):
    @abc.abstractstaticmethod
    def run(self):
        return NotImplementedError
