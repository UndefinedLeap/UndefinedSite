# Better C

> WIP!

Table Of Contents:

- [Void the empty paramter list](#void-the-empty-paramter-list)
- [Stdint.h, Stdbool.h](#stdint.h-stdbool.h)
- [Use asserts](#use-asserts)
- [Handle alloc's NULLs](#handle-allocs-nulls)
- [NULL that pointer](#null-that-pointer)
- [goto](#goto)
- [Macro like functions](#macro-like-functions)
- [Variadic functions](#variadic-functions)
- [Use debugger](#use-debugger)
- [Raise the flags](#raise-the-flags)

A small guide for C beginners out there to help them write better C code.

## Void the empty parameter list

In any language other than C, passing arguments to empty function parameter list will result in error. So this is valid code in C.

```c
void foo(){
    printf("hello");
}

int main(){
    foo(5); // Should error!
    return 0;
}
```
To solve this, we use void to explictly mark the function paramenter list as empty.
```c
void foo(void){
    printf("hello");
}

int main(){
    foo(5); // error: too many arguments to function 'foo'
    return 0;
}
```

## stdint.h, stdbool.h

- From `stdint.h`, you can use `uint_8` (unsigned 8bit integer), `uint_32` (unsigned 32bit integer), etc, for specific type and size of integer.
- From `stdbool.h`, you can use `bool` as boolean type `true`/`false`.

In both of header, they are just typedefs.

```c
int main(void){
    unsigned char x = 5;

    int is_true = 1;
    is_true = 0;
}
```

```c
int main(void){
    // Much cleaner!
    uint8_t x = 5;

    bool is_true = true;
    is_true = false;
}
```

## Use asserts

Assert macro tests expression and terminates the running process. Use this to stop your code if it has potential to shoot itself in foot.

```c
int main(void){
    int* x = (int*) malloc(sizeof(int));
    if(x == NULL){
        printf("OOF!");
    }
    some_more_code(x);
    return 0;
}
```

This is how it usually handled in many courses/tutorials. The problem with this is that even if `x` is NULL, there nothing stoping your program from running further, and crashing (or maybe not!) further down the line. This will make it harder to debug, even if you put some specific printfs. You can solve it by terminating the program with assert.

```c
#include<assert.h>

int main(void){
    int* x = (int*) malloc(sizeof(int));
    assert(x != NULL);
    some_more_code(x);
    return 0;
}
```
This will give you nice error: `Assertion failed: (x != NULL), function main, file main.c, line 5`.

Of course, practically you can choose what to do when malloc fails, but it can still be very usefull for, say array's index out-of-bound check, or any place where program should stop where it would result in nasty bugs.

## Handle alloc's NULLs

One thing that we have observed is that sometimes students doesn't check if `malloc`/`calloc`/etc returns `null` or not. This check shouldn't be skipped, because allocation can fail for multiple reason, and when it not checked properly, then somewhere in your program some code will try to access `null` pointer which will result in segmentation fault. And this can be hard to debug.

## NULL that pointer

After freeing malloc pointer, it better to null it, so that pointer which might still point to valid address but have garbage value, don't get accesed. Otherwise it will introduce bug, which is hard to track down. Nulling it will give you seg fault on accessing or let `-fsanitize=undefined,address` flag help catch it.

```c
int main(void){
    int* x = (int*) malloc(sizeof(int)*5);
    assert(x!=NULL);
    x[1] = 5;

    free(x);
    
    // Access is valid (shouldn't be!)
    // x[1] value is garbage!
    printf("%d", x[1]);

    return 0;
}
```

```c
int main(void){
    int* x = (int*) malloc(sizeof(int)*5);
    assert(x!=NULL);
    x[1] = 5;

    free(x);
    x = NULL;
    
    // Seg faults!
    printf("%d", x[1]);

    return 0;
}
```

## goto

> TODO

## Macro-like functions

> TODO

## Variadic functions

> TODO

## Use debugger

Beginners nowadays just use `printf` to check the code states and variable to debug their projects. The problem with this is that it hard to properly read the states and variables even if you have very pretty `printf` messages. Even if you do, you would be spending much of your time copy-pasting `printf` and editing them. This make them pretty counter-productive.

Beginners should try to get their hand dirty with debuggers like [gdb](https://sourceware.org/gdb/)/[lldb](https://lldb.llvm.org) even if it take some time out of their free time. Because, once you get used to debuggers, you can easily debug your code without wasting time.

Another amazing usecase for debugger is that you can use it to explore and get familiar with new codebase, as you can check the execution flow easily.

> You like printf debugging? 
> 
> Introducing a tool called the Debugger. It automatically adds printf debug for every variable in your code base and collects that info into a nice UI. You can pause the execution, continue it and step one line at a time to see your execution flow.
> 
> -[Sebastian Aaltonen](https://twitter.com/SebAaltonen/status/1571039580908040192)

## Raise the flags

> TODO

Use flags when compiling to catch potential bugs.

(Examples are of `gcc`)

- `-Wall`, enable all warning, all warning that might lead to bugs in code.
- `-Wextra`, some extra warnings.
- `-Werror`, treat warning as error, this is to enforce that programmer actually fix the warning and not just ignore it.
- `-pendantic`, Enforce ISO C standard, make code more portable as different compiler have different implementations.
- `-fsanitize=undefined`, check for undefined behaviour according to C standard.

> TODO: Use below links and update `-fsanitize=<a>,<b>,<etc>` point.
> 
> https://www.osc.edu/resources/getting_started/howto/howto_use_address_sanitizer
> https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html