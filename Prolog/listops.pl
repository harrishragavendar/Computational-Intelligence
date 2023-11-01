% Append two lists
append([], [a, b], L).
append([a,b],[c,d],L).

% Length of the list
length([a, b, c], N).
length([w,e],N).

% Check whether element is a member of the list
member(b, [a, b, c]).
member(d,[a,b,c]).

% Reverse the list
reverse([a, b, c], R).
reverse([m,n,o],R).

% Sort the list
sort([5,4,3,2],L).

% Minimum element in list
min_list([5,4,3,2],L).

% Maximum element in list
max_list([5,4,3,2],L).

% Sum of elements in list
sum_list([1,2,3,4],S).
