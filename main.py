from characters.CharacterHelper import getCharacters
from characters.party.Bartre import Bartre
from characters.party.Eliwood import Eliwood
from helper import flatten, maxAddress
from scripts import SkipTutorial, EditTitleScreen, ReassignCharacterIDsAndStats
from scripts.chapters import ChapterPrologue
from scripts.swap import swap

def main(input_file, output_file):

    allCharacters = getCharacters()
    # Drafted players list
    draftPicks = [allCharacters[2]]

    #Temporarily swap Raven and Lyn's IDs
    allCharacters[1].characterIDs.characterID = 0x04
    allCharacters[2].characterIDs.characterID = 0x03

    print(swap(allCharacters[1], allCharacters[2]))

    # Load all scripts
    updateList = flatten([
        SkipTutorial.get(),
        EditTitleScreen.get(),
        swap(allCharacters[1], allCharacters[2]),
        # ReassignCharacterIDsAndStats.get(draftPicks),
        ChapterPrologue.get(draftPicks)
    ])

    with open(input_file, 'rb') as file:
        data = bytearray(file.read())

    # Create an output and copy over the base game data
    outputData = bytearray(maxAddress(updateList) + 1)
    outputData[:len(data)] = data

    # Apply all loaded scripts
    for entry in updateList:
        address = int(entry[0], 16)
        try:
            outputData[address] = int(entry[1])
        except IndexError:
            print("Index out of bounds: " + str(address))
        except TypeError:
            print(entry[1])

    # Create a new file
    with open(output_file, 'wb') as file:
        file.write(outputData)

    print("Generation complete.")

if __name__ == "__main__":
    main('input.gba', 'output.gba')

