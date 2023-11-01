(defun fact(n)
    (cond 
        ((= n 1) 1)
        (T (* n (fact (- n 1))))
    )
)

(defun ncr(n r)
    (setq num (fact n))
    (setq denom1 (fact (- n r)))
    (setq denom2 (fact r))
    (/ num (* denom1 denom2))
)