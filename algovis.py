import pygame
import random

# Initialize Pygame
pygame.init()

# Get the screen dimensions
SCREEN_INFO = pygame.display.Info()
WIDTH, HEIGHT = SCREEN_INFO.current_w, SCREEN_INFO.current_h

# Constants
BG_COLOR = (0, 0, 0)
BAR_WIDTH = 4
GAP = 2
NUM_BARS = WIDTH // (BAR_WIDTH + GAP)

# Create the full-screen screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Sorting Algorithms Visualizer")

# Generate a list of random heights for the bars
def generate_random_bars():
    return [random.randint(50, HEIGHT - 50) for _ in range(NUM_BARS)]

bar_heights_bubble = generate_random_bars()
bar_heights_quick = bar_heights_bubble.copy()
bar_heights_merge = bar_heights_bubble.copy()

# Sorting algorithm labels
font = pygame.font.Font(None, 36)
bubble_label = font.render("Bubble Sort", True, (255, 0, 0))
quick_label = font.render("Quick Sort", True, (0, 255, 0))
merge_label = font.render("Merge Sort", True, (0, 0, 255))

# Small font for individual bar labels
small_font = pygame.font.Font(None, 18)

# Bubble Sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Quick Sort function
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

# Merge Sort function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Function to draw the bars and labels
def draw_bars(arr, x_offset=0, color=(0, 255, 0), label=None):
    for i, height in enumerate(arr):
        pygame.draw.rect(
            screen,
            color,
            (
                x_offset + i * (BAR_WIDTH + GAP),
                HEIGHT - height,
                BAR_WIDTH,
                height,
            ),
        )
        index_text = small_font.render(str(i), True, (255, 255, 255))
        screen.blit(index_text, (x_offset + i * (BAR_WIDTH + GAP) + 2, HEIGHT - height - 30))
    if label:
        screen.blit(label, (x_offset + 5, 5))

# Main loop
running = True
sorted_flag = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not sorted_flag:
        bubble_sort(bar_heights_bubble)
        quick_sort(bar_heights_quick, 0, len(bar_heights_quick) - 1)
        merge_sort(bar_heights_merge)
        sorted_flag = True

    screen.fill(BG_COLOR)
    draw_bars(bar_heights_bubble, x_offset=0, color=(255, 0, 0), label=bubble_label)  # Red for Bubble Sort
    draw_bars(bar_heights_quick, x_offset=WIDTH // 3, color=(0, 255, 0), label=quick_label)  # Green for Quick Sort
    draw_bars(bar_heights_merge, x_offset=(2 * WIDTH) // 3, color=(0, 0, 255), label=merge_label)  # Blue for Merge Sort
    pygame.display.update()

pygame.quit()
