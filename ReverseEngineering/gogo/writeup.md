# Gogo

## Given
- An ELF file 'enter_password'
- Clue： 'mercury.picoctf.net:6516'

## Process
* Execute the ELF file. It asks for a password. After we enter some random gibberish, no response is given. 
* Open the file with Ghidra and try to identify the `main()`. In return we can find a function called `main.main`. Let's study `main.main`.
* Here is the snippet where it prints the string "Enter password:" to the terminal. If you look at address `&DAT_080fea50`, it contains an array of characters that stores "Enter password:".
```Golang
  fmt.Printf(in_stack_ffffffac,(undefined4 *)&DAT_080fea50,(undefined4 *)0x10,0,(undefined4 *)0x0,0);
  local_18[0] = &DAT_080e1300;
  ppuVar4 = local_18;
  fmt.Scanf(&DAT_080e1300,(int)&DAT_080fd1b6,3,(int)ppuVar4,1,1);
  cVar6 = (char)ppuVar4;
  main.checkPassword(in_stack_ffffffac[1],*in_stack_ffffffac,in_stack_ffffffac[1]);
```
* Then `Scanf` it reads our input. By the way, as the `Scanf` is called through an fmt package, this program should be written in Golang, which kind of matches with the title. Our input is stored in address `&DAT_080e130`
* After that, `main.checkPassword()` is called. I suspect this function is validating our input. Let's see what it does. 
```Golang
void __regparm1 main.checkPassword(undefined4 param_1,int param_2, uint param_3)
{
  uint *puVar1;
  uint uVar2;
  undefined4 uVar3;
  int iVar4;
  int *in_GS_OFFSET;
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  undefined4 local_34;
  undefined4 local_30;
  undefined4 local_2c;
  undefined4 local_28;
  undefined4 local_24;
  byte local_20 [28];
  undefined4 uStack4;
  
  puVar1 = (uint *)(*(int *)(*in_GS_OFFSET + -4) + 8);
  if (register0x00000010 < (undefined *)*puVar1 ||
      (undefined *)register0x00000010 == (undefined *)*puVar1) {
    uStack4 = 0x80d4b72;
    uVar3 = runtime.morestack_noctxt(param_1);
    main.checkPassword(uVar3,param_2,param_3);
    return;
  }
  if ((int)param_3 < 0x20) {
    os.Exit(param_1,0);
  }
  FUN_08090b18(0);
  local_40 = 0x38313638;
  local_3c = 0x31663633;
  local_38 = 0x64336533;
  local_34 = 0x64373236;
  local_30 = 0x37336166;
  local_2c = 0x62646235;
  local_28 = 0x39383338;
  local_24 = 0x65343132;
  FUN_08090fe0();
  uVar2 = 0;
  iVar4 = 0;
  while( true ) {
    if (0x1f < (int)uVar2) {
      if (iVar4 == 0x20) {
        return;
      }
      return;
    }
    if ((param_3 <= uVar2) || (0x1f < uVar2)) break;
    if ((*(byte *)(param_2 + uVar2) ^ *(byte *)((int)&local_40 + uVar2)) == local_20[uVar2]) {
      iVar4 = iVar4 + 1;
    }
    uVar2 = uVar2 + 1;
  }
  runtime.panicindex();
  do {
    invalidInstructionException();
  } while( true );
}
```
* We see there is a while loop that perform binary XOR operation on two characters and compare the result to something. 
``` Assembly
        080d4b18 0f b6 2c 01     MOVZX      EBP,byte ptr [ECX + param_1*0x1]
        080d4b1c 83 f8 20        CMP        param_1,0x20
        080d4b1f 73 45           JNC        LAB_080d4b66
        080d4b21 0f b6 74        MOVZX      ESI,byte ptr [ESP + param_1*0x1 + 0x4]
                 04 04
        080d4b26 31 f5           XOR        EBP,ESI
        080d4b28 0f b6 74        MOVZX      ESI,byte ptr [ESP + param_1*0x1 + 0x24]
                 04 24
        080d4b2d 95              XCHG       param_1,EBP
        080d4b2e 87 de           XCHG       ESI,EBX
        080d4b30 38 d8           CMP        param_1,BL

```
* Since the XOR happens at `0x080d4b26`, let's enter Ghidra and set up breakpoint at `0x080d4b28` to see the arrays that participate the XOR
## Solution

## Flag