(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (ordered? s) (if (or (null? s) (null? (cdr s)))
                         #t 
                         (and (not (> (car s) (cadr s)))
                              (ordered? (cdr s)))))

(define (square x) (* x x))

(define (pow base exp)
    (if (= exp 0)
        1
        (if (= (modulo exp 2) 1)
            (* base (pow base (- exp 1)))
            (square (pow base (/ exp 2)))
            )
    )
    )
