---
layout: post
title: x64bg Tips and tricks
---

Since I like to use the commandline a lot, I found the following useful in x64dbg.

Save the memory region from where the PTR in the CPU register points to.

Example:
```
savedata c:\dumpfolder\dump1.bin,mem.decodepointer(esi),mem.size(esi)
```

If you want to dump from the base address of the memory region pointed to by the CPU register instead.
Example:
```
savedata c:\dumpfolder\dump_test.bin,mem.base(edi),mem.size(edi)
```
Also works with stackpointers:
Example:
```
savedata c:\dumpfolder\dump_test.bin,mem.base([esp+24]),mem.size([esp+24])
```

Conditional breakpoint oneliner example set on a CPU register. These also work with stack pointers.
Example:
```
bp VirtualAlloc;bpcnd VirtualAlloc,mem.valid('[cpu register] OR [stack pointer]');SetBreakpointFastResume VirtualAlloc, 1
```

If we break down the syntax, we first set a breakpoint on the API function "VirtualAlloc". Then we set at condition for the breakpoint, so that it will only stop when condition X is met. Useful if malware calls the function multiple times. In order for x64dbg not  break on the BP every time, we also have to set "SetBreakpointFastResume" to True.

The x64dbg doc states this for "SetBreakpointFastResume, sets the fast resume flag of a software breakpoint. If this flag is set and the break condition doesn’t evaluate to break, no GUI, plugin, logging or any other action will be performed, except for incrementing the hit counter."

There is also the condition "mem.iscode" which will break on a memory page that is set as executable, which also may be useful for you.

You can also try CPU register or stack pointer == value.

For example:
```
bp VirtualAlloc;bpcnd VirtualAlloc,[esp+24]==PE;SetBreakpointFastResume VirtualAlloc, 1
bp VirtualAlloc;bpcnd VirtualAlloc,[EDI]==PE;SetBreakpointFastResume VirtualAlloc, 1
```

More tips here:
https://help.x64dbg.com/en/latest/introduction/Expression-functions.html