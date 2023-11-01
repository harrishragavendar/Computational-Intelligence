(
    defun gcd(a b)
    (cond 
        ((= (mod a b) 0) b)
        (T (gcd b (mod a b)))
    )
)

(
    defun lcm(a b)
        (/ (* a b) (gcd a b))
)