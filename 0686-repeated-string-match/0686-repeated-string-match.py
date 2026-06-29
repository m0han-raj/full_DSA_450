class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a , len_b = len(a) , len(b)

        min_rep = ceil(len_b/len_a)

        rep_str_lst = [a]*min_rep

        for _ in range(3) : #assuming the repitition
            rep_str ="".join(rep_str_lst)
            if b in rep_str:
                return min_rep
            min_rep+=1
            rep_str_lst.append(a)

        return -1


