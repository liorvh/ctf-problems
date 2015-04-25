# stack:
# two dimensional
# [brainfuck code]
# [brainfuck stack]

# in C code, obfuscate stack with big endian longs instead of an array of chars

# overview
# stack:
# [opcodes] 
# [0, 42, 0, 57, 0, 49, 0, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 72, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 191, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 87, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 4, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 157, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 222, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 212, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 69, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 43, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 44, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 174, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 252, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 74, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 148, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 6, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 228, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 22, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 4, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 4, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 105, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 59, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 186, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 87, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 137, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 206, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 54, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 41, 3, 1, 3, 3, 1, 0, 1, 1, 5, 1, 2, 4, 2, 0, 6]

# opcodes:
# push val
#   push val onto the stack
# get val
#   push value at val onto the stack
# store val
#   pop value, store at val
# nor
#   nor two top (universal gate)
# add
#   add two top (wraps around at byte)
# mult
#   multiply two top (wraps around at byte)
# ret
#   stop and return value
# cmp val
#   set zero flag to comparison
# input
#   push input byte onto the stack

d = {
'push':'\x00',
'get':'\x01',
'store':'\x02',
'nor':'\x03',
'add':'\x04',
'mult':'\x05',
'ret':'\x06',
'cmp':'\x07',
'input':'\x08'}

# g: stack# position get
# s: stack# position val store
# p: pop
# n: nor
# c: cmp
# i: input
# |: a<b up, a>b down, a=b straight
# _: a<b left, a>b right, a=b straight

# init registers
jj00
# get opcode
021gg
    # inc eip: 2121g1+s
    # inc esp: 2020g1+s
    # dec esp: 2020g1-s
    # get op: 021gg
    # get stack: 120g1-g
    # push val:0
    (1 20g (inc eip, get op) s) inc esp pop
    120g2121g1+s021ggs2020g1+sp
    # get val:1
    (1 20g (1 (inc eip, get op) g) s) inc esp pop
    120g12121g1+s021gggs2020g1+sp
    # store val:2
    (1 (inc eip, get op) (get stack) s) dec esp pop
    12121g1+s021gg120g1-gs2020g1-sp
    # nor3
    dec esp (1 20g1- ((get stack 0) (get stack) nor) s) pop
    2020g1-s120g1-120gg120g1-gnsp
    # add4
    (1 20g ((get stack) dec esp (get stack) +) s) pop
    2020g1-s120g1-120gg120g1-g+sp
    # mult5
    (1 20g ((get stack) dec esp (get stack) *) s) pop
    2020g1-s120g1-120gg120g1-g*sp
    # ret6
    (get stack) ret
    120g1-gr
    # cmp val7
    (1 20g1- (get stack (inc eip, get op) cmp) s) pop
    120g1-120g1-g2121g1+s021ggcsp
    # input8
    (1 20g input s) inc esp pop
    120gis2020g1+sp
    # mod9
    (1 20g1- (get stack m) s) pop
    120g1-120g1-gmsp

    inc eip
    2121g1+s
