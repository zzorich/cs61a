(define (my-filter func lst) 
    (if (null? lst)
        nil
        (if (func (car lst))
            (cons (car lst) (my-filter func (cdr lst)))
            (my-filter func (cdr lst))
            )
        )
)
(define (interleave s1 s2) 
    (if (null? s1) 
        s2
        (cons (car s1) (interleave s2 (cdr s1)))
        )
    )

(define (accumulate merger start n term)
  (if (< 0 n) 
      (merger  (accumulate merger start (- n 1) term) (term n))
      start
      )
  )

(define (no-repeats lst) 
    (if (null? lst) 
        nil
        (cons (car lst) (no-repeats (my-filter (lambda (x) (not (= x (car lst)))) (cdr lst)) ) )
        )
    )
