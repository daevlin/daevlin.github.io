```c
void __cdecl fcn.00405fb3(int32_t arg_8h, int32_t arg_ch, int32_t arg_10h, uint32_t arg_14h)
{
    uint8_t *puVar1;
    uint8_t uVar2;
    uint32_t uVar3;
    int32_t unaff_EDI;
    uint32_t uVar4;
    int32_t var_124dch;
    int32_t var_122ach;
    int32_t var_122a8h;
    int32_t var_122a4h;
    int32_t var_122a0h;
    uint8_t auStack74400 [74384];
    int32_t var_4h;
    
    fcn.004161d0();
    uVar4 = 0;
    uVar3 = 0;
    if (arg_14h != 0) {
        do {
            auStack74400[uVar3] = (uint8_t)uVar3;
            uVar3 = uVar3 + 1;
        } while (uVar3 < 0x12296);
        var_122a4h = 0;
        do {
            uVar2 = auStack74400[var_122a4h];
            uVar4 = ((uint32_t)uVar2 + *(uint8_t *)((uint32_t)var_122a4h % (uint32_t)arg_ch + arg_8h) + uVar4) % 0x12296
            ;
            auStack74400[var_122a4h] = auStack74400[uVar4];
            auStack74400[uVar4] = uVar2;
            var_122a4h = var_122a4h + 1;
        } while ((uint32_t)var_122a4h < 0x12296);
        uVar3 = 0;
        var_122ach = 0;
        var_122a0h = arg_10h;
        do {
            arg_14h = arg_14h - 1;
            uVar3 = (uVar3 + 1) % 0x12296;
            puVar1 = auStack74400 + uVar3;
            uVar2 = *puVar1;
            var_122ach = ((uint32_t)uVar2 + var_122ach) % 0x12296;
            *puVar1 = auStack74400[var_122ach];
            auStack74400[var_122ach] = uVar2;
            fcn.00405ef3(0);
            *(uint8_t *)var_122a0h =
                 *(uint8_t *)var_122a0h ^ auStack74400[((uint32_t)*puVar1 + (uint32_t)uVar2) % 0x12296];
            var_122a0h = var_122a0h + 1;
            fcn.00403d12();
        } while (arg_14h != 0);
    }
    fcn.00415a8b(unaff_EDI);
    return;
}
```
