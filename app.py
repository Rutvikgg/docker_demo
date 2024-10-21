def draw_pyramid(height):
    for i in range(height):
        # Print spaces for alignment
        print(' ' * (height - i - 1), end='')
        # Print stars
        print('*' * (2 * i + 1))

def main():
    height = 5  # Hardcoded height of the pyramid
    draw_pyramid(height)

if __name__ == "__main__":
    main()
