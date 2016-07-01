# coding=utf-8

import argparse

leetDict = {
  'a': ['a', 'A', '@', '4', 'À'],
  'b': ['b', 'B', 'I3', 'l3', 'i3'],
  'c': ['c', 'C', '(', 'k', 'K'],
  'd': ['d', 'D'],
  'e': ['e', 'E', '3'],
  'f': ['f', 'F', 'ph', 'pH', 'Ph', 'PH'],
  'g': ['g', 'G', '6'],
  'h': ['h', 'H', '#'],
  'i': ['i', 'I', 'l', '!', '1'],
  'j': ['j', 'J'],
  'k': ['k', 'K', '(', 'c', 'C'],
  'l': ['l', 'L', '1', '!', 'i'],
  'm': ['m', 'M'],
  'n': ['n', 'N'],
  'o': ['o', 'O', '0'],
  'p': ['p', 'P'],
  'q': ['q', 'Q', '9'],
  'r': ['r', 'R'],
  's': ['s', 'S', '$', '5'],
  't': ['t', 'T', '7', '+'],
  'u': ['u', 'U', 'v', 'V'],
  'v': ['v', 'V', 'u', 'U'],
  'w': ['w', 'W', 'vv', 'VV'],
  'x': ['x', 'X'],
  'y': ['y', 'Y'],
  'z': ['z', 'Z', '2']
}

def permute(dictWord):
  if len(dictWord) > 0:
    currentLetter = dictWord[0]
    restOfWord = dictWord[1:]
    if len(restOfWord) > 0:
      perms = [s + p for s in leetDict[currentLetter] for p in permute(restOfWord)]
    else:
      perms = leetDict[currentLetter]
    return perms

parser = argparse.ArgumentParser(description='Permutate words of a wordlist.')
parser.add_argument('input_file', help='an input wordlist')
parser.add_argument('output_file', help='an output file for permuted wordlist')

args = parser.parse_args()

bplf = open(args.input_file, 'r')
profaneWords = bplf.read().splitlines()
bplf.close()

pplf = open(args.output_file, "w")

print 'Working...'

for profaneWord in profaneWords:
  pplf.writelines([p + '\n' for p in permute(profaneWord)])

pplf.close()

print 'Done.'
