from stack import Stack

def show_input_options(choices):
    for name in choices:
        print("Enter {} for {}".format(name[0], name))


def get_input(prompt):
    choices = ['Left', 'Middle', 'Right']
    letterToStack = dict(zip('lmr', stacks))
    while True:
        show_input_options(choices)
        user_input = input(prompt)
        if user_input.lower() in letterToStack:
            return letterToStack[user_input]


print("\nLet's play Towers of Hanoi!!\n")

print("The game follows three rules:\n")

print("1. Only one disk can be moved at a time.\n")

print("2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.\n")

print("3. No disk may be placed on top of a smaller disk")

stacks = [[], [], []]
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))
stacks[0] = list(range(num_disks, 0, -1))

num_optimal_moves = (2**num_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves"
      .format(num_optimal_moves))


num_user_moves = 0
while len(stacks[-1]) != num_disks:
    while True:
        print("\n\n\n...Current Stacks...")
        for stack in stacks:
            print(stack)
        from_stack = get_input("\nWhich stack do you want to move from?\n> ")
        to_stack = get_input("\nWhich stack do you want to move to?\n> ")
        if not from_stack:
            print("\n\nInvalid Move. Try Again")
        elif len(to_stack) == 0 or from_stack[-1] < to_stack[-1]:
            disk = from_stack.pop()
            to_stack.append(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")

print("You completed the game in {0} moves! The optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))