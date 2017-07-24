# from projectzero BCMPatcher/patch.py
THUMB2_INST_WIDTH = 4
def encode_thumb2_wide_branch(from_addr, to_addr):
	'''
	Encodes an unconditional THUMB2 wide branch from the given address to the given address.
	'''
	
	if from_addr < to_addr:
		s_bit = 0
		offset = to_addr - from_addr - THUMB2_INST_WIDTH
	else:
		s_bit = 1
		offset = 2**25 - (from_addr + THUMB2_INST_WIDTH - to_addr)

	i1 = (offset >> 24) & 1
	i2 = (offset >> 23) & 1
	j1 = (0 if i1 else 1) ^ s_bit
	j2 = (0 if i2 else 1) ^ s_bit

	b2 = 0b11110000 | (s_bit << 2) | ((offset >> 20) & 0b11)
	b1 = (offset >> 12) & 0xff
	b4 = 0b10010000 | (j1 << 5) | (j2 << 3) | ((offset >> 9) & 0b111)
	b3 = (offset >> 1) & 0xff
	return b1 | (b2 << 8) | (b3 << 16) | (b4 << 24)
print(hex(encode_thumb2_wide_branch(0x18b68c, 0x217090)))
print(hex((encode_thumb2_wide_branch(0x18b68c, 0x217090) - 0x43f0e92d) & 0xffffffff))
print(hex(encode_thumb2_wide_branch(0x21709a, 0x18b690)))
