
<body>

<h1>Magic Square Generator</h1>

<p>This repository contains a Python script that generates a magic square of size <code>n x n</code>. A magic square is a grid of numbers where the sums of the numbers in each row, column, and both main diagonals are equal.</p>

<h2>Code Overview</h2>

<p>The code defines a function <code>magic_square(n)</code> which creates an <code>n x n</code> magic square using a specific algorithm. The function initializes an empty matrix, then fills it with numbers from 1 to <code>n*n</code> such that the matrix satisfies the properties of a magic square.</p>


<h2>Usage</h2>

<ol>
    <li><strong>Clone the repository:</strong>
        <pre><code>git clone https://github.com/your-username/magic-square-generator.git</code></pre>
    </li>
    <li><strong>Navigate to the directory:</strong>
        <pre><code>cd magic-square-generator</code></pre>
    </li>
    <li><strong>Run the script:</strong>
        <pre><code>python magic_square.py</code></pre>
    </li>
    <li><strong>Change the size of the magic square by modifying the argument in <code>magic_square(n)</code>. For example, to generate a 7x7 magic square, call <code>magic_square(7)</code>.</strong></li>
</ol>

<h2>Example Output</h2>

<p>Running the script with <code>n = 5</code> will output:</p>

<div class="example-output">
17 24  1  8 15<br>
23  5  7 14 16<br>
 4  6 13 20 22<br>
10 12 19 21  3<br>
11 18 25  2  9
</div>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Contributing</h2>

<p>Feel free to submit issues or pull requests if you have any suggestions or improvements.</p>

<h2>Acknowledgements</h2>

<p>The magic square algorithm used here is based on the standard algorithm for generating odd-order magic squares.</p>

</body>

