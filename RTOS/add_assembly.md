assembly code output:
# installation 
 sudo apt update && sudo apt install gcc-arm-none-eabi binutils-arm-none-eabi gdb-multiarch build-essential

 sudo apt-get install vim


# command to compile
msis@msis-HP-Pro-Tower-400-G9-PCI-Desktop-PC:~/sandbox/001_add_prog$ arm-none-eabi-gcc -mcpu=cortex-m3 -mthumb -O0 -g -c add_prog.c -o add_prog.o

# command to get output
msis@msis-HP-Pro-Tower-400-G9-PCI-Desktop-PC:~/sandbox/001_add_prog$ arm-none-eabi-objdump -S add_prog.o

add_prog.o:     file format elf32-littlearm


Disassembly of section .text:

00000000 <main>:
int main(void)
{
   0:	b480      	push	{r7}
   2:	b085      	sub	sp, #20
   4:	af00      	add	r7, sp, #0
  int a=10,b=20;
   6:	230a      	movs	r3, #10
   8:	60fb      	str	r3, [r7, #12]
   a:	2314      	movs	r3, #20
   c:	60bb      	str	r3, [r7, #8]
  int c =a+b;
   e:	68fa      	ldr	r2, [r7, #12]
  10:	68bb      	ldr	r3, [r7, #8]
  12:	4413      	add	r3, r2
  14:	607b      	str	r3, [r7, #4]
  16:	2300      	movs	r3, #0
}
  18:	4618      	mov	r0, r3
  1a:	3714      	adds	r7, #20
  1c:	46bd      	mov	sp, r7
  1e:	bc80      	pop	{r7}
  20:	4770      	bx	lr



This text is a disassembly of a compiled C program written for an ARM Cortex-M processor (using the 16-bit Thumb instruction set). It shows how a CPU executes a basic addition at the hardware level.
Here is the step-by-step breakdown, registry trace, and explanation of those hex values.
------------------------------
## Understanding the Basics

* Hex Numbers (e.g., b480, b085): These are Machine Code (Opcodes). They are the actual binary data stored in the chip's memory that the CPU decodes into actions.
* Registers: Tiny, ultra-fast memory slots inside the CPU.
* r0 - r3: General-purpose slots used for math and temporary data.
   * r7: The Frame Pointer. It points to the current function's local variables on the stack.
   * sp: The Stack Pointer. It tracks the top of the memory scratchpad (the Stack).
   * lr: The Link Register. It holds the return address (where to go when the function ends).

------------------------------
## Line-by-Line Execution Trace
The compiler allocates memory on the stack for your variables at specific offsets from r7:

* a is stored at [r7 + 12]
* b is stored at [r7 + 8]
* c is stored at [r7 + 4]

## 1. Function Setup (Prologue)

00000000 main int main void 
0   b480        push {r7}


* What it does: Saves the old value of r7 onto the stack so it isn't ruined.
* Machine Code (b480): b4 means "PUSH", 80 targets register r7.

2   b085        sub sp, #20


* What it does: Lowers the Stack Pointer by 20 bytes. This reserves 20 bytes of private memory workspace for this function's variables.

4   af00        add r7, sp, #0


* What it does: Sets r7 equal to the current sp. r7 is now the anchor point for our local variables.

------------------------------
## 2. Variable Initialization (int a = 10; b = 20;)

6   230a        movs r3, #10


* What it does: Loads the number 10 into register r3. (0a in hex is 10 in decimal).
* Register State: r3 = 10

8   60fb        str r3, [r7, #12]


* What it does: Stores (STR) the value in r3 into the stack memory at address r7 + 12. This represents variable a.
* Memory State: Variable a now equals 10.

a   2314        movs r3, #20


* What it does: Loads the number 20 into register r3. (14 in hex is 20 in decimal).
* Register State: r3 = 20

c   60bb        str r3, [r7, #8]


* What it does: Stores the value in r3 into the stack memory at address r7 + 8. This represents variable b.
* Memory State: Variable b now equals 20.

------------------------------
## 3. The Math Operation (int c = a + b;)

e   68fa        ldr r2, [r7, #12]


* What it does: Loads (LDR) the value of a (from r7 + 12) back into register r2.
* Register State: r2 = 10

10  68bb        ldr r3, [r7, #8]


* What it does: Loads the value of b (from r7 + 8) into register r3.
* Register State: r3 = 20

12  4413        add r3, r2


* What it does: Adds r2 and r3 together, saving the result into r3.
* Register State: r3 = 10 + 20 = 30

14  607b        str r3, [r7, #4]


* What it does: Stores the result (30) into the stack memory at address r7 + 4. This represents variable c.
* Memory State: Variable c now equals 30.

------------------------------
## 4. Preparing the Return Value (return 0;)

16  2300        movs r3, #0


* What it does: Loads 0 into r3.
* Register State: r3 = 0

18  4618        mov r0, r3


* What it does: Copies r3 into r0. In ARM architecture, the value in r0 is always used as the final return value of a function.
* Register State: r0 = 0

------------------------------
## 5. Function Cleanup (Epilogue)

1a  3714        adds r7, #20
1c  46bd        mov sp, r7


* What it does: These two lines clean up the stack space we borrowed, resetting sp back to where it was before the function started.

1e  bc80        pop {r7}


* What it does: Restores the original value of r7 for the previous function.
* Machine Code (bc80): bc means "POP", 80 targets r7.

20  4770        bx lr


* What it does: Branch and Exchange to Link Register. This jumps back to the code that called main in the first place, officially exiting the program.
