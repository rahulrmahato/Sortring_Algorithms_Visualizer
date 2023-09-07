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
bar_heights_selection = bar_heights_bubble.copy()  # Initialize Selection Sort array
bar_heights_insertion = bar_heights_bubble.copy()  # Initialize Insertion Sort array

# Sorting algorithm labels and colors
font = pygame.font.Font(None, 36)
algorithm_labels = {
    "Bubble Sort": {"color": (255, 0, 0), "array": bar_heights_bubble},
    "Quick Sort": {"color": (0, 255, 0), "array": bar_heights_quick},
    "Merge Sort": {"color": (0, 0, 255), "array": bar_heights_merge},
    "Selection Sort": {"color": (255, 255, 0), "array": bar_heights_selection},
    "Insertion Sort": {"color": (255, 0, 255), "array": bar_heights_insertion},
}

# Small font for individual bar labels
small_font = pygame.font.Font(None, 18)

# Sorting algorithm functions
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

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

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Function to draw the bars and labels
def draw_bars(arr, label, x_offset=0):
    actual_label = label
    if label.endswith(" (Running)"):
        actual_label = label.replace(" (Running)", "")  # Remove the "(Running)" suffix for dictionary lookup

    for i, height in enumerate(arr):
        pygame.draw.rect(
            screen,
            algorithm_labels[actual_label]["color"],  # Use the color from the algorithm_labels dictionary
            (
                x_offset + i * (BAR_WIDTH + GAP),
                HEIGHT - height,
                BAR_WIDTH,
                height,
            ),
        )
        index_text = small_font.render(str(i), True, (255, 255, 255))
        screen.blit(index_text, (x_offset + i * (BAR_WIDTH + GAP) + 2, HEIGHT - height - 30))
    label_text = small_font.render(label, True, algorithm_labels[actual_label]["color"])  # Use the color from the algorithm_labels dictionary
    screen.blit(label_text, (x_offset + 5, 5))

# Main loop
running = True
sorted_flag = False

legend_offset = 0  # Offset for displaying legend labels

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not sorted_flag:
        for label in algorithm_labels.keys():
            algorithm_array = algorithm_labels[label]["array"]
            algorithm_name = label
            algorithm_name += " (Running)" if algorithm_name not in ["Bubble Sort", "Quick Sort"] else ""
            draw_bars(algorithm_array.copy(), algorithm_name)
            if algorithm_name == "Bubble Sort":
                bubble_sort(algorithm_array)
            elif algorithm_name == "Quick Sort":
                quick_sort(algorithm_array, 0, len(algorithm_array) - 1)
            elif algorithm_name == "Merge Sort":
                merge_sort(algorithm_array)
            elif algorithm_name == "Selection Sort":
                selection_sort(algorithm_array)
            elif algorithm_name == "Insertion Sort":
                insertion_sort(algorithm_array)
            draw_bars(algorithm_array, algorithm_name)

        sorted_flag = True
    else:
        # Display legend labels separately
        for label in algorithm_labels.keys():
            algorithm_name = label
            legend_text = small_font.render(algorithm_name, True, algorithm_labels[label]["color"])
            screen.blit(legend_text, (legend_offset, 5))
            legend_offset += 200  # Adjust the offset for spacing between legend labels

    pygame.display.update()

pygame.quit()
