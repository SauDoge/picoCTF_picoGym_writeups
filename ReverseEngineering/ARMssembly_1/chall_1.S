	.arch armv8-a
	.file	"chall_1.c"
	.text
	.align	2
	.global	func
	.type	func, %function
func:
	sub	sp, sp, #32
	str	w0, [sp, 12] // argument in addr sp + 12
	mov	w0, 58
	str	w0, [sp, 16] // 58 in addr sp + 16
	mov	w0, 2
	str	w0, [sp, 20] // 2 in addr sp + 20 
	mov	w0, 3
	str	w0, [sp, 24] // 3 in addr sp + 24
	ldr	w0, [sp, 20] // w0 = 2
	ldr	w1, [sp, 16] // w1 = 58
	lsl	w0, w1, w0  // w0 = 58 * 2^2 = 232
	str	w0, [sp, 28] // 232 in addr sp + 28
	ldr	w1, [sp, 28] // w1 = 232
	ldr	w0, [sp, 24] // w0 = 3
	
	sdiv w0, w1, w0  // w0 = 232 / 3 = 77

	str	w0, [sp, 28] // 77 at addr sp + 28
	ldr	w1, [sp, 28] // w1 = 77
	ldr	w0, [sp, 12] // w0 = arg
	sub	w0, w1, w0 // w0 = 77 - arg
	str	w0, [sp, 28]
	ldr	w0, [sp, 28]
	add	sp, sp, 32 
	ret // return from subroutine
	.size	func, .-func
	.section	.rodata
	.align	3
.LC0:
	.string	"You win!"
	.align	3
.LC1:
	.string	"You Lose :("
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	str	x1, [x29, 16]
	ldr	x0, [x29, 16]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	str	w0, [x29, 44]
	ldr	w0, [x29, 44]
	bl	func
	cmp	w0, 0 // if 77 - arg == 0
	bne	.L4
	adrp x0, .LC0 // store the address of label LC0 into x0
	add	x0, x0, :lo12:.LC0
	bl	puts
	b	.L6
.L4:
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts
.L6:
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
