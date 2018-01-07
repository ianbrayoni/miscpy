"""
Strategy Design Pattern
Ref: https://youtu.be/v9ejT8FO-7I
    https://medium.com/@sheikhsajid/design-patterns-in-python-part-1-the-strategy-pattern-54b24897233e
"""
import abc


# Interfaces
class QuackStrategyAbstract(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack(self):
        raise NotImplementedError('Users must define a quack method \
        to use this base class')


class FlyStrategyAbstract(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display(self):
        raise NotImplementedError('Users must define a fly method \
        to use this base class')


class DisplayStrategyAbstract(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display(self):
        raise NotImplementedError('Users must define a display method \
        to use this base class')


# Strategies
@QuackStrategyAbstract.register
class SimpleQuackStrategy(object):
    def quack(self):
        print("Quack!Quack!")


@QuackStrategyAbstract.register
class NoQuackStrategy(object):
    def quack(self):
        print("Cannot quack :-(")


@FlyStrategyAbstract.register
class SimpleFlyStrategy(object):
    def fly(self):
        print("Hooray, I can fly!")


@FlyStrategyAbstract.register
class JetFlyStrategy(object):
    def fly(self):
        print("Hooray, flying like a jet!")


@FlyStrategyAbstract.register
class NoFlyStrategy(object):
    def fly(self):
        print("Cannot fly :-(")


@DisplayStrategyAbstract.register
class DisplayEnglishStrategy(object):
    def display(self):
        print("This is a duck!")


@DisplayStrategyAbstract.register
class DisplaySpanishStrategy(object):
    def display(self):
        print("Este es un pato robot!")


# Instantiate strategies
simple_quack = SimpleQuackStrategy()
no_quack = NoQuackStrategy()

simple_fly = SimpleFlyStrategy()
jet_fly = JetFlyStrategy()
no_fly = NoFlyStrategy()

displayed_english = DisplayEnglishStrategy()
displayed_spanish = DisplaySpanishStrategy()


# Define interface of interest to clients
class Duck(object):
    """
    Defines the interface of interest to clients -
     MellowDuck, JellowDuck, RobotDuck
    Maintains reference to strategy objects.
    """

    def __init__(self, quack_strategy, fly_strategy, display_strategy):
        self._quack_strategy = quack_strategy
        self._fly_strategy = fly_strategy
        self._display_strategy = display_strategy

    def quack(self):
        self._quack_strategy.quack()

    def fly(self):
        self._fly_strategy.fly()

    def display(self):
        self._display_strategy.display()


# Define clients - Types of ducks

# MellowDuck - SimpleQuack, SimplyFly, DisplayEnglish
class MellowDuck(Duck):
    def __init__(self):
        super(MellowDuck, self).__init__(
            simple_quack, simple_fly, displayed_english)


# JellowDuck - SimpleQuack, JetFly, DisplayEnglish
class JellowDuck(Duck):
    def __init__(self):
        super(JellowDuck, self).__init__(
            simple_quack, jet_fly, displayed_english)


# RobotDuck - NoQuack, NoFly, DisplaySpanish
class RobotDuck(Duck):
    def __init__(self):
        super(RobotDuck, self).__init__(
            no_quack, no_fly, displayed_spanish)


if __name__ == '__main__':
    print("Mello Duck:")
    mellow = MellowDuck()
    mellow.quack()
    mellow.fly()
    mellow.display()

    print("\nJello Duck:")

    jellow = JellowDuck()
    jellow.quack()
    jellow.fly()
    jellow.display()

    print("\nRobot Duck:")

    robot = RobotDuck()
    robot.quack()
    robot.fly()
    robot.display()
