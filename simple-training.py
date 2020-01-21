from __future__ import print_function
import numpy as np
import torch

# 1st learning experience with pytorch
# https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
# official 60 min tutorials

x = torch.empty(5, 3)  # uninitialized 5*3 matrix
x = torch.rand(5, 3)  # random initialised 5*3 matrix
x = torch.zeros(5, 3, dtype=torch.long)  # fillin the matrix with 0z and dtype = long
# print(x)
# print(x.size())

# use data to build values
x = torch.tensor([5.1, 3])
# output int when 2 values are both int, else floating numbers
# print(x)

# use existed tensor to build new tensor
x = x.new_ones(5, 3, dtype=torch.double)
print(x)

x = torch.randn_like(x, dtype=torch.float)  # reload dtype
print(x)

#print(x.size())  # get size - output is a tuple

# calculation
y = torch.rand(5, 3)

# 2 ways to add 2 matrix with same x and y lengths
#print(x + y)
torch.add(x, y)

# given a variable as parameter
result = torch.empty(5,3)
torch.add(x, y, out=result)
#print(result)

# adding : in-place add x to y
# remember to add '_' after the operation to change the original variable
y.add_(x)
#print(y)


# index operation like Numpy
print(x[:,1]) # print x where y = 1 tuple

# change the shape
x = torch.randn(4,4)
y = x.view(16)
z = x.view(-1,8) # size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())
# print(z)

# if a tensor only contains 1 element -> use .item() to get corresonding python value
x =


