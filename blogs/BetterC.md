# Better C

# WIP!

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

### stdint.h

Defined in `stdint.h` header, you can use `uint_8` (unsigned 8bit integer), `uint_32` (unsigned 32bit integer), etc for specific type/size of integer. Of course, in stdint.h, they are just typedefs.

```c
int main(void){
    unsigned char y = 5;
    uint8_t x = 5; // Much cleaner!
    //....
}
```

### stdbool.h

Defined in `stdbool.h` header, you can use bool as boolean type `true`/`false`. In stdbool.h, they too are just typedef of int.

```c
int main(void){
    int boolean = 1;
    boolean = 0;

    // Much cleaner!
    bool x = true;
    x = false
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

Some people might see this one and be like WHAT?!. Well, idk what to say, I am including this point because I have seen people (especially C beginner) make this mistake, even professor have this in slides (I guess this is why).

You really shouldn't skip null check for heap memory allocation, because allocation can fail for multiple reason, and when it not checked properly, then somewhere in your program some code will try to access NULL which will result in segmentation fault, and this can be super hard to debug.

## NULL that pointer

After freeing malloc pointer, it better to null it, so that pointer which might still point to valid address but have garbage value, don't get accesed. Otherwise it will introduce bug, which is hard to track down. Nulling it will give you seg fault on accessing or help `-fsanitize=undefined,address` catch it.

```c
int main(void){
    int* x = (int*) malloc(sizeof(int)*5);
    assert(x!=NULL);
    x[1] = 5;

    free(x);

    printf("%d", x[1]);// Access is valid (shouldn't be), but value is garbage!

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

    printf("%d", x[1]);// Seg faults!

    return 0;
}
```
## Use debugger and address sanitizer

TODO for ARKA

- Use debugger like [gdb](https://sourceware.org/gdb/) ([lldb](https://lldb.llvm.org) for macos) to step through and inspect your code.
- To check for memory management related bugs, you can use AddressSans or software like valgrind.

## Raise the flags

TODO for ARKA

Use flags when compiling to catch potential bugs.

(Examples are of `gcc`)

- `-Wall`, enable all warning, all warning that might lead to bugs in code.
- `-Wextra`, some extra warnings.
- `-Werror`, treat warning as error, this is to enforce that programmer actually fix the warning and not just ignore it.
- `-pendantic`, Enforce ISO C standard, make code more portable as different compiler have different implementations.
- `-fsanitize=undefined`, check for undefined behaviour according to C standard.