# Reverse Engineering

## A Tangled Web We Weave

The flag has been hidden in these assembly instructions, except I forgot how to decode it... If you figure it out you get the flag.

```asm
section .data
    encoded_message db 0x0F, 0x10, 0x1C, 0x0B, 0x19, 0x04, 0x0A, 0x08, 0x0C, 0x0F, 0x20, 0x14, 0x4E, 0x11, 0x46, 0x20, 0x14, 0x4F, 0x11, 0x46, 0x20, 0x46, 0x4F, 0x48, 0x20, 0x11, 0x4F, 0x48, 0x17, 0x4E, 0x11, 0x46, 0x20, 0x4F, 0x11, 0x20, 0x12, 0x4C, 0x02

section .text
    global _start

_start:
    mov ecx, 0
    mov edi, encoded_message
    find_length:
        cmp byte [edi], 0
        je print_message
        inc ecx
        inc edi
        jmp find_length

    print_message:
        xor esi, esi
        mov edi, encoded_message
        decode:
            xor eax, eax
            mov al, byte [edi + esi]
            xor al, ; something missing?
            mov byte [edi + esi], al
            inc esi
            cmp byte [edi + esi], 0
            jne decode

        mov edx, ecx
        mov eax, 4
        mov ebx, 1
        mov ecx, encoded_message
        int 0x80

    mov eax, 1
    xor ebx, ebx
    int 0x80
```

---

### Solution

https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')Magic(3,true,false,'poctf')&input=MEYgMTAgMUMgMEIgMTkgMDQgMEEgMDggMEMgMEYgMjAgMTQgNEUgMTEgNDYgMjAgMTQgNEYgMTEgNDYgMjAgNDYgNEYgNDggMjAgMTEgNEYgNDggMTcgNEUgMTEgNDYgMjAgNEYgMTEgMjAgMTIgNEMgMDI

So, the `something missing?` is xor with `0x7f`.

### poctf{uwsp_4d_v1c70r14m_w4573l4nd3r}