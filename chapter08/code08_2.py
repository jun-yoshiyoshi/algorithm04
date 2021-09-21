# 3SAT(3-satisfiability)問題

"""
「∨」は、論理和（logical disjunction）記号で、「または」と読まれ、「A∨B」は「AまたはBのいずれか（または両方）が真であるときに真となる」ことになる。
「∧」は、論理積（logical conjunction）記号で、「かつ」と読まれ、「A∧B」は「AとBがともに真であるときのみ真となる」ことになる。
「￢」は否定を表し、「￢A」は「Aが真ではない、偽である」ことを意味している。
"""

import random


class kSAT:
    @classmethod
    def generate(cls, k, var_num, clause_num):
        """変数の数(var_um)と節の数(clause_num)をとり、kSAT問題を作る"""
        ksat = cls()
        var_list = list(range(var_num))
        res = []
        while len(res) < clause_num:
            clause = []
            clause_size = random.randint(1, k)
            for i in random.sample(var_list, clause_size):
                prefix = random.choice((0, 1))
                clause.append((prefix, i))
            clause.sort(key=lambda x: x[1])
            if clause not in res:
                res.append(clause)
        ksat.body = res
        return ksat

    def test(self, var_list):
        """受け取るvar_listの真偽を使い論理式を評価"""
        res = []
        for clause in self.body:
            clause_data = [not var_list[i] if p else var_list[i] for p, i in clause]
            res.append(any(clause_data))
        return all(res)

    def __str__(self):
        res = []
        for clause in self.body:
            clause_str = [f"￢x{i}" if p else f"x{i}" for p, i in clause]
            res.append("(" + "v".join(clause_str) + ")")
        return "^".join(res)


ksat = kSAT.generate(3, 4, 3)
print(ksat)
