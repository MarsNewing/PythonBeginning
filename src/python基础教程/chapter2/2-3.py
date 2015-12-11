# create a box which adjust its size according to the length of sentence

inputStr = raw_input("Sentence: ")
sentenceLength = len(inputStr)
boxWidth = sentenceLength + 6
firstRow = '+' + '-'*(boxWidth - 2) + '+'
secondRow = '|' + ' '*(boxWidth - 2) + '|'
sentenceRow = '|' + ' '*2 + inputStr + ' '*2 + '|'
outputStr = firstRow + '\n' + secondRow + '\n' + sentenceRow + '\n' + secondRow + '\n' + firstRow
print(outputStr)
