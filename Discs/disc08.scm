;; scheme ;;
;; scheme ;;

(define (my-append a b)
    (if (null? a)
        b
        (cons (car a) (my-append (cdr a) b)))
)

(define (replicate t n)
    (if (= n 0)
        nil
        (cons t (replicate t (- n 1)))))

(define (uncompress s)
    (if (null? s)
        nil
        (my-append (replicate (car(car s)) (car(cdr (car s)))) (uncompress (cdr s)))
    )
)

(define (map fn lst)
    (if (null? lst)
        nil
        (cons (fn (car lst)) (map fn (cdr lst)))))
    
(define (make-tree label branches) 
    (cons label branches)
)    
(define (label tree)
    (car tree)
)
(define (branches tree)
    (cdr tree)
)
    

