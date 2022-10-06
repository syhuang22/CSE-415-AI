import math
import re


def is_multiple_of_11(n):
    if n % 11 == 0:
        return True
    return False


def last_prime(m):
    p = 1
    for i in range(2, m+1):
        if is_prime(i):
            p = i
    return p


def is_prime(p):
    if p > 1:
        for i in range(2, p):
            if (p % i) == 0:
                return False
        return True


def quadratic_roots(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return "complex"
    elif d == 0:
        x = (-b + math.sqrt(b**2 - 4*a*c))/2*a
        return x
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return x1, x2


def perfect_shuffle(even_list):
    s1 = []
    n1 = 0
    n2 = int(len(even_list)/2)
    for i in range(0, len(even_list)):
        if i % 2 == 0:
            s1.append(even_list[n1])
            n1 = n1 + 1
        else:
            s1.append(even_list[n2])
            n2 = n2 + 1
    return s1


def five_times_list(input_list):
    s1 = [i * 5 for i in input_list]
    return s1


def triple_vowels(text):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for x in text:
        if x in vowels:
            text = text.replace(x, x+x+x)
    return text


def count_words(text):
    clean = ('[', ']')
    for x in text:
        if x in clean:
            text = text.replace(x, '?')
    clean_list = re.split(r"[^a-zA-Z0-9-+*/@#%']+", text.lower())
    count = dict()
    for i in clean_list:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1
    if "" in count:
        del count[""]
    return count


def make_quartic_evaluator(a, b, c, d, e):
    return lambda x: a*x**4 + b*x**3 + c*x**2 + d*x + e


class Polygon:

    def __init__(self, n_sides, lengths=None, angles=None):
        self.n_sides = n_sides
        self.lengths = lengths
        self.angles = angles
    """Polygon class."""

    def is_rectangle(self):
        if self.n_sides != 4:
            return False
        if self.n_sides == 4:
            if self.angles is None:
                return None
            if self.angles is not None:
                return self.equal_angle()
            if self.lengths is not None:
                return self.equal_length()
        if self.angles is None and self.lengths is None:
            return None
        return False

    def is_rhombus(self):
        if self.n_sides != 4:
            return False
        if self.n_sides == 4:
            if self.lengths is not None:
                return self.equal_length()
            if self.angles is not None and self.lengths is not None:
                return self.angles[0] == self.angles[2] or self.angles[1] == self.angles[3]
        if self.angles is None or self.lengths is None:
            return None
        return False

    def is_square(self):
        if self.n_sides != 4:
            return False
        if self.angles is None and self.lengths is None:
            return None
        if self.n_sides == 4:
            if self.angles is not None and self.lengths is not None:
                return self.equal_angle() and self.equal_length()
            if self.angles is None and self.equal_length() is False:
                return False
            if self.angles is None and self.equal_length():
                return None
            if self.lengths is None and self.equal_angle():
                return None
        return False

    def is_regular_hexagon(self):
        if self.n_sides != 6:
            return False
        if self.angles is None and self.lengths is None:
            return None
        if self.n_sides == 6:
            if self.angles is not None and self.lengths is not None:
                return self.equal_angle() and self.equal_length()
            if self.angles is None and self.equal_length() is False:
                return False
            if self.angles is None and self.equal_length():
                return None
            if self.lengths is None and self.equal_angle():
                return None
        return False

    def equal_length(self):
        x = self.lengths[0]
        for i in self.lengths:
            if x != i:
                return False
        return True

    def equal_angle(self):
        x = self.angles[0]
        for i in self.angles:
            if x != i:
                return False
        return True

    def is_isosceles_triangle(self):
        if self.n_sides != 3:
            return False
        if self.angles is None and self.lengths is None:
            return None
        if self.n_sides == 3:
            if self.angles is not None:
                if self.angles[0] == self.angles[1] or self.angles[0] == self.angles[2] or \
                        self.angles[1] == self.angles[2]:
                    return True
            if self.lengths is not None:
                if self.lengths[0] == self.lengths[1] or self.lengths[0] == self.lengths[2] or \
                        self.lengths[1] == self.lengths[2]:
                    return True
        return False

    def is_equilateral_triangle(self):
        if self.n_sides != 3:
            return False
        if self.angles is None and self.lengths is None:
            return None
        if self.n_sides == 3:
            if self.angles is not None and self.lengths is not None:
                return self.equal_length() and self.equal_angle()
            if self.angles is None:
                return self.equal_length()
            if self.lengths is None:
                return self.equal_angle()
        return False

    def is_scalene_triangle(self):
        if self.n_sides != 3:
            return False
        if self.angles is None and self.lengths is None:
            return None
        if self.n_sides == 3:
            if self.angles is not None:
                return len(set(self.angles)) == len(self.angles)
            if self.lengths is not None:
                return len(set(self.lengths)) == len(self.lengths)
        return False
