from Vector import Vector
import itertools
import functools
from functools import singledispatchmethod as overload


class Matrix:
    def __init__(self, components: list):
        self.components = []
        for elem in components:
            line = []
            for el in elem:
                line.append(el)
            self.components.append(line)

    def create_MT(self, lines, columns):
        other = Matrix([[]])
        for index in range(lines):
            for _ in range(columns):
                other.components[index].append(0)
            other.components.append([])
        other.components.pop()
        return other

    def printable(self):
        print(self.components)

    def comp_size(self, other):
        if len(self.components) != len(other.components):
            return False
        lines = 0
        while lines < len(self.components):
            if len(self.components[lines]) != len(other.components[lines]):
                return False
            lines += 1
        return True

    def is_square(self):
        if len(self.components) != len(self.components[0]):
            return False
        return True

    def exchange_rows(self, i, j):
        self.components[i], self.components[j] = self.components[j], self.components[i]
        return self

    def change_value(self, i, j, value):
        self.components[i][j] = value
        return self

    def add(self, other):
        save = self.components
        if not isinstance(other, Matrix):
            return None
        if len(self.components) != len(other.components):
            return None
        new = []
        for lines in range(len(self.components)):
            if len(self.components[lines]) != len(other.components[lines]):
                self.components = save
                return None
            new_ = []
            for columns in range(len(self.components[lines])):
                new_.append(
                    self.components[lines][columns] + other.components[lines][columns]
                )
            new.append(new_)
        self.components = new
        return self

    def sub(self, other):
        save = self.components
        if not isinstance(other, Matrix):
            return None
        if len(self.components) != len(other.components):
            return None
        new = []
        for lines in range(len(self.components)):
            if len(self.components[lines]) != len(other.components[lines]):
                self.components = save
                return None
            new_ = []
            for columns in range(len(self.components[lines])):
                new_.append(
                    self.components[lines][columns] - other.components[lines][columns]
                )
            new.append(new_)
        self.components = new
        return self

    def scl(self, other):
        new = []
        for lines in range(len(self.components)):
            new_ = []
            for columns in range(len(self.components[lines])):
                new_.append(self.components[lines][columns] * other)
            new.append(new_)
        self.components = new
        return self

    """Par exemple, si AA est:
    A=[a11 a12 
    a21 a22
    a31a32]

    Et vv est:
    v=[v1v2]

    Alors le résultat de AvAv sera:
    [a11*v1+a12*v2 a21*v1+a22*v2 a31*v1+a32*v2]
    """

    def mul_vec(self, other):
        if not isinstance(other, Vector):
            return None
        if len(other.components) != len(self.components[0]):
            return None
        res = []
        end = []
        for elem in self.components:
            for index in range(len(other.components)):
                res.append(elem[index] * other.components[index])
            end.append(functools.reduce(lambda i, j: i + j, res))
            res = []
        return Vector(end)

    """Si
    A=[2 3
    4 1]
    et
    B=[5 7
    6 8]

    Le produit C=A*BC=A*B serait :
    C=[(2*5+3*6)(2*7+3*8)(4*5+1*6)(4*7+1*8)]
    C=[(10+18)(14+24)(20+6)(28+8)]
    C=[28 38 26 36]"""

    def mul_mat(self, other):
        if not isinstance(other, Matrix):
            return None
        if len(self.components[0]) != len(other.components):
            return None
        res = []
        end = []
        temp = []
        for index in range(len(self.components)):
            for index2 in range(len(other.components[0])):
                for index3 in range(len(self.components[0])):
                    res.append(
                        self.components[index][index3]
                        * other.components[index3][index2]
                    )
                temp.append(functools.reduce(lambda i, j: i + j, res))
                res = []
            end.append(temp)
            temp = []
        return Matrix(end)

    # add adiagonal numbers of square matrice
    def trace(self):
        if not self.is_square():
            return None
        res = 0
        for i in range(len(self.components)):
            res += self.components[i][i]
        return res

    def transpose(self):
        res = self.create_MT(len(self.components[0]), len(self.components))
        for index in range(len(self.components)):
            for index2 in range(len(self.components[0])):
                res.components[index2][index] = self.components[index][index2]
        return res

    def get_smaller_m(self, column):
        new_size = len(self.components) - 1
        main = []
        for _ in range(new_size):
            main.append([])
        for i in range(1, len(self.components)):
            for j in range(len(self.components[i])):
                if j != column:
                    main[i - 1].append(self.components[i][j])
        return Matrix(main)

    def det2x2(self):
        return (self.components[0][0] * self.components[1][1]) - (
            self.components[1][0] * self.components[0][1]
        )

    def det3x3(self):
        res = 0
        for index in range(len(self.components[0])):
            if index % 2 == 0:
                res += self.components[0][index] * self.get_smaller_m(index).det2x2()
            else:
                res -= self.components[0][index] * self.get_smaller_m(index).det2x2()
        return res

    def determinant(self):
        if not self.is_square:
            return None
        if len(self.components) == 2:
            return self.det2x2()
        elif len(self.components) == 3:
            return self.det3x3()
        else:
            res = 0
            for index in range(len(self.components[0])):
                if index % 2 == 0:
                    res += (
                        self.components[0][index] * self.get_smaller_m(index).det3x3()
                    )
                else:
                    res -= (
                        self.components[0][index] * self.get_smaller_m(index).det3x3()
                    )
            return res

    def inverse(self):
        """on cree une matrice identite (que des 1 en diagonale et 0 ailleurs)
        on applique la methode RREF sur les 2 pour avoir l'inverse de la matrice de base
        car matrice identite corespnd aux 2 selon theoreme A*A'= matricee Identite
        donc de A a I fait que de I a A'
        """
        if not self.is_square:
            return None
        identite = [
            [float(i == j) for i in range(len(self.components))]
            for j in range(len(self.components))
        ]
        for j in range(len(self.components)):
            for i in range(j, len(self.components)):
                if self.components[i][j] != 0:
                    self.components[i], self.components[j] = (
                        self.components[j],
                        self.components[i],
                    )
                    identite[i], identite[j] = identite[j], identite[i]
                    break
            else:
                print("La matrice n'est pas inversible.")
                return None
            pivot = self.components[j][j]
            for k in range(len(self.components)):
                self.components[j][k] /= pivot
                identite[j][k] /= pivot
            for i in range(len(self.components)):
                if i != j:
                    ratio = self.components[i][j]
                    for k in range(len(self.components)):
                        self.components[i][k] -= ratio * self.components[j][k]
                        identite[i][k] -= ratio * identite[j][k]
        return Matrix(identite)

    def row_echelon(self):
        """en gros avoir une matrice avec une ligne diagonale de 1 et que des 0 en dessous
        chiant
        on cherche les pivots (1er elem non nul de la ligne) (si que des nul on inverse les lignes)
        on soustrait les lignes d en dessous sur la meme colonne pour avoir des 0
        on recommence en faisant +1 sur la ligne d apres(on a la diagonale.
        pour la fin on reprend et on divide chaque elem de ligne par la valeur du pivot pour avoir 1 en pivot
        """
        if not self.is_square:
            return None
        pivot = 0
        for row in range(len(self.components)):
            if pivot >= len(self.components[0]):
                break
            while self.components[row][pivot] == 0:
                pivot += 1
                if pivot >= len(self.components[0]):
                    return self
            for i in range(row + 1, len(self.components)):
                if self.components[i][pivot] != 0:
                    self.components[row], self.components[i] = (
                        self.components[i],
                        self.components[row],
                    )
                    break
            reducer = self.components[row][pivot]
            for k in range(len(self.components[row])):
                self.components[row][k] = self.components[row][k] / reducer
            for i in range(len(self.components)):
                if i != row:
                    multiplier = self.components[i][pivot]
                    self.components[i] = [
                        elem - multiplier * self.components[row][j]
                        for j, elem in enumerate(self.components[i])
                    ]
            pivot += 1
        return self

    def rank(self):
        """
        meme combat que les precedents avec le pivot de gauss
        cette fois on monte de rang des qu on trouve un pivot potable"""
        rank = 0
        for j in range(len(self.components[0])):
            pivot = False
            for i in range(rank, len(self.components)):
                if self.components[i][j] != 0:
                    self.components[i], self.components[rank] = (
                        self.components[rank],
                        self.components[i],
                    )
                    pivot = True
                    break
            if pivot:
                for i in range(rank + 1, len(self.components)):
                    coefficient = self.components[i][j] / self.components[rank][j]
                    for k in range(j, len(self.components[0])):
                        self.components[i][k] -= coefficient * self.components[rank][k]
                rank += 1
        return rank
