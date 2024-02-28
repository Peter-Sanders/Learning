			global _start

			section .text
_start:		mov		rax, 2
			mov		rdi, path
			xor		rsi, rsi 
			syscall

			push	rax
			sub		rsp, 16

read_buffer:
			xor		rax, rax
			mov		rdi, [rsp+16]
			mov		rsi, rsp
			mov		rdx, 16
			syscall
			
			test	rax, rax
			jz	exit

			mov		rdx, rax
			mov		rax, 1
			mov		rdi, 1
			mov		rsi, rsp
			syscall

			jmp read_buffer 

exit:
			mov		rax, 60
			xor rdi, rdi
			syscall

			section .data
path:		db		"advent-storage/advent-23-1.txt", 0
