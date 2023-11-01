% Average of elements in a list
avg(X):-
 sum_list(X,S),
 length(X,N),
 A is S/N,
 write(A).