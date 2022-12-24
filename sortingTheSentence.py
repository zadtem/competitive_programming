class Solution:
    def sortSentence(self, s: str) -> str:
        assert 2<= len(s) <= 200
        lst = s.split()
        lst2 = []
        for j in range(0, len(lst)-1):
          minElement =j
          for i in range(j+1,len(lst)):
             if (lst[i][-1] < lst[minElement][-1]):
                    minElement = i
          if (minElement != j):
              lst[j], lst[minElement] = lst[minElement], lst[j]
        for i in lst:
            j = str(lst.index(i)+1)
            lst2.append(i.replace(j, ""))
        print(lst2)
        final = " ".join(lst2)
        return final
        

