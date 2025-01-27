from characters.Character import Character

# TODO when characters swap, their IDs also need to swap (permanently)

def swap(charA: Character, charB: Character):
    currentAddressA = int(charA.startingAddress, 16)
    currentAddressB = int(charB.startingAddress, 16)
    resultList = []

    for byte in charA.getCharacterByteList()[:4]:
        hexAddress = '0x' + format(currentAddressB, 'X')
        resultList.append((hexAddress, byte))
        currentAddressB += 1

    currentAddressB += 1

    for byte in charA.getCharacterByteList()[5:]:
        hexAddress = '0x' + format(currentAddressB, 'X')
        resultList.append((hexAddress, byte))
        currentAddressB += 1

    for byte in charB.getCharacterByteList()[:4]:
        hexAddress = '0x' + format(currentAddressA, 'X')
        resultList.append((hexAddress, byte))
        currentAddressA += 1

    currentAddressA += 1

    for byte in charB.getCharacterByteList()[5:]:
        hexAddress = '0x' + format(currentAddressA, 'X')
        resultList.append((hexAddress, byte))
        currentAddressA += 1
    return resultList
