;; Scheme ;;


(define lst
  (list (list 1) 2 (list 3 4) 5)
)

(define (composed f g)
  (lambda (x) (f (g x)))
)

(define (remove item lst)
  (if (null? lst)
      nil
      (if (= item (car lst))
	  (remove item (cdr lst))
	  (cons (car lst) (remove item (cdr lst)))))

)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)


(define (filter-lst f lst)
  (if (null? lst)
      nil
      (if (f (car lst))
	     (cons (car lst) (filter-lst f (cdr lst)))
	     (filter-lst f (cdr lst))))
)

(define (no-repeats s)
  (if (null? s)
      nil
      (cons (car s) (no-repeats (remove (car s) (cdr s)))))
)

(define (substitute s old new)
  (define (func a)
    (if (eq? a old)
	new
	a))
  (if (null? s)
      nil
      (if (pair? (car s))
	  (cons (substitute (car s) old new) (substitute (cdr s) old new))
	  (cons (func (car s)) (substitute (cdr s) old new))))
)

(define (substitute2 s old new)
  (if (null? s)
      nil
      (if (pair? (car s))
	  (cons (substitude (car s) old new) (substitute (car s) old new))
	  (cons (if (eq? (car s) old)
		    new
		    (car s)) (substitute (car s) old new))))
)


(define (sub-all s olds news)
  (define (zip xs ys)
   (if (or (null? xs) (null? ys))
     nil
     (cons
       (list (car xs) (car ys))
       (zip (cdr xs) (cdr ys)))))
  (define zips
    (zip olds news))
  (define (action s zip_olds_news)
    (if (null? zip_olds_news)
	s
	(action (substitute s (car(car(zip_olds_news))) (cdr(car(zip_olds_news)))) (cdr zip_olds_news))))
  (action s zips)
)

;(substitute (substitute s old new) old new)





