std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}


def print_score(std):
    print(f"{std['name']}:{std['score']}")


print_score(std1)
print_score(std2)


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(f'{self.name}:{self.score}')

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


michael = Student('Michael', 98)
bob = Student('Bob', 81)
michael.print_score()
print(michael.get_grade())
bob.print_score()
print(bob.get_grade())
