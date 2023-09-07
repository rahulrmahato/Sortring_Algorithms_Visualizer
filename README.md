# Sorting Algorithms Visualizer

This Python program is a sorting algorithms visualizer that allows you to observe the sorting process of three different sorting algorithms: Bubble Sort, Quick Sort, and Merge Sort. The visualization is achieved through graphical bars displayed on a Pygame window.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Sorting Algorithms](#sorting-algorithms)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. Install the Pygame library if you haven't already:
   ```bash
   pip install pygame
   ```

3. Clone or download this repository to your local machine.

## Usage

1. Navigate to the directory where you have the code.

2. Run the script:
   ```bash
   python sorting_visualizer.py
   ```

3. The visualizer window will appear, displaying bars with random heights.

4. Watch as the three sorting algorithms work to arrange the bars in ascending order. Each sorting algorithm is represented by bars of a different color.

5. Once the sorting is complete, you can close the window to exit the program.

## Sorting Algorithms

### Bubble Sort

- Bubble Sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed.

### Quick Sort

- Quick Sort is a fast, recursive, and in-place sorting algorithm that divides a list into smaller sublists and sorts those sublists independently. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.

### Merge Sort

- Merge Sort is an efficient, stable, and comparison-based sorting algorithm that divides the unsorted list into n sublists, each containing one element, and then repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining.

## Customization

You can customize various aspects of the visualizer and sorting algorithms:

- Adjust the number of bars, their heights, and colors by modifying the code in the `generate_random_bars` function and the `draw_bars` function.

- Change the sorting algorithms' behavior or add new ones by modifying the sorting functions defined in the code.

- Customize the Pygame window, including screen dimensions and captions, by modifying the relevant constants.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. We welcome improvements, bug fixes, and new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

![Screenshot 2023-09-07 214155](https://github.com/rahulrmahato/Sortring_Algorithms_Visualizer/assets/82278176/7cd84ef1-db2c-4d7c-847e-634c01a30450)

---

![Screenshot 2023-09-07 214117](https://github.com/rahulrmahato/Sortring_Algorithms_Visualizer/assets/82278176/f2298a46-4677-4e9a-ac16-63a0b0888986)

---

![Screenshot 2023-09-07 220711](https://github.com/rahulrmahato/Sortring_Algorithms_Visualizer/assets/82278176/1611baef-725b-4b32-af99-a67ccb2c1de6)
