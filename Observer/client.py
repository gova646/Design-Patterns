from subject import Subject
from concreteObserver import User

subject = Subject('Group')
user1 = User('user1')
user2 = User('user2')
subject.addObserver(user1)
subject.addObserver(user2)

subject.notifyAll('HI')

subject.removeObserver(user1)

subject.notifyAll('Hello')
