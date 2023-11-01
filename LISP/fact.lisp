(defun fact(n)
    (cond 
        ((= n 1) 1)
        (T (* n (fact (- n 1))))
    )
)