; ;;;;;;;;;;;;;;
; ; Questions ;;
; ;;;;;;;;;;;;;;
; Scheme
(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (unique s)
  (if (null? s)
      nil
      (cons (car s)
            (unique
             (filter (lambda (x) (not (equal? x (car s))))
                     (cdr s)
             )
            )
      )
  )
)

(define (cons-all first rests)
  (map (lambda (x) (cons first x)) rests)
)

; ; List all ways to make change for TOTAL with DENOMS
; ; 
; ; if denoms.1 > n 
(define (list-change total denoms)
  (define (l-c tot deno)
    (if (null? deno)
        nil
        (if (= 0 tot)
            '(nil)
            (if (< tot (car deno))
                (l-c tot (cdr deno))
                (append 
                    (cons-all (car deno) (l-c (- tot (car deno)) denoms))
                    (list-change tot (cdr deno))
                )
            )
        )
    )
  )
  (l-c total denoms)
)

; Tail recursion
(define (replicate x n)
  (define (rep n result)
    (if (= n 0)
        result
        (rep (- n 1) (cons x result))
    )
  )
  (rep n nil)
)

(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (term n)
                (accumulate combiner start (- n 1) term)
      )
  )
)

(define (accumulate-tail combiner start n term)
  (define (tail point result)
    (if (> point n)
        result
        (tail (+ 1 point) (combiner result (term point)))
    )
  )
  (tail 1 start)
)

; Macros
(define-macro
 (list-of map-expr for var in lst if filter-expr)
 'YOUR-CODE-HERE
)
