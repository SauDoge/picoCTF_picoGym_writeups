# Hurry Up! Wait!

## Given
- An executable file 'svchost.exe'

## Process
- The file appears to have .exe extension, but it is actually an ELF if we check it with `file` on the terminal
```
svchost.exe: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=dffd9a6bc115677c3b91a1497e6f38affeaf8f50, stripped
```
- Try executing the file after changing the extension but an error return 
```
./svchost.elf: error while loading shared libraries: libgnat-7.so.1: cannot open shared object file: No such file or directory
```
- A shared library called "libgnat-7.so.1" is missing. After some googling, I found out that it is a library that provide runtime components used by applications compiled with GNAT, where GNAT is a compiler for a programming language called Ada. Therefore this program is most likely written in Ada.

- Let's use Ghidra to open the file instead and ignore the missing library at the moment. 

- I start by looking into the functions in the symbol tree with the decompiler. The `entry` should be the starting function.

```Ada
void entry(undefined8 param_1,undefined8 param_2,undefined8 param_3)
{
  undefined8 in_stack_00000000;
  undefined auStack8 [8];
  
  __libc_start_main(FUN_00101fcc,in_stack_00000000,&stack0x00000008,FUN_00102a30,FUN_00102aa0,
                    param_3,auStack8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```
- [`__libc_start_main` ](https://refspecs.linuxbase.org/LSB_3.1.0/LSB-generic/LSB-generic/baselib---libc-start-main-.html) will perform initalization of execution environment, so it should be the starting point. `FUN_00101fcc` should be the main(). Let's check what it does.

``` Ada
undefined4 FUN_00101fcc(undefined4 param_1,undefined8 param_2,undefined8 param_3)

{
  undefined local_10 [8];
  
  gnat_envp = param_3;
  gnat_argv = param_2;
  gnat_argc = param_1;
  __gnat_initialize(local_10);
  FUN_00101d7c();
  FUN_0010298a();
  FUN_00101d52();
  __gnat_finalize();
  return gnat_exit_status;
}
```
- There are three functions called: `FUN_00101d7c()`, `FUN_0010298a()`, `FUN_00101d52()`. Let's check what they do.
    * `FUN_00101d7c()` appears to be some sort of initialization procedures as we can see lines like `__gnat_runtime_initialize(1);`. 
    * `FUN_0010298a()` calls a shit ton of other functions. I then moved on to check what they do.
```
void FUN_0010298a(void)
{
  ada__calendar__delays__delay_for(1000000000000000);
  FUN_00102616();
  FUN_001024aa();
  FUN_00102372();
  FUN_001025e2();
  FUN_00102852();
  FUN_00102886();
  FUN_001028ba();
  FUN_00102922();
  FUN_001023a6();
  FUN_00102136();
  FUN_00102206();
  FUN_0010230a();
  FUN_00102206();
  FUN_0010257a();
  FUN_001028ee();
  FUN_0010240e();
  FUN_001026e6();
  FUN_00102782();
  FUN_001028ee();
  FUN_00102102();
  FUN_001023da();
  FUN_0010226e();
  FUN_001021d2();
  FUN_00102372();
  FUN_001023a6();
  FUN_001021d2();
  FUN_00102956();
  return;
}
```
- Every function called has a similar pattern of only calling `ada__text_io__put__4()` with different parameters. We can check what it does in the [documentation](https://learn.adacore.com/courses/intro-to-ada/chapters/standard_library_files_streams.html#text-i-o). It seems that the function will write some text into a location. Here is an example:
```Ada
void FUN_00102616(void)

{
  ada__text_io__put__4(&DAT_00102cd8,&DAT_00102cb8);
  return;
}
```
- `&DAT_00102cd8` stores the character 'p', while `&DAT_00102cb8` looks like a random memory location (according to [this writeup](https://dmfrsecurity.com/2021/11/01/picoctf-2021-hurry-up-wait-writeup/), it should be the stdout)

## Solution
- Check the character written in every `ada_text_io_put__4()` function call. 
- The characters together should be the flag.

## Flag
> picoCTF{d15a5m_ftw_0e74cd4}