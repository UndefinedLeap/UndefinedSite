# WIP WIP WIP WIP WIP

# Cokoban, sokoban game written in C

Sokonban is puzzle type game, where you push around objects and put them on 'trigger' to open door, to get to your goals.

Game will be written in C with [sokol gfx](https://github.com/floooh/sokol) and [sokol gp](https://github.com/edubart/sokol_gp).

## Setup

### Zig's Build system

We will be using zig compiler as build system, this will make building project and make cross-compilation easier.
Though, it is completely possible for you to use your own build systems.
You can download zig from [here](https://ziglang.org/download/).

### Building

1. Clone [Sokol2DStarterProject](https://github.com/BlackGoku36/Sokol2DStarterProject). We will start creating game from starter project.

```bash
git clone https://github.com/BlackGoku36/Sokol2DStarterProject.git
```

2. After repo is clone build it:

```bash
zig build run
```

You should see something like this (rotating colorful square):

![](../assets/CK2D1.png)

> At moment only supported platform are MacOS (Metal) and Windows (OpenGL). But it should be pretty easy compile for other gapi backends and OSes. <br>(Hint: You just have to edit `build.zig`!).

[**Part 2**](CK2D2.html)

---

Check code repository: [Cokoban](https://github.com/BlackGoku36/Cokoban)
