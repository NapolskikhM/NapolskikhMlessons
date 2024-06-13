from fake_math import divide as div_f_
from true_math import divide as div_t_

result1 = div_f_(69, 3)
result2 = div_f_(3, 0)
result3 = div_t_(49, 7)
result4 = div_t_(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)