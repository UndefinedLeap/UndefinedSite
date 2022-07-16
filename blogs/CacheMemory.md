# Cache Memory Notes

## What a cache memory?

DRAM performance improve lot slower compared to CPU performance, as a result DRAM and CPU performance gap keep on increasing. Chances are that your CPU is already done it's job and is waiting (idling) for data from DRAM to continue further, here the DRAM speed is bottelnecking CPU speed. To solve this, we put smaller but faster (also more costy) memory on CPU. Chunk(s) of memory (DRAM) is loaded into this, so that CPU can immediately access it. This memory is know as cache memory.

Memory hierarchy looks something like this:

```txt
                          |  DRAM
    Size and              |  L3 (shared between processes)
         latency decrease |  L2
                          v  L1 (Data), L1 (Instruction)
```
*Hierarchy is showen as formality, we don't have to keep levels of cache is mind when programming*

## Associativity

### Direct-mapped cache

TBD

### Set-associative cache

TBD

### Fully associative cache

TBD

---

Agenda:

- Explain what cache memory is and why does it matter.
- What is direct mapped, associative and set-associative cache memory.
- Simple calculations of things like cache address bits and determine different things of the cache memory that helps with understanding of data in cache.
- Different types of misses and how it can be improved.
- Real-life example of code that hate cache:
    - Multiplication of huge N matrix with sub matrix and how it can be optimised.
    - Why Linked list sucks in this regard.
- Why nobody (except those who want high performance design, I don't think cache memory is big brain thing tho) seems to give fuck about cache memory even if it taught in university.