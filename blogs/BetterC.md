# Better C

Table Of Contents:

- Source code level:
    - [Empty Parameter List](#empty-paramter-list)
    - [Ints and Bools](#ints-and-bools)
    - [Asserts](#asserts)
    - [Return value of function](#return-value-of-function)
    - [NULLing the pointer](#nulling-the-pointer)
    - [goto](#goto)
    - [Etc](#etc)
    
- Compiler level:
    - [Flags](#flags)
    
- Tools level:
    - [Use debugger](#use-debugger)

## Source code level

---

### Empty Parameter List

In any language other than C, passing arguments to an empty function parameter list will result in an error. So this is a valid code in C.

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

### Ints and Bools

- From `stdint.h`, you can use `uint8_t` (unsigned 8bit integer), `uint32_t` (unsigned 32bit integer), etc, for specific type and size of integer.
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

### Asserts

Assert macro tests expression and terminates the running process. Use this to stop your code if it has the potential to shoot itself in the foot.

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

Above is how many courses/tutorials check malloc's NULL. The problem with this is that even if `x` is NULL, your program will continue to run and crash further down the line. It will become harder to debug, even if you put pretty printfs. You can solve it by terminating the program with assert.

```c
#include<assert.h>

int main(void){
    int* x = (int*) malloc(sizeof(int));
    assert(x != NULL);
    some_more_code(x);
    return 0;
}
```
This will give you nice error:
```txt
Assertion failed: (x != NULL), function main, file main.c, line 5
```

Of course, you can choose what to do when malloc fails, but it can still be useful for, say, index out-of-bound checks or any other place where the program should stop.

### Return value of function

One thing we observed is that sometimes students don't check what functions return (especially of the standard library). Functions can report failure by returning `NULL`, `-1` or some error enum. And when these functions remain unchecked, you will miss this error and become annoyed and frustrated.

### NULLing the pointer

After freeing the malloc pointer, it is better to null it, so that pointer which might still point to a valid address but have a garbage value, doesn't get accessed. Otherwise, it will introduce a bug, which is hard to track down. Nulling it will give you seg fault on accessing or let the `-fsanitize=undefined,address` flag help catch it.

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

### goto

The `goto` keyword let the program jumps to a labelled statement.

```c
int main(void){
    printf("hello");
    goto world;
    printf(" bye!");
    world:
        printf(" world!");
    return 0;
}
```
```txt
hello world!
```

While it might be tempting to use goto for some complex control flows, not only it's complicated jumping from here and there but also its `fall-through` behaviour like the `switch` statement, will make it hard to be handled.

```c
int main(void){
    printf("hello");
    goto world;
    world:
        printf(" world!");
    bye:
        printf(" bye!");
    return 0;
}
```
```txt
hello world! bye!
```

So, only use goto as defer mechanism to handle errors. Otherwise, there might be a code smell in whatever you are trying to do.

```c
#include<errno.h>

// A way to handle errors with goto
int main(void){
    FILE* file_txt = fopen("file.txt", "w");
    if(file_txt == NULL) goto err;
    
    fprintf(file_txt, "TEST!\n");
    
    fclose(file_txt);
    
    err:
        printf("Error %s encountered!", strerror(errno));
    return 0;
}
```
### Etc

- Function-like macros: This should only be used if your functions are small because macros (pre-processor) don't understand anything about language and only copy-paste. It will result in buggy code that is hard to debug.

- Variadic functions: This should be strictly avoided as it doesn't have any type-safety and can easily break your program or introduce security vulnerabilities.

## Compiler level

---

### Flags

Use flags when compiling to catch potential bugs.

(Examples are of `gcc`)

- `-Wall`, enable all warnings, all warnings that might lead to bugs in code.
- `-Wextra`, some extra warnings.
- `-Werror`, treat warning as an error, this is to enforce that programmer fixes the warning and not just ignore it.
- `-Wpendantic`, Enforce ISO C standard, make code more portable as different compilers have different implementations.
- `-Wconversion`, warn when invalid conversion between int/float/double and of different size occurs.
- `-Wshadow`, warn when variable shadows previously declared variables.
- `-std=cxx`, uses `cxx` compiler, so that code conforms to that particular ISO C standard.
- `-fsanitize=<a>,<b>,<c>`, use santizer to catch bugs.
- `-fsanitize=undefined`, check for undefined behaviour.
- `-fsanitize=address`, check for out-of-bounds and use-after-free bugs.
- `-fsanitize=leak`, check for memory leaks.
- [more](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html)

## Tools level

---

### Use debugger

Beginners nowadays only use `printf` to check the code states and variables to debug their projects. The problem is that it is hard to properly read the code states and variables even if you have pretty `printf` messages. Even if you do, you would be spending much of your time copy-pasting `printf` and editing them. It would make them pretty counter-productive.

Beginners should try to get their hands dirty with debuggers like [gdb](https://sourceware.org/gdb/)/[lldb](https://lldb.llvm.org) even if it takes some time out of their free time. Because, once you get used to debuggers, you can easily debug your code without wasting time.

Another amazing use case for a debugger is that you can use it to explore and get familiar with a new codebase, as you can check the execution flow easily.

> You like printf debugging?
>
<br>
> Introducing a tool called the Debugger. It automatically adds printf debug for every variable in your code base and collects that info into a nice UI. You can pause the execution, continue it and step one line at a time to see your execution flow.
>
<br>
> -[Sebastian Aaltonen](https://twitter.com/SebAaltonen/status/1571039580908040192)
