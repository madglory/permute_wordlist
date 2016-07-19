# coding=utf-8

import argparse

leetDict = {
  'c': ['c', '(', 'k', 'K'],
  'f': ['f', 'ph', 'pH', 'Ph', 'PH'],
  'i': ['i', 'l', '!', '1'],
  'k': ['k', '(', 'c', 'C'],
  'l': ['l', '1', '!', 'i'],
  'u': ['u', 'v', 'V'],
  'v': ['v', 'u', 'U'],
  'w': ['w', 'vv', 'VV']
}

def permute(dictWord):
  if len(dictWord) > 0:
    currentLetter = dictWord[0]
    restOfWord = dictWord[1:]

    if currentLetter in leetDict:
        substitutions = leetDict[currentLetter]
    else:
        substitutions = [currentLetter]

    if len(restOfWord) > 0:
      perms = [s + p for s in substitutions for p in permute(restOfWord)]
    else:
      perms = substitutions
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
